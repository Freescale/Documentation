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
.. table:: Hardware dependant packages

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
<http://www.yoctoproject.org/docs/1.6.1/dev-manual/dev-manual.html#usingpoky-extend-customimage-customtasks>`_

.. include:: packagegroups.inc

Images
------

The following images are provided by |project_name| only. See the list of Yocto
Project's reference images in `Yocto Project Reference Manual
<http://www.yoctoproject.org/docs/current/ref-manual/ref-manual.html#ref-images>`_

.. include:: images.inc
