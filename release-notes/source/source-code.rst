.. include:: variables.inc
Software Architecture
*********************

.. _soc-hierarchy:

SoC Hierarchy
============================

The following tree shows the SoC hierarchy:

.. blockdiag:: soc-tree.diag
   :scale: 60%
   :align: center

.. _machine-overrides-extender:

What is machine-overrides-extender Class
========================================

The `Machine Overrides Extender class <https://github.com/Freescale/meta-freescale/blob/master/classes/machine-overrides-extender.bbclass>`_
is a class from **meta-freescale** created to extend some machine overrides
depending on which `SoC <https://en.wikipedia.org/wiki/System_on_a_chip>`_
is part of a
`MPSoC <https://en.wikipedia.org/wiki/Multiprocessor_system_on_a_chip>`_.
For example, a MPSoC has IPU, and GPU for 3D, but does not have GPU for 2D.

The list of SoC on a given MPSoC is known and does not change overtime. The
current MPSoC configuration can be found in file
`imx-base.inc <https://github.com/Freescale/meta-freescale/blob/master/conf/machine/include/imx-base.inc>`_,
the lines where the variable ``MACHINEOVERRIDES_EXTENDER`` is set for each MPSoC.
When a new machine file is added to **meta-freescale**, defining the MPSoC is
enough.

The Machine Overrides Extender class adds the pre-determined list of SoC
configured for that MPSoC to the ``MACHINEOVERRIDE``, and as a consequence,
the BSP packages are properly configured for that machine by default.

In other words, when adding a new machine support, the user only need to know
the MPSoC for that machine, the **meta-freescale** BSP support is already
configured to provide the proper package depending on the MPSoC (and this is
configured via Machine Overrides Extender).

This meas any new machine added in future can use the configured BSP provided by
**meta-freescale**.

On top of the hardware architecture which impacts the BSP, there are also the
software architecture. There are three supported BSPs:

* ``imx-generic-bsp``: Used to configure any generic aspect of the BSP, for example,
  those configurations that depends only on the MPSoC.

* ``imx-mainline-bsp``: Used to configure the mainline packages.

* ``imx-nxp-bsp``: Used to configure the packages provided by NXP.

The BPS overrides are provided to allow the user to chose between the BSPs and
using the proper package for each case.

For example, the recipe
`weston_9.0.0.imx.bb <https://github.com/Freescale/meta-freescale/blob/master/recipes-graphics/wayland/weston_9.0.0.imx.bb#L180-L183>`_
with focus on the following lines::

   PACKAGECONFIG:remove:imxfbdev = "kms"
   PACKAGECONFIG:append:imxfbdev = " fbdev clients"
   PACKAGECONFIG:append:imxgpu   = " imxgpu"
   PACKAGECONFIG:append:imxgpu2d = " imxg2d"

In this recipe, the ``PACKAGECONFIG`` is configured depending on the SoC, for
the SoCs with ``imxfvdev``, the weston package should not include the
configuration ``kms``, and includes ``fbdev`` and ``clients``.

For the MPSoC ``mx6q``, the overrides does include ``imxfbdev``, ``imxgpu``
and ``imxgpu2``::

   MACHINEOVERRIDES_EXTENDER:mx6q:use-nxp-bsp = "imx-generic-bsp:imx-nxp-bsp: \
   imxfbdev:imxipu:imxvpu:imxgpu:imxgpu2d:imxgpu3d:mx6-generic-bsp:mx6-nxp-bsp: \
   mx6q-generic-bsp:mx6q-nxp-bsp"


For the MPSoC ``mx8mm``, the overrides does not include ``imxfbdev`` and include
``imxgpu`` and ``imxgpu2``::

   MACHINEOVERRIDES_EXTENDER:mx8mm:use-nxp-bsp = "imx-generic-bsp:imx-nxp-bsp: \
   imxdrm:imxvpu:imxgpu:imxgpu2d:imxgpu3d:mx8-generic-bsp:mx8-nxp-bsp: \
   mx8m-generic-bsp:mx8m-nxp-bsp:mx8mm-generic-bsp:mx8mm-nxp-bsp"

The Weston configuration has a different value for ``mx6q`` and ``mx8mm``,
because both MPSoC are different.

.. _linux-providers:

Linux Kernel
============

|project_name| supports the following sources for Linux Kernel:

.. tabularcolumns:: l | l | l
.. include:: fsl-community-bsp-supported-kernels.inc

As stated in :ref:`kernel_release_notes`, |project_name| is not responsible for
the Linux Kernel content in any kernel provider. If you are looking for the
feature list, supported devices, official way to get a support channel or how to
report bug, please, see above where to get help, for each kernel provider.

 * **linux-imx**: provider, Freescale has a release notes document for each
   version released. This document has a list of known issues, new features,
   list of kernel arguments, and the linux-imx kernel scope for each Freescale
   Reference Board. This document is present into the Document Bundle provided
   by Freescale.

Default Linux Providers
-----------------------

The following table shows the default version of Linux Kernel provided by
|project_name| for each supported machine.

.. tabularcolumns:: l | l | l
.. table:: Default Linux kernel version for each supported machine

   .. include:: linux-default.inc

Bootloaders
============

|project_name| supports barebox and u-boot as bootloaders.

.. tabularcolumns:: l | l | l
.. include:: fsl-community-bsp-supported-bootloaders-descr.inc


The following table shows the default bootloaders (and their
versions) for the supported boards.

.. tabularcolumns:: l | l | l
.. table:: Default bootloader version for each supported machine

   .. include:: bootloader-default.inc

User Space Packages
===================

There is a huge number of user space packages provided by the Yocto Project.
The following table shows some version for few highlighted packages.

.. tabularcolumns:: l | c | l
.. table:: Main user space package versions

   .. include:: userspace-pkg.inc

Freescale User Space Packages
-----------------------------
This section shows the version package for each board.
Those packages provide hardware acceleration for GPU or VPU,
hardware optimization or some hardware test tools.

 * **Hardware acceleration** is achieved using a different core
   for processing some specific task. In this case, GPU or VPU.

 * **Hardware optimization** is achieved with some changes in source
   code in order to get a better performance for a specific task
   on a specific hardware. For example, audio decode made by software,
   but with optimizations for ARM.

 * **Hardware-specific** is applicable when the package was designed to
   be executed on a specific hardware, and it does not make sense
   on other hardware. For example, imx-test is a test package for
   imx boards. It can be cross-compiled for any other core, although
   it will only behave as expect if executed on imx boards.

The package version and variety varies on :ref:`soc-hierarchy`.
For example, machines with i.MX28 SoC does not have VPU, the recipe imx-vpu is
not needed. There are differences, as well, in GPU support recipes.

Version by :ref:`soc-hierarchy`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The following table shows the version of each package depending on the
:ref:`soc-hierarchy`.

.. tabularcolumns:: L | C | C | C | C | C | C
.. table:: User space package version by SoC hierarchy

   .. include:: soc-pkg.inc


Hardware relation by :ref:`soc-hierarchy`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The following table shows how packages interact with hardware depending on the
:ref:`soc-hierarchy`

.. tabularcolumns:: L | C | C  | C  | C
.. table:: Hardware dependent packages

   .. include:: soc-pkg-optimization.inc

PackageGroups and Images
========================

The |project_name| provides a list of PACKAGEGROUPS and images intended to ease
the initial development of custom applications.

The main goal is not to provide a production solution, on the contrary, it
should be seen as an example of package set for a specific IP development, and
an example of initial generic development and test images.

PACKAGEGROUPS
-------------

The following list shows the current PACKAGEGROUPs available in |release_name|
when using |project_name|.

You can understand what a PACKAGEGROUPS is and learn how to use it in `Yocto
Project Development Manual
<http://www.yoctoproject.org/docs/2.4/dev-manual/dev-manual.html#usingpoky-extend-customimage-customtasks>`_

.. include:: packagegroups.inc

Images
------

The following images are provided by |project_name| only. See the list of Yocto
Project's reference images in `Yocto Project Reference Manual
<http://www.yoctoproject.org/docs/2.4/ref-manual/ref-manual.html#ref-images>`_

.. include:: images.inc

Distros
-------

The following distros are supported by |project_name|.

.. include:: distros.inc

*NOTE: Poky's distros are still available to use.*
