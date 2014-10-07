Building and Customizing the Kernel
===================================

What is a recipe?
*****************

Recipes are the files that define how a package build should act. How is the
package version defined, where it is the mainstream repository, how to build,
install and link the program, service or resource provided by it, and just about
every other action that can happen in the BitBake tool related to the recipe's
package are defined inside this file.

The kernel recipe
*****************

For *meta-fsl-arm* the kernel recipes are under
*meta-fsl-arm/recipes-kernel/linux*. For more information about the Kernel
recipes you can look directly at their source here: `meta-fsl-arm - Layer
containing Freescale ARM hardware support metadata for all kernels
<http://git.yoctoproject.org/cgit/cgit.cgi/meta-fsl-arm/tree/recipes-kernel/linux?h=daisy>`_)

For meta-fsl-arm, there are 3 kernel recipes:

.. note:: TODO: COMPLETE THIS LIST:

* *linux-fslc_3.8.bb*: kernel mainline (from kernel.org)
* *linux-imx_2.6.35.3.bb*: kernel from FSL, for imx5x and imx28
* *linux-imx_3.0.35.bb*: kernel from FSL for imx6

Take the linux-imx for imx6 as an example: `meta-fsl-arm - Layer containing
Freescale ARM hardware support metadata for kernel 3.0.35
<http://git.yoctoproject.org/cgit/cgit.cgi/meta-fsl-arm/tree/recipes-kernel/linux/linux-imx_3.0.35.bb?h=daisy>`_

The recipe defines:

* what's the compatible machine for this linux version (mx6)
* what's the commit ID for the head of this code (SRCREV) (MX6DL and MX6SL have
  different source code)
* what's the patches for the mx6 boards (SRC_URI).

In order to see where the source code is cloned from, you need to go to the .inc
file `meta-fsl-arm - Layer containing Freescale ARM hardware support metadata
<http://git.yoctoproject.org/cgit/cgit.cgi/meta-fsl-arm/tree/recipes-kernel/linux/linux-imx.inc?h=daisy>`_

.. code-block:: console

    SRC_URI = "git://git.freescale.com/imx/linux-2.6-imx.git \
               file://defconfig \
    "

It's from *git.freescale.com*. In addition, there is a *defconfig* file added on
SRC_URI.

There is a *defconfig* file for every board, on every Linux revision. Some
*defconfigs* are shared for more than one board (for example, every mx6 board),
and some Linux versions are not compatible for some boards (for example, imx53
is only compatible with 2.6.35).

During a *bitbake linux-imx*, a temporary directory will be created under
*build/tmp/armv7-imx6\*/linux-imx*, with code from git, applied patches and the
*defconfig*. BitBake will then take the *defconfig* and configure the kernel,
build it, and deploy it.

So, in order to change the kernel configuration (make menuconfig) you **must**
replace your defconfig file from
*meta-fsl-arm/recipes-kernel/linux/linux-imx-3.0.35/mx6*.

How to change the kernel configuration
**************************************

Changing the recipe default kernel configuration is easy. First, create the new
*defconfig* using any way you think it's best, then copy it to the right
directory for your board/kernel recipe, i.e:
*meta-fsl-arm/recipes-kernel/linux/linux-imx-3.0.35/mx6*. After that, run the
following commands:

.. code-block:: console

    $ bitbake -c cleansstate linux-imx
    $ bitbake linux-imx # if you want to build only the kernel image
    $ bitbake fsl-image-gui # if you want to generate a complete image using the new kernel

The first command will clean the sstate-cache information about the kernel while
keeping the downloaded source for it. Essentially, this will redo all the steps
of a recipe while keeping the data that will not change, allowing you to test
changes without having to go through all the download process of something as
large as the Linux kernel tree.

.. note:: If you want to clean up **everything** about a recipe, *including* the
          downloaded source code you will need to run the following command:

          .. code-block:: console

             $ bitbake -c cleanall <recipe-name>

          Keep in mind that unless will have a specific reason for deleting the
          source code of a package it is better to run *cleansstate* than
          *cleanall*.

How to use menuconfig with BitBake
**********************************

To generate a new configuration for your kernel using menuconfig you need to run
the following command:

.. code-block:: console

    $ bitbake -c menuconfig linux-imx

will generate a config file on
*tmp/work/imx6qsabresd-poky-linux-gnueabi/linux-imx/3.0.35-r33.10/git/.config*.
Use this file with any of the tools for configuring the kernel to make the
changes you require, then copy it back to the kernel recipe directory so you can
use it. Run the *cleansstate* command to reset the recipe sstate cache, and then
build it all again:

.. code-block:: console

    $ cp tmp/work/imx6qsabresd-poky-linux-gnueabi/linux-imx/3.0.35-r33.10/git/.config ../sources/meta-fsl-arm/recipes-kernel/linux/linux-imx-3.0.35/mx6/defconfig
    $ bitbake -c cleansstate linux-imx
    $ bitbake fsl-image-gui

The newly built *uImage* file will be under tmp/deploy/images.

If you changed only the *uImage*, and doesn't want to reflash the entire SD card
you can mount the boot partition of the card, and copy just the kernel file to
it:

.. code-block:: console

    $ sudo cp tmp/deploy/image/uImage-imx6-XXX.bin /media/user/Boot imx6/uImage

Using the kernel mainline - kernel.org
**************************************

In order to use kernel mainline instead of linux-imx you just have to add the
following code to your *conf/local.conf*:

.. code-block:: console

    PREFERRED_PROVIDER_virtual/kernel = "linux-fslc"

.. note:: Make sure the desired board is supported by kernel.org before using
          the mainline.

Checkout `this online document
<https://community.freescale.com/docs/DOC-95017>`_ in order to download and
build kernel mainline manually.

Final points
************

Building and customizing the kernel is not a simple task. The Yocto Project
tools are probably not the best tools to use during the development and/or
customization stage of your board's kernel. It is easier to use an external
toolchain, which you can easily create with *bitbake meta-toolchain*. Once the
kernel development/customization is done, the changes (config + patches) can be
integrated in your custom layer (more about that later!) so they are ready for
production use.

A good way to work with the kernel is to have a copy of kernel source code
cloned on your machine directly from *git.freescale.com*, so you can
reconfigure, rebuild, apply some patches, make changes, and build it manually -
in any way you need. After finishing the work on something, apply all the
patches and configuration you have created to the layer kernel recipe, and then
your custom kernel will be available to OpenEmbedded.

Look at the kernel recipes as examples on how to create patches to the
kernel. Also, patches can be applied with just about any recipe, not only
kernels.

If you have any errors, bugs or annoyances giving you headaches you can find
community support within the `meta-freescale e-mail list
<meta-freescale@yoctoproject.org>`_.
