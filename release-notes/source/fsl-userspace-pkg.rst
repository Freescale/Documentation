Freescale Userspace Packages
============================
.. |mm_version| replace:: 3.0.8
.. |libfslvpuwrap_version| replace:: 1.0.38
.. |latest_bsp_version_mx6| replace:: 3.5.7-1.0.0

This section shows the version package for each board.
Those packages provide hardware acceleration for GPU or VPU,
hardware optimization or some hardware test tools.

Hardware acceleration is achieved using a different core
for processing some specific task. In this case, GPU or VPU.

Hardware optimization is achieved with some changes in source
code in order to get a better performance for a specific task 
on a specific hardware. For example, audio decode made by software,
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

* cfa10036
* cfa10037
* cfa10049
* cfa10055
* cfa10056
* cfa10057
* cfa10058
* imx28evk
* m28evk

.. include:: fsl-pkg-imx28.inc

--------
MX5
--------
Freescale userspace packages for mx5 SOC family.

It includes:

* imx51evk
* imx53ard
* imx53qsb
* m53evk

.. include:: fsl-pkg-imx5.inc
             

------------
MX6
------------
Freescale userspace packages for mx6 SOC family

It includes:

* cgtqmx6
* gk802
* imx6dlsabreauto
* imx6dlsabresd
* imx6qsabreauto
* imx6qsabrelite
* imx6qsabresd
* imx6slevk
* imx6solosabreauto
* imx6solosabresd
* nitrogen6x
* wandboard-dual
* wandboard-quad
* wandboard-solo

.. include:: fsl-pkg-imx6.inc

