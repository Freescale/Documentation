Linux Kernel
============
.. |linux_imx_version_mx6| replace:: 3.0.35_4.1.0
.. |linux_imx_version_mxs5| replace:: 2.6.35_maintain
.. |linux_fslc_version| replace:: 3.11
.. |linux_boundary_version| replace:: 3.0.35_4.1.0
.. |linux_cfa_version| replace:: 3.10
.. |linux_wandboard_version| replace:: 3.0.35_4.0.0


Fsl-community-bsp supports the following sources for Linux Kernel:

* **linux-imx**: Linux Kernel provided and supported by Freescale
* **linux-fslc**: Linux Kernel mainline with backported fixes (kernel.org)
* **linux-boundary**:
* **linux-cfa**: Linux Kernel mainline 3.10 with added drivers
* **linux-denx**:
* **linux-timesys**:
* **linux-wandboard**:

-----------------------
Default Linux Providers
-----------------------

The following table shows the default version of Linux Kernel provided by
FSL Community BSP for each supported machine.

.. include:: linux-default.inc


-----------
linux-fslc
-----------

linux-fslc provides the Linux Kernel |linux_fslc_version| from mainline (kernel.org)
with some backported fixes.

For the mainline kernel some boards has a very good support, although
other ones has only a basic support.

Please, see in the following table which are the main features supported
by mainline kernel for each supporte board.


.. include:: linux-fslc.inc

