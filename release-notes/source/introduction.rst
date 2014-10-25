.. include:: variables.inc

************
Introduction
************
This document has the release notes of the |project_name| |release|
which is a community effort to improve Freescale's SoCs support in the
OpenEmbedded and Yocto Project projects.

What the |project_name| is
==========================
The |project_name| is a community-driven project to provide and
maintain Board Support Package (BSP) metadata layers for use in the
OpenEmbedded and Yocto Project projects with Freescale's SoCs.

The |project_name| follows the same Yocto Project's *release schedule* and the
*branch naming*, since release 1.3 (denzil).

See the `Yocto Project Release <https://wiki.yoctoproject.org/wiki/Releases>`_
for details on the Yocto Project.

Motivation
----------
The |project_name| started with the goal of making the use of
OpenEmbeedded and Yocto Project projects, with Freescale's SoCs,
easier and providing an example of how to assemble an easy-to-use
platform to base products on.

The project provides:

 * common environment configuration;
 * download several layers with `repo <https://github.com/Freescale/fsl-community-bsp-platform>`_;
 * common `place <https://lists.yoctoproject.org/listinfo/meta-freescale>`_;
   for discussion regarding Freescale SoCs (kernels, bootloaders, user space
   packages (BSP in general), bugs, how-tos, and so on.

What the |project_name| is not
------------------------------
The |project_name| does not have a professional support team. The members of this
community have full-time jobs and work on the project on spare time. Most of them
are working with Freescale SoCs in their full-time job, it means most of them can
provide a professional support if requested.

The provided source code is not supposed to have production quality. It is a
reference BSP and platform for people to build products on top of it. Because of that,
expect to have an adjustment cycle for your product when you decide to use it as
a reference for your next product.

The project is a community-driven work and it is NOT an official Freescale support channel.

What you can expect
-------------------
* You can expect help when you post a question, but please, be patient. Wait for at
  least 2 days until thinking nobody cares about your problem. Most of time people
  do reply when they know the answer, or try to provide advice. In case you are 
  ignored, probably nobody knows the answer;
* The stable branch is supported for six months after the release date (following
  the Yocto Project's release schedule);
* The upstreaming takes place as fast as possible and any needed adjustment is
  going to be made accordingly.

What the community expects from you
-----------------------------------
The community does expect that you contribute back by:

 * replying when you know the answer for a question in the mailing list;
 * reviewing the patches sent to mailing list;
 * testing new patches that affect you directly or indirectly;
 * reporting bugs you may find;
 * upstreaming bug fixes;
 * upstreaming features that may be good for community.

Upstream
========
The |project_name| provides a BSP, test images, and demos for Freescale
reference boards and 3rd party boards based on Freescale's SoCs. Besides the BSP,
a Linux-based operating system has several other packages such as ssh client/server,
window managers, applications, and so on. These packages are not part of the BSP,
in other words, when using |project_name| we are also using applications, tools
and metadata from other projects such as OpenEmbedded and Poky.

The |project_name| always has a stable and a development version. You may face
errors that are not caused by |project_name|'s layers, but by the
OpenEmbedded's or Poky's metadata. In this case, the error must be fixed
in the layer it belongs.

The following image shows the upstream levels:

.. blockdiag:: upstream1.diag
   :align: center
   :scale: 60%

Main branch names
-----------------

* master-next: this branch is used to keep the patches to be built by the autobuilder
  for the very first built test. Do not expect to have a clear merging schedule, 
  or to have a stable project;
* master: this is the branch where development takes place. Any new feature or
  bug fix must be merged here first. This is the development of the next stable branch;
* |version|: the latest stable branch. This branch only accepts bug fixes, and
  is supported for 6 months after the release date.

There are other branches which are the previous stable branches. They are kept online
for users' convenience, and you cannot expect backports or bug fixes.

Upstreaming cycle
-----------------
Additionally to the normal upstreaming process when working with any Yocto Project's
layer, we have the BSP upstreaming cycle.

The BSP upstreaming cycle starts just after a |freescale_release_name|
is published in `git.freescale.com <http://git.freescale.com/git/cgit.cgi/imx/fsl-arm-yocto-bsp.git/>`_.
The patches to adapt the recipes from **meta-fsl-bsp-release** are sent for review
and comments to the **meta-freescale** mailing list and are merged in the **meta-fsl-arm**,
**meta-fsl-demos** layers or upstreamed to Yocto Project accordingly.

A more detailed step-by-step is shown below:

 1. New |freescale_release_name| is published;
 2. The patches are sent to **meta-freescale**;
 3. After the review process, the patches are merged in the proper layer's *master-next* branch;
 4. Source code is built by the autobuilder;
 5. After one week in *master-next*, it is merged in *master*;
 6. Freescale internally bases the next |freescale_release_name| in community source code;
 7. Back to step 1.

It means Freescale uses the |project_name| source code with its bug fixes, improvements,
and any new features to create the *next* |freescale_release_name|.

Freescale uses the latest stable branch from Yocto Project to base the *next*
|freescale_release_name|. When this release is published, it is rebased and
reworked to be merged in the current development branch.

The differences between |project_name| and |freescale_release_name|
===================================================================

The goal of both projects are different. See below the main points
of divergence.

|freescale_release_name|
------------------------
The |freescale_release_name| is intended to provide a static base for Freescale
to test and validate the BSP modules in the Freescale evaluation boards and it is
developed internally by Freescale. The set of supported boards vary from release
to release and is listed in the |freescale_release_name|'s release notes for the
respective version.
The release points to a static revision of every included layer so, after release
it does not receive updates and bug fixes.

|project_name|
--------------
The |project_name| is a reference system that can be used as a base for products
and is an open project that accepts contributions from the community.
It supports a wide range of boards which goes from Freescale evaluation boards
(**meta-fsl-arm** layer) to 3rd party boards (**meta-fsl-arm-extra**).
The release is a "*moving target*”, so there are updates on top of the released
source code, such as addition of new features and of bug fixes.

