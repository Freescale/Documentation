.. include:: variables.inc

************
Introduction
************
This document is the release notes for the |project_name| |release|,
which is the result of a community effort to improve Freescale's SoC
support for OpenEmbedded and Yocto Project.

.. only:: draft

   .. warning::

      This document is still in **draft** form and *shouldn't be
      considered finished*.  In case you wish to contribute with
      suggestions, fixes or comments, then please get in touch
      through the `meta-freescale
      <https://lists.yoctoproject.org/listinfo/meta-freescale>`_
      mailing list.

.. only:: latex

   This document is released under Creative Commons 4.0 (CC BY-SA 4.0)

   If you want to make part of |project_name| access
   `http://freescale.github.io <http://freescale.github.io>`_ and find
   links to this document, how to contribute, and how to download both
   the source code and several pre-built images.

Defining the |project_name|
===========================
The |project_name| is a community-driven project to provide and
maintain Board Support Package (BSP) metadata layers for use in
OpenEmbedded and Yocto Project with Freescale's SoCs.

The |project_name| follows Yocto Project's *release schedule* and
*branch naming* (since release 1.3, denzil).

See the `Yocto Project Release <https://wiki.yoctoproject.org/wiki/Releases>`_
for details on the Yocto Project.

Motivation
----------
The |project_name| started with the goal of easing the use of
OpenEmbeedded and Yocto Project with Freescale's SoCs
and providing an example of how to assemble an easy-to-use
platform as the basis for future products.

The |project_name| provides:

 * common environment configuration;
 * multiple download layers with the use of `repo <https://github.com/Freescale/fsl-community-bsp-platform>`_;
 * common `location <https://lists.yoctoproject.org/listinfo/meta-freescale>`_
   for discussing Freescale SoCs, kernels, bootloaders, user space
   packages, (BSP in general), bugs, how-tos, and so on

What the |project_name| is not
------------------------------
The |project_name| does not have a paid support team. The members of this
community have full-time jobs and work on the project in their spare time. Most of them
are working with Freescale SoCs in their full-time job, so it means some of them can
provide paid support if requested.

The provided source code is not intended to be a product in itself. It is a
reference platform for people to build products with. Because of this,
plan to have a development and test cycle for your product if you decide to base it on
the |project_name|.

The project is community-driven work, and it is NOT an official Freescale support channel.

What you can expect
-------------------
* You can expect help when you post a question, but please be patient.
  Wait for at least two days for a response. Most of the time, people
  do reply when they know an answer or have advice to offer. If you don't
  receive a reply, then it may be due to no one in the community having an adequate
  response.
* The stable branch is supported for six months after the release date (following
  the Yocto Project's release schedule);
* The upstreaming takes place as quickly as possible and any needed adjustment is
  going to be made accordingly.

What the community expects from you
-----------------------------------
The community does expect that you contribute back by:

 * replying when you know the answer to a question in the mailing list;
 * reviewing the patches sent to mailing list;
 * testing new patches that affect you directly or indirectly;
 * reporting bugs you may find;
 * upstreaming bug fixes;
 * upstreaming features that may be good for the community.

Upstreaming
===========
The |project_name| provides test images and demos in addition to the base BSP for Freescale
reference boards and third-party boards. In addition to the BSP,
a Linux-based operating system typically requires several other packages, such as ssh client/server,
window managers, applications, and so on. These packages are not part of the BSP.
In other words, the |project_name| is used with applications, tools
and metadata from other projects, such as OpenEmbedded and Poky.

The |project_name| always offers a stable version and a development version.
You may face errors that are not caused by |project_name|'s layers but
instead by OpenEmbedded's or Poky's metadata.
In this case, the error must be fixed in its layer.

The following image shows the upstream levels:

.. blockdiag:: upstream1.diag
   :align: center
   :scale: 60%

Main branch names
-----------------

* master-next: this branch is used to keep the patches to be built by the autobuilder
  for the very first test build. Do not expect to have a clear merging schedule,
  or to have a stable project when working with the master-next branch;
* master: this is the branch where development takes place. Any new feature or
  bug fix must be merged here first. This is the development of the next stable branch;
* |version|: the latest stable branch. This branch only accepts bug fixes, and
  is supported for 6 months after the release date.

There are other branches available, and they are the previous stable branches. They are kept online
for users' convenience, and you should not expect backports or bug fixes.

Upstream cycle
--------------
In addition to the normal Yocto Project upstream process, there is also a BSP upstream cycle.

The BSP upstream cycle starts just after a |freescale_release_name|
is published in `git.freescale.com <http://git.freescale.com/git/cgit.cgi/imx/fsl-arm-yocto-bsp.git/>`_.
The patches to adapt the recipes from **meta-fsl-bsp-release** are sent out for review
to the **meta-freescale** mailing list and are merged in the **meta-fsl-arm** and
**meta-fsl-demos** layers or upstreamed to Yocto Project accordingly.

A more detailed step-by-step process is shown below:

 1. New |freescale_release_name| is published;
 2. The patches are sent to **meta-freescale**;
 3. After the review process, the patches are merged in the proper layer's *master-next* branch;
 4. Source code is built by the autobuilder;
 5. After one week in *master-next*, it is merged in *master*;
 6. Freescale internally bases the next |freescale_release_name| from the community source code;
 7. Back to step 1.

The result is that Freescale uses the |project_name| source code with its bug fixes, improvements,
and any new features to create the *next* |freescale_release_name|.

Freescale uses the latest stable branch from Yocto Project to base the *next*
|freescale_release_name|. When this release is published, it is rebased and
reworked to be merged in the current development branch.

The differences between |project_name| and |freescale_release_name|
===================================================================

The goal for each project is different. See below for the main points
of divergence.

|freescale_release_name|
------------------------
The |freescale_release_name| is intended to provide a static base for Freescale
to test and validate the BSP modules with Freescale evaluation boards, and it is
developed internally by Freescale. The set of supported boards vary from release
to release and is listed in the |freescale_release_name| notes for the
specific version. The release points to a static revision of every included
layer. Therefore, the release does not receive updates and bug fixes.

|project_name|
--------------
The |project_name| is a reference system that can be used as a base for products
and is an open project that accepts contributions from the community.
It supports a wide range of boards which range from Freescale evaluation boards
(**meta-fsl-arm** layer) to third-party boards (**meta-fsl-arm-extra**).
The release is a "*moving target*”, so there are updates on top of the released
source code, such as the addition of new features and bug fixes.

.. tabularcolumns:: p{5cm} | p{5cm} | p{5cm}
.. table:: Comparative between |freescale_release_name| and |project_name|

  .. include:: fslxcmt.inc

