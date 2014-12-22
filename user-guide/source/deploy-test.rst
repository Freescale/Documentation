Deploy and test
===============

Images - the result of a bitbake
********************************

OK, so now we have just built an image with BitBake. Here is an example of what was generated:

.. literalinclude:: code-blocks/deploy-test/ls-deploy-images.sh
   :language: console

Get used with the generated images. Understand that some files are a symbolic link to the real image. The symbolic links will always point to latest image.

SD card image
*************

Take a look on how the SD card image is generated here: `meta-fsl-arm layer<http://git.yoctoproject.org/cgit/cgit.cgi/meta-fsl-arm/tree/classes/image_types_fsl.bbclass?h=daisy>`_, which contains the Freescale ARM hardware support metadata. The disk layout used is as follows:

====================== ================================== ========================================
Start                  End                                Notes
====================== ================================== ========================================
0                      IMAGE_ROOTFS_ALIGNMENT             Reserved to bootloader (not partitioned)
IMAGE_ROOTFS_ALIGNMENT BOOT_SPACE                         Kernel and boot data
BOOT_SPACE             SDIMG_SIZE + IMAGE_OVERHEAD_FACTOR Rootfs location
====================== ================================== ========================================

Please refer to the original file to get in-depth information about the disk layout.

It's basically some initial space for u-boot. One partition for uImage. One partition for rootfs. The total SD card size will be calculate for every image, if you want to add more empty space inside generated SD card, use IMAGE_OVERHEAD_FACTOR.

Deploy
======

It's pretty easy to deploy an image to a SD card. Just use the *dd* program with the SD card device file:

.. warning:: **Be careful!** It is really easy to destroy your host system  filesystem if you use the wrong device file! Always check what is the correct SD card device file by running *dmesg* after pluggin it in.

.. literalinclude:: code-blocks/deploy-test/dd-sd-card.sh
   :language: console

You can also deploy the EXT3 rootfs to a partition:

.. literalinclude:: code-blocks/deploy-test/dd-sd-card-partition.sh
   :language: console

Or deploy only the tar.bz rootfs to a previously mounted partition:

.. literalinclude:: code-blocks/deploy-test/copy-sd-card-mounted-partition.sh
   :language: console

You can also deploy (just copy, really) only the kernel to a partition:

.. literalinclude:: code-blocks/deploy-test/copy-kernel.sh
   :language: console

And to setup only u-boot:

.. literalinclude:: code-blocks/deploy-test/dd-uboot.sh
   :language: console

.. note:: If you are using HDMI please modify the u-boot environment arguments so it can boot correctly:

          .. literalinclude:: code-blocks/deploy-test/uboot-hdmi-settings.sh
             :language: console

As you can see, there are several options on how you can prepare SD cards with your built images. Of course you can create your own way to setup a working card, but always double check the u-boot bootenv variable, as it is dependent on how the disk devices are loaded or setup by you.

After that, just plug your SD card into the board, and turn it own or reset it to boot it. To login just use *root* as the username. There is no password set by default, so you should have access to the system console.
