Directory tree
**************

You probably have something like this under the fsl-community-bsp directory:

.. literalinclude:: code-blocks/build-result/tree-from-root-command.sh
   :language: console

Sstate-cache keeps track of each package task, so once one package taks is
finished, and there isn't any changes relevant to it, the package task will not
run again.  If a team shares the same build environment, the sstate-cache
directory can be shared as well. For configuring it go to the `Yocto Project
Reference Manual
<https://wiki.yoctoproject.org/wiki/Enable_sstate_cache#use_sstate_cache_server>`_.

The downloaded source code can be shared for any build directory. It holds every
package's source code, such as the SSH source code (and this source code can be
built for any architecture). In addition, you may want to share the download
directory with your team (one download directory for the complete team). Go to
Yocto Project Reference Manual `DL_DIR variable entry
<http://www.yoctoproject.org/docs/current/ref-manual/ref-manual.html#var-DL_DIR>`_
to find out how to share the directory between users.

The *build* directory tree
**************************

The *build* directory is used by OpenEmbedded to store information about
builds. It is perfectly normal and common to use several build directories, each
with it's own machine, distro and configuration:

.. literalinclude:: code-blocks/build-result/tree-from-build_mx6-command.sh
   :language: console

Inside the *tmp* directory you will find built images and build results. Images
are placed inside the *deploy* directory. Build statistics like initial and
final time for each package/task are under the *buildstats* directory. The
complete log for any BitBake task executed is under the *log* directory.

.. note:: Take a look at the file *log/cooker/imx6qsabresd/\*.log*. Please
          notice that * is the start time of BitBake, so every time you run
          BitBake you will have a different one.

The source code, the patches and the logs for the last BitBake execution for
each package are under the *work* directory. For example, take a look on the
files under *tmp/work/imx6qsabresd-poky-linux-gnueabi/linux-imx/3.0.35-r37.14/*,
created during the kernel tasks execution:

.. literalinclude:: code-blocks/build-result/tree-from-imx6-linux-work-command.sh
   :language: console

Go under *temp*, and you will see a lot of log.* and run.* files:

.. literalinclude:: code-blocks/build-result/ls-from-imx6-linux-temp-work-command.sh
   :language: console

For each package you will be able to see the log for the latest task, and what
was done on the latest task. For example:

* log.taskorder: shows the order each task for the kernel package was executed;
* log.do_compile.*: shows the log output for a *do_compile* task that executed
  in the program with PID of \*;
* log.do_compile: link to the latest log output from the *do_compile* task
  executed for the kernel;
* run.do_compile: link to the latest *do_compile* task command line log.

For the images generated, you will find something like this:

.. literalinclude:: code-blocks/build-result/ls-imx6qsabresd-images.sh
   :language: console

You can access any generated image. Every time you successfully run BitBake to
compile a full image it generates new images and links to it. The real images
file names end in the format **yearmothdaypid** (long number), and the symbolic
links points to the latest created images.

The *.ext3* files are the EXT3 image for the rootfs. You can copy a EXT3 image
directly to a disk partition using dd:

.. literalinclude:: code-blocks/build-result/dd-image-disk-partition.sh
   :language: console

The files with the *.sdcard* extension points to the complete system image to be
copied directly to a SD card (NOT a partition of it), and it normally contains
u-boot+uImage+rootfs:

.. literalinclude:: code-blocks/build-result/dd-image-sdcard.sh
   :language: console

The .tar.bz2 files are the tarball for the rootfs that you can extract it on
your PC. You can use it to check if the rootfs generated for your image is
correct, as it represents the file structure that will be used in your machine's
system. For a standard image generation you only need to know where the final
images are placed.

Files of interest inside the roofs are *uImage*, which is the built kernel
image, and *u-boot*, which is the Das U-Boot boot loader image.
