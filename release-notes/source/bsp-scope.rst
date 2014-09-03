Scope
=========

FSL Community BSP Scope
---------
The scope of this Release Notes includes the FSL Community BSP meta layers:

 * `meta-fsl-arm <http://git.yoctoproject.org/cgit/cgit.cgi/meta-fsl-arm/?h=daisy>`_:
   provides the base support and Freescale ARM reference boards;
 * `meta-fsl-arm-extra <https://github.com/Freescale/meta-fsl-arm-extra/tree/daisy>`_:
   provides support for 3rd party and partner boards;
 * `meta-fsl-demos <https://github.com/Freescale/meta-fsl-demos/tree/daisy>`_:
   provides images recipes, demo recipes, and packagegroups used to easy the development with Yocto Project.
 * `Documentation <https://github.com/Freescale/Documentation>`_
   provides the source code for FSL Community BSP Release Notes (RN), User Guide (UG) and
   Frequently Asked Questions (FAQ)

Kernel Release Notes
--------------------

The FSL Community BSP include support for several kernel providers, each machine
may have a different Linux Kernel provider.

For the provider **linux-imx**, Freescale has a Release Notes for each version released,
this document has a list of known issues, new features, list of kernel arguments, and the
linux-imx kernel scope for each Freescale Reference Board.

See the respective Linux Kernel provider for your machine in section :ref:`linux-providers`

Supported Board List
--------------------
Please, see in next table the complete supported board list.


.. include:: machine-list.inc
