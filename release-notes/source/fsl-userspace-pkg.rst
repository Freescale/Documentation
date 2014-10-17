Freescale User Space Packages
=============================
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
For example, machines with i.MX28 SoC does not have VPU, the recipe imx-vpu is not needed.
There are differences, as well, in GPU support recipes.

--------------------------------
Version by :ref:`soc-hierarchy`
--------------------------------

The following table shows the version of each package depending on the :ref:`soc-hierarchy`.

.. tabularcolumns:: L | C | C | C | C | C | C
.. table:: User space package version by SoC hierarchy

   .. include:: soc-pkg.inc


-----------------------------------------
Hardware relation by :ref:`soc-hierarchy`
-----------------------------------------

The following table shows how packages interact with hardware depending on the :ref:`soc-hierarchy`

.. tabularcolumns:: L | C | C  | C  | C
.. table:: Hardware dependant packages

   .. include:: soc-pkg-optimization.inc

