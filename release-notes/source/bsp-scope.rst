.. include:: variables.inc

Scope
=========

|project_name| Scope
-----------------------
The scope of the |project_name| includes the meta layers:

 * `meta-fsl-arm <http://git.yoctoproject.org/cgit/cgit.cgi/meta-fsl-arm/?h=dizzy>`_:
   provides the base support and Freescale ARM reference boards;
 * `meta-fsl-arm-extra <https://github.com/Freescale/meta-fsl-arm-extra/tree/dizzy>`_:
   provides support for 3rd party and partner boards;
 * `meta-fsl-demos <https://github.com/Freescale/meta-fsl-demos/tree/dizzy>`_:
   provides images recipes, demo recipes, and packagegroups used to easy the development with Yocto Project.
 * `Documentation <https://github.com/Freescale/Documentation/tree/dizzy>`_
   provides the source code for |project_name| Release Notes (RN), User Guide (UG) and
   Frequently Asked Questions (FAQ)

Kernel Release Notes
--------------------
The |project_name| includes support for several kernel providers. Each machine
may have a different Linux Kernel provider.

For the **linux-imx** provider, Freescale has a release notes document for each
version released. This document has a list of known issues, new features, list
of kernel arguments, and the linux-imx kernel scope for each Freescale Reference
Board. This document is present into the Document Bundle provided by Freescale.

See the respective Linux Kernel provider for your machine in section :ref:`linux-providers`

Different Product SoC Families
------------------------------
Currently, the |project_name| includes the following Product SoC Families:

 * **i.MX Application Processors (imx)**: Regarding the `i.MX Freescale Page
   <http://www.freescale.com/webapp/sps/site/homepage.jsp?code=IMX_HOME>`_:
   *i.MX applications processors are multicore ARM®-based solutions for multimedia and display
   applications with scalability, high performance, and low power capabilities.*

 * **Vybrid Controller Solutions based on ARM® Cores (vybrid)**: Regarding the
   `Vybrid Freescale Page <http://www.freescale.com/webapp/sps/site/homepage.jsp?code=VYBRID>`_:
   *Vybrid controller solutions are built on an asymmetrical-multiprocessing
   architecture using ARM® cores as the anchor for the platform, and are ideal
   for many industrial applications.*

 * **Layerscape Architecture (ls)**: Regarding the `Layerscape Freescale Page
   <http://www.freescale.com/webapp/sps/site/overview.jsp?code=QORIQ_LAYERSCAPE>`_:
   *delivers unprecedented efficiency and scale for the smarter, more capable
   networks of tomorrow.*

Freescale groups a set of SoCs which target different markets in product
families. Those are grouped according to their SoC features and internal hardware
capabilities.

The Yocto Project's tools have the required capabilities to differentiate the
architectures and BSP components for the different SoC families. In this perspective,
the |project_name| can support a wide range of architectures and product lines
which go across several markets.

For the |project_name|, the different SoCs, from all product lines manufactured by
Freescale, can be seen as different machines, thus easing the use of same architecture
across different markets.

.. _supported-boards:

Supported Board List
--------------------
Please, see the next table for the complete supported board list.

.. tabularcolumns:: |c|p{6cm}|c|c|
.. table:: Supported machines in |project_name|

   .. include:: machine-list.inc
