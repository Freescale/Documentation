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

    MACHINE ??= 'wandboard'
    DISTRO ?= 'fslc-framebuffer'
    PACKAGE_CLASSES ?= "package_rpm"
    EXTRA_IMAGE_FEATURES ?= "debug-tweaks"
    USER_CLASSES ?= "buildstats image-mklibs image-prelink"
    PATCHRESOLVE = "noop"
    BB_DISKMON_DIRS = "\
        STOPTASKS,${TMPDIR},1G,100K \
        STOPTASKS,${DL_DIR},1G,100K \
        STOPTASKS,${SSTATE_DIR},1G,100K \
        STOPTASKS,/tmp,100M,100K \
        ABORT,${TMPDIR},100M,1K \
        ABORT,${DL_DIR},100M,1K \
        ABORT,${SSTATE_DIR},100M,1K \
        ABORT,/tmp,10M,1K"
    PACKAGECONFIG_append_pn-qemu-native = " sdl"
    PACKAGECONFIG_append_pn-nativesdk-qemu = " sdl"
    CONF_VERSION = "1"

    DL_DIR ?= "${BSPDIR}/downloads/"

Important variables:

* ``MACHINE``: Specifies the machine
* ``DISTRO``: Specifies the distro
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
      ${BSPDIR}/sources/meta-openembedded/meta-multimedia \
      \
      ${BSPDIR}/sources/meta-freescale \
      ${BSPDIR}/sources/meta-freescale-3rdparty \
      ${BSPDIR}/sources/meta-freescale-distro \
    "

Layer configuration file ``meta-freescale/conf/layer.conf``
---------------------------------------------------------

This is basically a template that specifies the layer's name and structure::

    # We have a conf and classes directory, add to BBPATH
    BBPATH .= ":${LAYERDIR}"

    # We have a packages directory, add to BBFILES
    BBFILES += "${LAYERDIR}/recipes-*/*/*.bb \
                ${LAYERDIR}/recipes-*/*/*.bbappend"

    BBFILE_COLLECTIONS += "freescale-layer"
    BBFILE_PATTERN_freescale-layer := "^${LAYERDIR}/"
    BBFILE_PRIORITY_freescale-layer = "5"

    # Add the Freescale-specific licenses into the metadata
    LICENSE_PATH += "${LAYERDIR}/custom-licenses"

    FSL_EULA_FILE = "${LAYERDIR}/EULA"

    IMX_MIRROR ?= "http://www.freescale.com/lgfiles/NMG/MAD/YOCTO/"
    QORIQ_MIRROR ?= "http://git.freescale.com/source/"

    # FIXME: set this to avoid changing all the recipes that use it
    FSL_MIRROR ?= "${IMX_MIRROR}"

    MIRRORS += " \
    ${IMX_MIRROR}   http://download.ossystems.com.br/bsp/freescale/source/ \n \
    ${QORIQ_MIRROR} http://download.ossystems.com.br/bsp/freescale/source/ \n \
    "

    # The dynamic-layers directory hosts the extensions and layer specific
    # modifications related to Freescale products.
    #
    # The .bbappend and .bb files are included if the respective layer
    # collection is available.
    BBFILES += "${@' '.join('${LAYERDIR}/dynamic-layers/%s/recipes*/*/*.bbappend' % layer \
                   for layer in BBFILE_COLLECTIONS.split())}"
    BBFILES += "${@' '.join('${LAYERDIR}/dynamic-layers/%s/recipes*/*/*.bb' % layer \
                   for layer in BBFILE_COLLECTIONS.split())}"

Important variables:

* ``BBFILES``: Specifies where BitBake looks for ``.bb*`` files
* ``BBFILE_PRIORITY_freescale``: Specifies priority for recipes in the meta-freescale layer
* ``MIRRORS``: Specifies additional paths where the build system can find source code


Machine configuration file: ``meta-freescale/conf/imx6slevk.conf``
-------------------------------------------------------------------

Machine configurations look like this::

    #@TYPE: Machine
    #@NAME: Freescale i.MX6SL Evaluation Kit
    #@SOC: i.MX6SL
    #@DESCRIPTION: Machine configuration for Freescale i.MX6SL Evaluation Kit
    #@MAINTAINER: Otavio Salvador <otavio@ossystems.com.br>

    MACHINEOVERRIDES =. "mx6:mx6sl:"

    include conf/machine/include/imx-base.inc
    include conf/machine/include/tune-cortexa9.inc

    KERNEL_DEVICETREE = "imx6sl-evk.dtb imx6sl-evk-csi.dtb imx6sl-evk-ldo.dtb \
                         imx6sl-evk-uart.dtb imx6sl-evk-btwifi.dtb"

    UBOOT_CONFIG ??= "sd"
    UBOOT_CONFIG[sd] = "mx6slevk_config,sdcard"
    UBOOT_CONFIG[epdc] = "mx6slevk_epdc_config"
    UBOOT_CONFIG[spinor] = "mx6slevk_spinor_config"
    UBOOT_CONFIG[mfgtool] = "mx6slevk_config"

    SERIAL_CONSOLE = "115200 ttymxc0"

    MACHINE_FEATURES += " pci wifi bluetooth"

    MACHINE_FIRMWARE += "linux-firmware-ath6k firmware-imx-epdc"

Important variables:

* ``IMAGE_FSTYPES``: Located in `imx-base.inc <http://git.yoctoproject.org/cgit/cgit.cgi/meta-freescale/tree/conf/machine/include/imx-base.inc>`_.
  Defines the type of outputs for the root filesystem. Default is: ``"sdcard.gz"``
* ``UBOOT_ENTRYPOINT_*``: Located in `imx-base.inc <http://git.yoctoproject.org/cgit/cgit.cgi/meta-freescale/tree/conf/machine/include/imx-base.inc>`_.
  Defines where the Kernel is loaded by U-boot
* ``SOC_FAMILY``: Defines the machine's family. Only recipes with the same ``SOC_FAMILY`` (defined with the recipe's variable ``COMPATIBLE_MACHINE``)
  are taken into account when baking for a particular machine.
* ``UBOOT_MACHINE``: Defines the u-boot configuration file
