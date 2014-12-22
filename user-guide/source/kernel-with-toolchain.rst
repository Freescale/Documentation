Build kernel manually using a toolchain
=======================================

After the meta-toolchain build is finished, the install script it will be available at *tmp/deploy/sdk*. Copy to the host machine and install it:

.. literalinclude:: code-blocks/kernel-with-toolchain/install-toolchain.sh
   :language: console

To start using it you must set up the environment to use it's binaries instead of the ones from the host machine. You can do that by using your shell command to load a script, similarly on how you did at the start of this user guide:

.. literalinclude:: code-blocks/kernel-with-toolchain/setup-toolchain-environment.sh
   :language: console

Building a Hello World program with the toolchain
*************************************************

With that done let's try to build a simple Hello World program. Write it and then try to compile it by directly calling the compiler from the toolchain:

.. literalinclude:: code-blocks/kernel-with-toolchain/compile-hello-world.sh
   :language: console

Obviously, the compiled binary will not run on your host system since it was compiled to a different architecture. But you can check it with the *file* program, as the example shows, to confirm it was indeed compiled to the correct architecture.

Bulding the Kernel with the toolchain
*************************************

Compiling a hello world program is easy, let's try something a little more complex. To build the kernel you need to define a few environment variables yourself that are not done sone while activating the toolchain. After that just compile the kernel as you would do for the host machine:

.. literalinclude:: code-blocks/kernel-with-toolchain/compile-kernel.sh
   :language: console

Make sure to have *mkimage* available on *bin* patch (if using *mkimage* from u-boot export its patch). Or you can download your distribution package. Here's how you do it for Ubuntu:

.. literalinclude:: code-blocks/kernel-with-toolchain/apt-get-install-uboot-mkimage.sh
   :language: console

During the kernel compilation you may find the following error:

.. literalinclude:: code-blocks/kernel-with-toolchain/compile-kernel-loadaddr-error.sh
   :language: console

This is regarding a missing LOADADDR variable for *mkimage* to use to generate uImage with the right offset to be placed in the right LOADADDR.

This address value is dependent on your board hardware. Also, it can be different depending on the imx6 variations. You need to find the correct one for your board to define it.

If the machine you are using is supported in the Yocto Project or this BSP you can probably find the value related with your board in the file *conf/machine/include/imx-base.inc* or online on the meta-fsl-arm, the layer containing Freescale ARM hardware support metadata, which you can find it `here <http://git.yoctoproject.org/cgit/cgit.cgi/meta-fsl-arm/tree/conf/machine/include/imx-base.inc>`_. It is the same value used in variable UBOOT_ENTRYPOINT.

For example as of this writing for the Freescale SABRE-SD board looking in *conf/machine/include/imx-base.inc*

.. literalinclude:: code-blocks/kernel-with-toolchain/uboot-entrypoint-imx6.sh
   :language: console

Then the build command would be:

.. literalinclude:: code-blocks/kernel-with-toolchain/make-uimage-with-loadaddr.sh
   :language: console

As a quick reference table, here are the 3 most wanted make commands already with the LOADADDR variable set:

* **imx28evk**:

  .. literalinclude:: code-blocks/kernel-with-toolchain/make-loadaddr-imx28evk.sh
     :language: console

* **imx53qsb**:

  .. literalinclude:: code-blocks/kernel-with-toolchain/make-loadaddr-imx53qsb.sh
     :language: console

* **imx6qsabresd**:

  .. literalinclude:: code-blocks/kernel-with-toolchain/make-loadaddr-imx6qsabresd.sh
     :language: console
