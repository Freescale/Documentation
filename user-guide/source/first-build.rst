Compiling your first build
==========================

Synchronize your source code
****************************

Make sure that your copy of the source code is up-to-date. So, run this command
to synchronize it::

    $ repo sync

Create your local branch
************************

Do your work on a different branch, to help organizing your work. You can do
that by running this repo command::

    $ repo start <new branch name> --all

*Why should I create a local branch?*

If you change *any* source code (for example, choosing another preferred kernel)
and want to sync again, or use master instead of a stable branch, you will be
able to rebase or sync your source code, even with your changes. This will also
make easier in case you find a bug, fix it, and want to send a patch back to the
community.

Choose your board
*****************

To setup your build environment run the following command on the project root::

    $ source setup-environment build

After the command finishes you will be in the newly created build directory. All
build actions will happen inside using this directory as starting point.

The default board for daisy is imx6qsabresd, you can choose QSB or imx28 if you
prefer::

    $ vi conf/local.conf

Your default local.conf file can looks like::

    MACHINE ??= 'imx6qsabresd'
    DISTRO ?= 'poky'
    PACKAGE_CLASSES ?= "package_rpm"
    EXTRA_IMAGE_FEATURES = "debug-tweaks"
    USER_CLASSES ?= "buildstats image-mklibs image-prelink"
    PATCHRESOLVE = "noop"
    BB_DISKMON_DIRS = "\
    STOPTASKS,${TMPDIR},1G,100K \
    STOPTASKS,${DL_DIR},1G,100K \
    STOPTASKS,${SSTATE_DIR},1G,100K \
    ABORT,${TMPDIR},100M,1K \
         ABORT,${DL_DIR},100M,1K \
    ABORT,${SSTATE_DIR},100M,1K"
    CONF_VERSION = "1"

    BB_NUMBER_THREADS = '4'
    PARALLEL_MAKE = '-j 4'
    ACCEPT_FSL_EULA = ""

Change the MACHINE variable to your board name. In order to figure out what is
the machine name you can list the machines directory. Here is the command to do
so for the Freescale boards::

    $ ls ../sources/meta-fsl-arm/conf/machine/*.conf | \
      xargs -n1 -i basename {} .conf | sort
    imx23evk
    imx28evk
    imx31pdk
    imx35pdk
    imx51evk
    imx53ard
    imx53qsb
    imx6dlsabreauto
    imx6dlsabresd
    imx6qsabreauto
    imx6qsabresd
    imx6slevk
    imx6solosabreauto
    imx6solosabresd
    twr-vf65gs10

For non-Freescale boards use::

    $ ls ../sources/meta-fsl-arm-extra/conf/machine/*.conf | \
      xargs -n1 -i basename {} .conf | sort
    cfa10036
    cfa10037
    cfa10049
    cfa10055
    cfa10056
    cfa10057
    cfa10058
    cgtqmx6
    cubox-i
    imx233-olinuxino-maxi
    imx233-olinuxino-micro
    imx233-olinuxino-mini
    imx233-olinuxino-nano
    imx6qsabrelite
    m28evk
    m53evk
    nitrogen6x
    nitrogen6x-lite
    pcl052
    pcm052
    quartz
    wandboard-dual
    wandboard-quad
    wandboard-solo

And to print all the boards just use both directories::

    $ ls ../sources/meta-fsl-arm/conf/machine/*.conf \
      ../sources/meta-fsl-arm-extra/conf/machine/*.conf | \
      xargs -n1 -i basename {} .conf | sort
    cfa10036
    cfa10037
    cfa10049
    cfa10055
    cfa10056
    cfa10057
    cfa10058
    cgtqmx6
    cubox-i
    imx233-olinuxino-maxi
    imx233-olinuxino-micro
    imx233-olinuxino-mini
    imx233-olinuxino-nano
    imx23evk
    imx28evk
    imx31pdk
    imx35pdk
    imx51evk
    imx53ard
    imx53qsb
    imx6dlsabreauto
    imx6dlsabresd
    imx6qsabreauto
    imx6qsabrelite
    imx6qsabresd
    imx6slevk
    imx6solosabreauto
    imx6solosabresd
    m28evk
    m53evk
    nitrogen6x
    nitrogen6x-lite
    pcl052
    pcm052
    quartz
    twr-vf65gs10
    wandboard-dual
    wandboard-quad
    wandboard-solo

Please be sure to use the exact name of the board as the value of the variable,
as the tools will complain if a different name is used.

Also, look at the meta-fsl-arm:daisy release notes: Freescale Community BSP Release Notes
1.6 documentation for more information about new boards added on this release.

Starting your first build
*************************

The biggest image from *meta-fsl-demos* is **fsl-image-gui**. It has X11,
gstreamer, fsl codec for gstreamer, unit-test, gpu, one gpu sample (with source
code) for imx53 and QT 4.8. But it takes a lot of time to build (if you are luck
and have a powerful machine, it will take only few hours). If you have already
built it once, it will take about 3 seconds to decide nothing has been changed
and about 15 minutes to generate the image file (it's a 750MB rootfs, so it does
take some time to create such big file).

There are several other images you can create. In order to see which ones are
present on the Poky Platfom Builder (the core tool of the Yocto Project), please
run::

    $ ls ../sources/poky/meta*/recipes*/images/*.bb | \
      xargs -n1 -i basename {} .bb | sort
    build-appliance-image_8.0
    core-image-base
    core-image-clutter
    core-image-directfb
    core-image-full-cmdline
    core-image-lsb
    core-image-lsb-dev
    core-image-lsb-sdk
    core-image-minimal
    core-image-minimal-dev
    core-image-minimal-initramfs
    core-image-minimal-mtdutils
    core-image-multilib-example
    core-image-rt
    core-image-rt-sdk
    core-image-sato
    core-image-sato-dev
    core-image-sato-sdk
    core-image-testmaster
    core-image-testmaster-initramfs
    core-image-weston
    core-image-x11
    qt4e-demo-image

Also, if you added other layers there may be other images available to
you. Check their documentation to see the available images provided by them.

For your first image, start with **core-image-base**. It does not have X11,
gstreamer or QT, but it only take 30 minutes to build at first time. And it
should work just fine for any board.

Following the complete sequence of commands, make sure you're on the right
build directory (named "build", if you followed this tutorial to the letter),
then run::

    $ bitbake core-image-base

And then the build process will start.

.. note:: as of 2014-02-24, the required disk space for building a
          *core-image-image* is about ~18GB.
