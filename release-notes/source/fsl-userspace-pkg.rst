Freescale Userspace Packages
============================
.. |mm_version| replace:: 3.0.8
.. |libfslvpuwrap_version| replace:: 1.0.38
.. |latest_bsp_version_mx6| replace:: 3.5.7-1.0.0

This section shows the version package for each board.
Those packages provides hardware acceleration for GPU or VPU,
provides hardware optimization or some hardware test tools.

Hardware acceleration is achieved using a different core
for processing some specific task. In this case, GPU or VPU.

Hardware optimization is achieved with some changes in source
code in order to get a better performance for a specific task 
in a specific hardware. For example, audio decode made by software,
but with optimizations for ARM.

Hardware relate is applicable when the package was designed to
be executed in a specific hardware, and it does not make sense
in other hardware. For example, imx-test is a test package for
imx boards. It can be cross-compiled for any other core, although
it will only act as expect if executed on imx boards.

--------
MX28
--------
Freescale userspace packages for mx28 SOC family.

It includes:

* imx28evk


.. include:: fsl-pkg-imx28.inc

--------
MX5
--------
Freescale userspace packages for mx5 SOC family.

It includes:

* imx51evk
* imx53ard
* imx53qsb

.. include:: fsl-pkg-imx5.inc
             

------------
MX6
------------
Freescale userspace packages for mx6 SOC family

It includes:

* imx6qsabreauto
* imx6qsabresd
* imx6slevk
* imx6dlsabresd
* imx6slevk
* nitrogen6x
* cgtqmx6
* wandboard-solo
* imx6qsabrelite
* wandboard-dual

.. include:: fsl-pkg-imx6.inc

