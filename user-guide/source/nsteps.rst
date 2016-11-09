Build and boot in *N*-steps
===========================

1. Check `required host packages`_ for your Linux Distribution

2. Download the `repo`_ tool::

    $ mkdir -p ~/bin
    $ PATH=~/bin:${PATH}
    $ curl http://commondatastorage.googleapis.com/git-repo-downloads/repo > ~/bin/repo 
    $ chmod a+x ~/bin/repo

3. Download the Yocto Metadata::

    $ mkdir fsl-community-bsp # You can name it anything you want
    $ cd fsl-community-bsp
    fsl-community-bsp $ repo init \
                            -u https://github.com/Freescale/fsl-community-bsp-platform \
                            -b morty
    fsl-community-bsp $ repo sync 

4. Select your machine (:ref:`machines`) and prepare the environment for bitbake::

    fsl-community-bsp $ MACHINE=<selected machine> DISTRO=<selected distro> source setup-environment build
    build $

5. Select your image (:ref:`images`) and build::

    build $ bitbake-layers show-recipes "*image*" | grep ':'  # To list all possible images
    build $ bitbake <selected image>	# Bake! The first time can take several hours

6. Flash your SD card:

    a) With a pre-formed sdcard image::

        # Insert your SD Card
        # Type '$ dmesg | tail' to see the device node being used, e.g /dev/sdb
        # In case the SD to be flashed has already some partitions, the host system may have 
        # mounted these, so unmount them, e.g. '$ sudo umount /dev/sdb?'.
        build $ ls -la 'tmp/deploy/images/<selected machine>/*.sdcard'
        
        # Flash the soft link .sdcard image
        build $ sudo dd \
                  if=tmp/deploy/images/<selected machine>/<selected image>-<selected machine>.sdcard \
                  of=/dev/sdX \
                  bs=1M \
                  conv=fsync

    b) With a pre-formed root filesystem archive, kernel and device tree binary image::

        # Insert your SD Card
        # Check your card is mounted ls /media/<user name>/<mounted filesystem name>
        build $ ls -la 'tmp/deploy/images/<selected machine>/*.tar.gz'
        
        # Inflate the the soft link .tar.gz onto the cards filesystem
        build $ sudo tar -zxvf \
                  tmp/deploy/images/<selected machine>/<selected image>-<selected machine>.tar.gz \
                  -C /media/<user name>/<mounted filesystem name>
        
        # If you will use U-Boot from the SD Card it will need to be placed on 
        # a small partition at the start of the card.  If you will use U-Boot 
        # from flash or elsewhere you can have a single exfs2 parition on the 
        # whole card.  
        
        # Copy over the kernel
        build $ ls -la 'tmp/deploy/images/<selected machine>/uImage*.bin'
        build $ sudo cp \
                  'tmp/deploy/images/<selected machine>/uImage-<selected machine>.bin' \
                  /media/<user name>/<mounted filesystem name>/boot/
        
        # Copy over the device tree binary
        build $ ls -la 'tmp/deploy/images/<selected machine>/uImage*.dtb'
        build $ sudo cp \
                  'tmp/deploy/images/<selected machine>/uImage-<selected machine>.dtb' \
                  /media/<user name>/<mounted filesystem name>/boot/

7. Place your SD Card in the correct board's slot and boot!

Found errors? Subscribe and report it to `meta-freescale list`_

.. links
.. _required host packages: https://www.yoctoproject.org/docs/current/yocto-project-qs/yocto-project-qs.html#packages
.. _repo: http://source.android.com/source/downloading.html
.. _meta-freescale list: https://lists.yoctoproject.org/listinfo/meta-freescale
