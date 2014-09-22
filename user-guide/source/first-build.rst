Compiling your first build
==========================

Synchronize your source code
****************************

Make sure that your copy of the source code is up-to-date. So, run this command
to synchronize it:

.. literalinclude:: code-blocks/first-build/repo-sync.sh
   :language: console

Create your local branch
************************

Do your work on a different branch, to help organizing your work. You can do
that by running this repo command:

.. literalinclude:: code-blocks/first-build/repo-create-branch.sh
   :language: console

*Why should I create a local branch?*

If you change *any* source code (for example, choosing another preferred kernel)
and want to sync again, or use master instead of a stable branch, you will be
able to rebase or sync your source code, even with your changes. This will also
make easier in case you find a bug, fix it, and want to send a patch back to the
community.

Choose your board
*****************

To setup your build environment run the following command on the project root:

.. literalinclude:: code-blocks/first-build/setup-environment.sh
   :language: console

After the command finishes you will be in the newly created build directory. All
build actions will happen inside using this directory as starting point.

The default board for daisy is imx6qsabresd, you can choose QSB or imx28 if you
prefer:

.. literalinclude:: code-blocks/first-build/edit-local-conf.sh
   :language: console

Your default local.conf file will look like:

.. literalinclude:: code-blocks/first-build/local-conf-example.conf

Change the MACHINE variable to your board name. In order to figure out what is
the machine name you can list the machines directory. Here is the command to do
so for the Freescale boards:

.. literalinclude:: code-blocks/first-build/list-freescale-machines.sh
   :language: console

For non-Freescale boards use:

.. literalinclude:: code-blocks/first-build/list-non-freescale-machines.sh
   :language: console

And to print all the boards just use both directories:

.. literalinclude:: code-blocks/first-build/list-all-machines.sh
   :language: console

Please be sure to use the exact name of the board as the value of the variable,
as the tools will complain if a different name is used.

Also, look at the meta-fsl-arm:daisy release notes: Freescale Community BSP Release Notes
1.6 documentation for more information about new boards added on this release.

Starting your first build
*************************

The biggest image from *meta-fsl-demos* is **fsl-image-gui**. It has X11,
gstreamer, fsl codec for gstreamer, unit-test, gpu, one gpu sample (with source
code) for imx53 and QT 4.8. But it takes a lot of time to build (if you are luck
and have a powerful machine, it will take only few hours). If you have already
built it once, it will take about 3 seconds to decide nothing has been changed
and about 15 minutes to generate the image file (it's a 750MB rootfs, so it does
take some time to create such big file).

There are several other images you can create. In order to see which ones are
present on the Poky Platfom Builder (the core tool of the Yocto Project), please
run:

.. literalinclude:: code-blocks/first-build/list-core-images.sh
   :language: console

Also, if you added other layers there may be other images available to
you. Check their documentation to see the available images provided by them.

For your first image, start with **core-image-base**. It does not have X11,
gstreamer or QT, but it only take 30 minutes to build at first time. And it
should work just fine for any board.

Following the complete sequence of commands, make sure you're on the right
build directory (named "build", if you followed this tutorial to the letter),
then run:

.. literalinclude:: code-blocks/first-build/bitbake-core-image-base.sh
   :language: console

And then the build process will start.

.. note:: as of 2014-02-24, the required disk space for building a
          *core-image-image* is about ~18GB.

Also, to generate fsl-image-gui, which is the biggest image, with complete
support to a GUI and several other features, execute this:

.. literalinclude:: code-blocks/first-build/bitbake-fsl-image-gui.sh
   :language: console

.. note:: as of 2014-02-24, the required disk space for building a fsl-image-gui
          is ~44GB. So it will take a while until it finishes, even on recent
          build machines.
