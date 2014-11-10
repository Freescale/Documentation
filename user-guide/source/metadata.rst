Metadata
========

BitBake handles the parsing and execution of the data files, which consist of various types:

* **Recipes**: Provides details and build information about particular pieces of software
* **Classes**: Abstracts common build subroutines and information (e.g. how to build a Linux kernel)
* **Configuration Data**: Defines machine-specific settings, policy decisions, and so forth. 
  Configuration data acts as the glue to bind everything together.

Layers
------

* Metadata is organized into multiple ``layers``.
* Layers allow you to isolate different types of customizations from each other.
* DO NOT do your modifications in existing layers, instead create a layer and 
  create recipes (``.bb`` files) or modify existing ones (``.bbappend`` files)


Configuration Data
------------------

* ``build/conf/local.conf``: Local user configuration for your build environment
* ``build/conf/bblayers.conf``: Defines layers, which are directory trees,
  traversed by BitBake.
* ``sources/meta-*/conf/layer.conf``: Layer configuration file
* ``sources/meta-*/conf/machine/*.conf``: Machine configuration files


Build's local configuration file ``build/conf/local.conf``
----------------------------------------------------------

By default, the ``setup-enviroment`` script creates a ``local.conf`` like this::

    MACHINE ??= 'wandboard-dual'
    DISTRO ?= 'poky'
    #PACKAGE_CLASSES ?= "package_rpm"
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
    #added by bitbake
    DL_DIR = "/home/b42214/fsl-local/yocto/fsl-community-bsp-dylan/downloads/"
    #added by bitbake
    SSTATE_MIRRORS = ""
    #added by bitbake
    PACKAGE_CLASSES = "package_rpm"

Important variables:

* ``MACHINE``: Specifies the machine, ``imx6qsabresd`` is the default
* ``BB_NUMBER_THREADS`` and ``PARALLEL_MAKE``: Specifies the max number of threads when
  baking and compiling
* ``DL_DIR``: Tarball repository. Several users can share the same folder, so data can 
  be reused.

Build's layer configuration file ``build/conf/bblayers.conf``
-------------------------------------------------------------

* Also created by the ``setup-environment`` script

* In case you need to add a layer, add it to ``BBLAYERS``::

    LCONF_VERSION = "6"

    BBPATH = "${TOPDIR}"
    BSPDIR := "${@os.path.abspath(os.path.dirname(d.getVar('FILE', True)) + '/../..')}"

    BBFILES ?= ""
    BBLAYERS = " \
      ${BSPDIR}/sources/poky/meta \
      ${BSPDIR}/sources/poky/meta-yocto \
      \
      ${BSPDIR}/sources/meta-openembedded/meta-oe \
      \
      ${BSPDIR}/sources/meta-fsl-arm \
      ${BSPDIR}/sources/meta-fsl-arm-extra \
      ${BSPDIR}/sources/meta-fsl-demos \
    "

Layer configuration file ``meta-fsl-arm/conf/layer.conf``
---------------------------------------------------------

This is basically a template that specifies the layer's name and structure::

    # We have a conf and classes directory, add to BBPATH
    BBPATH .= ":${LAYERDIR}"

    # We have a packages directory, add to BBFILES
    BBFILES += "${LAYERDIR}/recipes-*/*/*.bb \
                ${LAYERDIR}/recipes-*/*/*.bbappend"

    BBFILE_COLLECTIONS += "fsl-arm"
    BBFILE_PATTERN_fsl-arm := "^${LAYERDIR}/"
    BBFILE_PRIORITY_fsl-arm = "5"

    FSL_EULA_FILE = "${LAYERDIR}/EULA"

    FSL_MIRROR ?= "http://www.freescale.com/lgfiles/NMG/MAD/YOCTO/"

    MIRRORS += " \
    ${FSL_MIRROR}	http://download.ossystems.com.br/bsp/freescale/source/ \n \
    "

Important variables:

* ``BBFILES``: Specifies where BitBake looks for ``.bb*`` files
* ``BBFILE_PRIORITY_fsl-arm``: Specifies priority for recipes in the meta-fsl-arm layer
* ``MIRRORS``: Specifies additional paths where the build system can find source code


Machine configuration file: ``meta-fsl-arm/conf/imx6qsabresd.conf``
-------------------------------------------------------------------

Machine configurations look like this::

    #@TYPE: Machine
    #@NAME: i.MX6Q SABRE SD
    #@DESCRIPTION: Machine configuration for Freescale i.MX6Q SABRE SD

    include conf/machine/include/imx-base.inc
    include conf/machine/include/tune-cortexa9.inc

    SOC_FAMILY = "mx6:mx6q"

    KERNEL_DEVICETREE = "${S}/arch/arm/boot/dts/imx6q-sabresd.dts"

    UBOOT_MACHINE = "mx6qsabresd_config"

    SERIAL_CONSOLE = "115200 ttymxc0"

    MACHINE_FEATURES += " pci wifi bluetooth"

Important variables:

* ``IMAGE_FSTYPES``: Located in `imx-base.inc <http://git.yoctoproject.org/cgit/cgit.cgi/meta-fsl-arm/tree/conf/machine/include/imx-base.inc>`_.
  Defines the type of outputs for the root filesystem. Default is: ``"tar.bz2 ext3 sdcard"``
* ``UBOOT_ENTRYPOINT_*``: Located in `imx-base.inc <http://git.yoctoproject.org/cgit/cgit.cgi/meta-fsl-arm/tree/conf/machine/include/imx-base.inc>`_.
  Defines where the Kernel is loaded by U-boot
* ``SOC_FAMILY``: Defines the machine's family. Only recipes with the same ``SOC_FAMILY`` (defined with the recipe's variable ``COMPATIBLE_MACHINE``)
  are taken into account when baking for a particular machine.
* ``UBOOT_MACHINE``: Defines the u-boot configuration file
