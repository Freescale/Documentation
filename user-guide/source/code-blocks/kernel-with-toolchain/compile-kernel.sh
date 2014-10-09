$ source /opt/poky/1.6.1/environment-setup-armv7a-vfp-neon-poky-linux-gnueabi
$ cd linux-imx
$ git checkout remotes/origin/imx_3.0.35
$ export ARCH=arm
$ export CROSS_COMPILE=$TARGET_PREFIX
$ unset LDFLAGS
$ make imx6_defconfig
$ make uImage
