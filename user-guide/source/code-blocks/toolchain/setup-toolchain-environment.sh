$ cd /opt/poky/1.6.1/
$ cat environment-setup-cortexa9hf-vfp-neon-poky-linux-gnueabi
export SDKTARGETSYSROOT=/opt/poky/1.6.1/sysroots/cortexa9hf-vfp-neon-poky-linux-gnueabi
export PATH=/opt/poky/1.6.1/sysroots/x86_64-pokysdk-linux/usr/bin:/opt/poky/1.6.1/sysroots/x86_64-pokysdk-linux/usr/bin/arm-poky-linux-gnueabi:$PATH
export PKG_CONFIG_SYSROOT_DIR=$SDKTARGETSYSROOT
export PKG_CONFIG_PATH=$SDKTARGETSYSROOT/usr/lib/pkgconfig
export CONFIG_SITE=/opt/poky/1.6.1/site-config-cortexa9hf-vfp-neon-poky-linux-gnueabi
export OECORE_NATIVE_SYSROOT="/opt/poky/1.6.1/sysroots/x86_64-pokysdk-linux"
export OECORE_TARGET_SYSROOT="$SDKTARGETSYSROOT"
export OECORE_ACLOCAL_OPTS="-I /opt/poky/1.6.1/sysroots/x86_64-pokysdk-linux/usr/share/aclocal"
export PYTHONHOME=/opt/poky/1.6.1/sysroots/x86_64-pokysdk-linux/usr
export CC="arm-poky-linux-gnueabi-gcc  -march=armv7-a -mthumb-interwork -mfloat-abi=hard -mfpu=neon -mtune=cortex-a9 --sysroot=$SDKTARGETSYSROOT"
export CXX="arm-poky-linux-gnueabi-g++  -march=armv7-a -mthumb-interwork -mfloat-abi=hard -mfpu=neon -mtune=cortex-a9 --sysroot=$SDKTARGETSYSROOT"
export CPP="arm-poky-linux-gnueabi-gcc -E  -march=armv7-a -mthumb-interwork -mfloat-abi=hard -mfpu=neon -mtune=cortex-a9 --sysroot=$SDKTARGETSYSROOT"
export AS="arm-poky-linux-gnueabi-as "
export LD="arm-poky-linux-gnueabi-ld  --sysroot=$SDKTARGETSYSROOT"
export GDB=arm-poky-linux-gnueabi-gdb
export STRIP=arm-poky-linux-gnueabi-strip
export RANLIB=arm-poky-linux-gnueabi-ranlib
export OBJCOPY=arm-poky-linux-gnueabi-objcopy
export OBJDUMP=arm-poky-linux-gnueabi-objdump
export AR=arm-poky-linux-gnueabi-ar
export NM=arm-poky-linux-gnueabi-nm
export M4=m4
export TARGET_PREFIX=arm-poky-linux-gnueabi-
export CONFIGURE_FLAGS="--target=arm-poky-linux-gnueabi --host=arm-poky-linux-gnueabi --build=x86_64-linux --with-libtool-sysroot=$SDKTARGETSYSROOT"
export CFLAGS=" -O2 -pipe -g -feliminate-unused-debug-types"
export CXXFLAGS=" -O2 -pipe -g -feliminate-unused-debug-types"
export LDFLAGS="-Wl,-O1 -Wl,--hash-style=gnu -Wl,--as-needed"
export CPPFLAGS=""
export OECORE_DISTRO_VERSION="1.6.1"
export OECORE_SDK_VERSION="1.6.1"
export ARCH=arm
export CROSS_COMPILE=arm-poky-linux-gnueabi-
$ . environment-setup-cortexa9hf-vfp-neon-poky-linux-gnueabi
