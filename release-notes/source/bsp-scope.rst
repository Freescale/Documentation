.. include:: variables.inc

|project_name| Scope
***********************
The scope of the |project_name| includes the meta layers:

 * `meta-fsl-arm <http://git.yoctoproject.org/cgit/cgit.cgi/meta-fsl-arm/?h=dizzy>`_:
   provides the base support and Freescale ARM reference boards;
 * `meta-fsl-arm-extra <https://github.com/Freescale/meta-fsl-arm-extra/tree/dizzy>`_:
   provides support for 3rd party and partner boards;
 * `meta-fsl-demos <https://github.com/Freescale/meta-fsl-demos/tree/dizzy>`_:
   provides images recipes, demo recipes, and packagegroups used to easy the
   development with Yocto Project.
 * `Documentation <https://github.com/Freescale/Documentation/tree/dizzy>`_:
   provides the source code for |project_name| Release Notes (RN), User Guide
   (UG) and Frequently Asked Questions (FAQ)

.. _kernel_release_notes:

Kernel Release Notes
====================
The |project_name| includes support for several kernel providers. Each machine
may have a different Linux Kernel provider.

The |project_name| is not responsible for the content of those kernels.
Although we *as community* should feel empowered to submit bug fixes and new
features for those projects.

See the respective Linux Kernel provider for your machine in section
:ref:`linux-providers`.

Different Product SoC Families
==============================
Currently, the |project_name| includes the following Product SoC Families:

 * **i.MX Application Processors (imx)**: Regarding the `i.MX Freescale Page
   <http://www.freescale.com/webapp/sps/site/homepage.jsp?code=IMX_HOME>`_:
   *i.MX applications processors are multicore ARM®-based solutions for
   multimedia and display applications with scalability, high performance, and
   low power capabilities.*

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
families. Those are grouped according to their SoC features and internal
hardware capabilities.

The Yocto Project's tools have the required capabilities to differentiate the
architectures and BSP components for the different SoC families. In this
perspective, the |project_name| can support a wide range of architectures and
product lines which go across several markets.

For the |project_name|, the different SoCs, from all product lines manufactured
by Freescale, can be seen as different machines, thus easing the use of same
architecture across different markets.

.. _supported-boards:

Supported Board List
====================
Please, see the next table for the complete supported board list.

.. tabularcolumns:: c | p{5cm} | c | c
.. table:: Supported machines in |project_name|

   .. include:: machine-list.inc

Machine Maintainers
-------------------

Since |project_name| Release 1.6 (Daisy), the maintainer field in machine
configuration files of **meta-fsl-arm** and **meta-fsl-arm-extra** is mandatory
for any new board to be added.

So now on, every new board must have someone assigned as maintainer.
This ensures, in long term, all boards with a maintainer assigned.
Current orphan boards are not going to be removed unless it causes maintenance
problem and the fix is not straightforward.

The maintainer duties:
 * The one with casting vote when a deadlock is faced.
 * Responsible to keep that machine working (that means, booting and with some
   stability) Keep kernel, u-boot updated/tested/working.
 * Keep release notes updated
 * Keep test cycle updated
 * Keep the most usual images building and booting

When a build error is detected, the maintainer will "fix" it. For those
maintainers with kernel control (meta-fsl-arm-extra), it is expected that they
properly fix the kernel issue (when it's a kernel issue). However, anything out
of community control should be worked around anyway.

Machines with maintainers
^^^^^^^^^^^^^^^^^^^^^^^^^

.. tabularcolumns:: l | p{9cm}
.. table:: Machines with maintainers

   .. include:: machines-with-maintainers.inc

Machines without a maintainer
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. tabularcolumns:: l | p{9cm}
.. table:: Machines without a maintainer

   .. include:: machines-without-maintainers.inc
