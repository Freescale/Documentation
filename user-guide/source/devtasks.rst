Common Development Tasks
========================

.. _new-layer:

Creating a new layer
---------------------

Use a custom layer when creating or modifying any metadata file (recipe,
configuration file, or class). The main reason is **modularity**. On the other hand,
make sure your new metadata has not already be implemented (layer, recipe or machine), so
before proceeding check the main `Layer Index`_.


1. To have access to Yocto scripts, run the setup environment script under your ``BASE``
   directory::

    fsl-community-bsp $ . setup-environment build

2. Move to the place you want to create your layer and choose a name
   (e.g. ``fsl-custom``)::

    sources $ yocto-layer create fsl-custom
    # Answer the questions. Make sure the priority is set correctly (higher numbers,
    # higher priorities). Set the priority equal to the lowest already present, except
    # when you create a new recipe with the same name as another recipe and want to shadow
    # the original one.

3. Add any metadata content. Suggestion: Version the layer with GIT

4. Edit and add the layer to the ``build/conf/bblayers.conf`` file

5. To verify that your layer is `seen` by BitBake, run the following command under
   the ``BUILD`` folder::

    build $ bitbake-layers show-layers

6. You can now include any new image/machine definitions in your layer. If you
   created a new recipe and want to include it on your next build, add it to your
   ``build/conf/local.conf`` file through the ``CORE_IMAGE_EXTRA_INSTALL`` variable.

.. _patching-kernel:

Patching the Linux Kernel
-------------------------

The Linux Kernel is just another Yocto recipe, so by learning to patch it, you learn
to patch any other package. On the other hand, Yocto **should not** be used for
package development. However, if the need does arise, follow the steps listed below. It is assumed
that you have already built the package you want to patch.

* Create the patch or patches. In this example we are patching the
  Linux kernel for `wandboard-dual machine <http://www.wandboard.org/>`_;
  in other words, the value of ``MACHINE`` in ``build/conf/local.conf`` is
  ``MACHINE ??= 'wandboard-dual'``

* If you already have the patches available, make sure they can be applied cleanly with
  the commands ``git apply --check <PATCH_NAME>``. To create new or additional patches::

    build $ cd tmp/work/wandboard_dual-poky-linux-gnueabi/linux-wandboard/3.0.35-r0/git
    # Edit any files you want to change
    $ git add <modified file 1> <modified file 2> ..
    $ git commit -s -m '<your commit's title>'	# Create the commit
    $ git format-patch -1			# Create the patch

* Create a new layer (see :ref:`new-layer`)

* In the new layer (e.g ``meta-fsl-custom``), create the corresponding sub-directories
  and the ```.bbfile``::

    sources $ mkdir -p \
                       meta-fsl-custom/recipes-kernel/linux/linux-wandboard-3.0.35/
    sources $ cat > meta-fsl-custom/recipes-kernel/linux/linux-wandboard_3.0.35.bbappend << EOF
                    FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}-${PV}:"
                    SRC_URI += "file://0001-calibrate-Add-printk-example.patch"
                    PRINC := "${@int(PRINC) + 1}"
                    EOF

* Move the patch to the new layer::

    sources $ cp ../build/tmp/work/wandboard_dual-poky-linux-gnueabi/linux-wandboard/3.0.35-r0/git/0001-calibrate-Add-printk-example.patch \
                 meta-fsl-custom/recipes-kernel/linux/linux-wandboard-3.0.35

* Setup the environment and clean previous package's build data (``sstate``)::

    fsl-community-bsp $ . setup-environment build
    build $ bitbake -c cleansstate linux-wandboard

* Compile and Deploy::

    build $ bitbake -f -c compile linux-wandboard # -f indicates bitbake to re-execute the compile task
    build $ bitbake -c deploy linux-wandboard

* Insert the SD into your Host and copy the ``uImage`` into the first partition.
  Do not forget to unmount the partition before removing the card!::

    build $ sudo cp tmp/deploy/images/uImage /media/Boot

* Insert the SD into your board and test your change.

.. _building-kernel-manually:

Building the Kernel Manually
----------------------------

* Prepare the Yocto/BitBake environment::

    fsl-community-bsp $ . setup-environment build

* Build the toolchain::

    build $ bitbake meta-toolchain
    # Other toolchains:
    #   Qt Embedded toolchain build: bitbake meta-toolchain-qte
    #   Qt X11 toolchain build: bitbake meta-toolchain-qt

* Install it on your PC::

    build $ sudo sh tmp/deploy/sdk/poky-eglibc-x86_64-arm-toolchain-<version>.sh

* Setup the toolchain environment::

    build $ source /opt/poky/<version>/environment-setup-armv7a-vfp-neon-poky-linux-gnueabi

* Get the Linux Kernel source code::

    $ git clone git://git.freescale.com/imx/linux-2.6-imx.git linux-imx
    $ cd linux-imx

* Create a local branch::

    linux-imx $ BRANCH=imx_3.0.35_4.0.0 # Change to any branch you want,
                                        # Use 'git branch -a' to list all
    linux-imx $ git checkout -b my-${BRANCH} origin/${BRANCH}

* Define/Export ``ARCH`` and ``CROSS_COMPILE``::

    linux-imx $ export ARCH=arm
    linux-imx $ export CROSS_COMPILE=arm-poky-linux-gnueabi-
    linux-imx $ unset LDFLAGS

* Choose a configuration and compile::

    linux-imx $ make imx6_defconfig
    linux-imx $ make uImage

* To Test your changes, copy the ``uImage`` into your SD Card::

    linux-imx $ sudo cp arch/arm/boot/uImage /media/Boot

* If you want your changes to be reflected in your Yocto Framework,
  create the patches following the subsection :ref:`patching-kernel`

.. _contributing:

Contributing
------------

The Yocto Project is open-source, so anyone can contribute. No matter
what your contributions are (bug fixes or new metadata), they should be sent
as patches to the community list. Many eyes will look at your patch, and
at some point it will either be accepted or rejected.

Follow these steps to contribute:

* Make sure you have previously configured your personal info::

    $ git config --global user.name "Your Name Here"
    $ git config --global user.email "your_email@example.com"

* Subscribe to the `meta-freescale Mailing List`_

* Always base your work on **master** branches::

    fsl-community-bsp $ repo init \
        -u https://github.com/Freescale/fsl-community-bsp-platform \
        -b master
    fsl-community-bsp $ repo sync

* Create local branches so your work is **not** done on master::

    fsl-community-bsp $ repo start <branch name> --all

Where ``<branch name>`` is any name you want to give to your local branch (e.g.
``fix_uboot_recipe``, ``new_gstreamer_recipe``, etc.)

* Make your changes in any Freescale related folder (e.g. ``sources/meta-fsl-arm``).
  In case you modified a recipe (.bb) or include (.inc) file, do not forget to `bump`
  (increase the value by one) either the ``PR`` or ``INC_PR`` value

* Commit your changes using `GIT`. In this example we assume your change is on ``meta-fsl-arm`` folder::

    sources/meta-fsl-arm $ git add <file 1> <file 2>
    sources/meta-fsl-arm $ git commit

In the commit's log, the title must start with the filename that was changed or created,
followed by a brief description of the patch's goal. On subsequent lines, provide a thorough description of the changes.
Make sure you follow the standards (type ` git log --pretty=oneline` to see previous commits)

* Create a patch::

    sources/meta-fsl-arm $ git format-patch -s --subject-prefix='<meta-fsl-arm][PATCH' -1

Where the last parameter (``-1``) indicate to patch the last commit.
In case you want to create patches for older commits, just indicate the correct index.
If your patch is done in another folder, just make sure you change the `--subject-prefix` value.

* Send your patch or patches with::

    git send-email --to meta-freescale@yoctoproject.org <patch>

where ``<patch>`` is the file created by ``git format-patch``.

* Keep track of patch responses on the mailing list. In case you need to rework your patch,
  repeat the steps but this time change the patch's subject to
  ``--subject-prefix='<meta-fsl-*][PATCH v2'``

* Once your patch has been approved, you can delete your working branches::

    fsl-community-bsp $ repo abandon <branch name>

.. links
.. _Layer Index: http://layers.openembedded.org/layerindex/layers/
.. _meta-freescale Mailing List: https://lists.yoctoproject.org/listinfo/meta-freescale
