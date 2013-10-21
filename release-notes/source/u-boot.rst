U-Boot
============
.. |u_boot_fslc_version| replace:: 2013.10-rc4
.. |u_boot_boundary_version| replace:: 2013.07
.. |u_boot_imx_version_mx6| replace:: 2013.04
.. |u_boot_imx_version_mx5| replace:: 2009.08
.. |u_boot_imx_version_mxs| replace:: 2009.08
.. |u_boot_imx_tag_mx6| replace:: imx_v2013.04_3.5.7_1.0.0_alpha
.. |u_boot_imx_tag_mx5| replace:: imx_2.6.35_11.09.01
.. |u_boot_imx_tag_mxs| replace:: imx_2.6.35_10.12.01 branch


Fsl-community-bsp supports two sources for u-boot:


* **u-boot-imx**: U-Boot supported by Freescale
* **u-boot-fslc**: provides the U-Boot |u_boot_fslc_version| version with backported
  fixes and configuration patches related with meta-oe/yocto.
* **u-boot-boundary**: provides the U-Boot |u_boot_boundary_version| supported by
  Boundary Devices. This repository is basicaly kept in-line with true main-line U-Boot,
  but used it as a staging area due to responsive to customer needs. The primary deltas
  at this point are additional boards (nit6xlite is not yet in main-line), support
  for additional displays, and support for custom boards.

--------------
Default u-boot
--------------

The following table shows the default u-boot version and provider for all
supported boards.

.. include:: u-boot-default.inc

------------
u-boot-imx
------------

The following table shows the version of U-Boot provided and supported by Freescale
for each supported machine.

.. include:: u-boot-imx.inc

