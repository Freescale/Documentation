Freescale Userspace Packages
============================
.. |mm_version| replace:: 3.0.10
.. |libfslvpuwrap_version| replace:: 1.0.45
.. |latest_bsp_version_mx6| replace:: 3.10.17-1.0.0
.. |latest_bsp_version_mx5| replace:: 11.09.01


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
   be executed in a specific hardware, and it does not make sense
   in other hardware. For example, imx-test is a test package for
   imx boards. It can be cross-compiled for any other core, although
   it will only act as expect if executed on imx boards.

The package version and variety varies on :ref:`soc-hierarchy`.
For example, machines with i.MX28 SOC does not have VPU, the recipe imx-vpu is not needed.
There are differences, as well, in GPU support recipes.

--------------------------------
Version by :ref:`soc-hierarchy`
--------------------------------

The following table shows the version of each package depending on the :ref:`soc-hierarchy`.

.. include:: soc-pkg.inc


-----------------------------------------
Hardware relation by :ref:`soc-hierarchy`
-----------------------------------------

The following table shows how packages interact with hardware depending on the :ref:`soc-hierarchy`

.. include:: soc-pkg-optimization.inc

