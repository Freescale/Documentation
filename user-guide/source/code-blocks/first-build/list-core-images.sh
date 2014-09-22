$ ls ../sources/poky/meta*/recipes*/images/*.bb | \
  xargs -n1 -i basename {} .bb | sort
build-appliance-image_8.0
core-image-base
core-image-clutter
core-image-directfb
core-image-full-cmdline
core-image-lsb
core-image-lsb-dev
core-image-lsb-sdk
core-image-minimal
core-image-minimal-dev
core-image-minimal-initramfs
core-image-minimal-mtdutils
core-image-multilib-example
core-image-rt
core-image-rt-sdk
core-image-sato
core-image-sato-dev
core-image-sato-sdk
core-image-testmaster
core-image-testmaster-initramfs
core-image-weston
core-image-x11
qt4e-demo-image
