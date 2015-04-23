#! /bin/bash

### This script generates documentation based on metadata extracted
### out of BitBake's cache data.
###
### It basically sources setup-environment and run
### extract-bitbake-metadata.py for each given machine (if the
### MACHINES environment variable is set, uses it, otherwise find
### machine files in yocto_dir). extract-bitbake-metadata.py collects
### data from the BitBake cache for each machine and writes a file
### (doc-data.pckl, in Python's pickle format) which is eventually
### used by bitbake-metadata2doc.py to transform all the collected
### data into documentation in rst format.

# Check if running from the scripts dir
if [ "`basename $PWD`" != "scripts" ]; then
    echo "This script is expected to be run from the scripts directory" >&2
    exit 1
fi

usage() {
    local exit_code
    local output
    [ -n $1 ] && exit_code=$1
    if [ -n "$exit_code" ] && [ "$exit_code" != "0" ]; then
        output=2
    else
        output=1
    fi

    echo "Usage: `basename $0` <yocto directory> <gitdm directory> <start commit> <end commit>" >&$output
    echo >&$output
    echo "For detail on how to use it, see ../release-notes/README" >&$output
    [ -n "$exit_code" ] && exit $exit_code
}


[ -z "$4" ] && usage 1

if [ "$1" = "-h" ] || [ "$1" = "-help" ] || [ "$1" = "--help" ]; then
    usage 0
fi

yocto_dir="$1"
gitdm_dir="$2"
start_commit="$3"
end_commit="$4"
anchor="`pwd`"
fsl_layers="meta-fsl-arm meta-fsl-arm-extra meta-fsl-demos"

machines=
if [ -n "$MACHINES" ]; then
    machines="$MACHINES"
else
    machines=`./output-machine-list $yocto_dir`
fi

images=
for fsl_layer in $fsl_layers; do
    images="$images \
            `find $yocto_dir/sources/$fsl_layer \
                  -name '*image*.bb' \
                  -exec basename '{}' .bb \;`"
done

packagegroups=
for fsl_layer in $fsl_layers; do
    packagegroups="$packagegroups \
                   `find $yocto_dir/sources/$fsl_layer \
                         -name '*packagegroup*.bb' \
                         -exec basename '{}' .bb \;`"
done

marshalled_data_file=doc-data.pckl

rm -f $anchor/$marshalled_data_file

build_dir=`mktemp -d --tmpdir=$yocto_dir`

for machine in $machines; do
    cd $yocto_dir
    echo "Using $build_dir as build directory"
    MACHINE=$machine . ./setup-environment `basename $build_dir`

    MACHINE=$machine python $anchor/extract-bitbake-metadata.py \
        $anchor/$marshalled_data_file \
        amd-gpu-bin-mx51 \
        amd-gpu-x11-bin-mx51 \
        barebox \
        directfb \
        directfb-examples \
        libdrm \
        firmware-imx \
        fsl-alsa-plugins \
        gpu-viv-bin-mx6q \
        gpu-viv-g2d \
        gst-fsl-plugin \
        gstreamer \
        gstreamer1.0 \
        gstreamer1.0-plugins-imx \
        imx-kobs \
        imx-lib \
        imx-test \
        imx-uuc \
        imx-vpu \
        libfslcodec \
        libfslparser \
        libfslvpuwrap \
        libmcc \
        libz160 \
        mqxboot \
        mxsldr \
        virtual/kernel \
        virtual/bootloader \
        udev \
        u-boot \
        xserver-xorg \
        xf86-dri-vivante \
        xf86-video-imxfb \
        xf86-video-imxfb-vivante \
        $images \
        $packagegroups

    ret=$?
    if [ "$ret" != "0" ]; then
        echo "ERROR: error extracting bitbake metadata for board $MACHINE"
        exit 1
    fi
done

rm -rf $build_dir

cd $anchor
python ./bitbake-metadata2doc.py $marshalled_data_file "../release-notes/source" "$yocto_dir" "$gitdm_dir" "$start_commit" "$end_commit"
ret=$?
if [ $ret -ne 0 ]; then
    echo 'Error running bitbake-metadata2doc.py.  Aborting.' >&2
    exit $ret
fi

# Update open_bugs.inc and closed_bugs.inc:
./generate-bugs-table.py --open-bugs
./generate-bugs-table.py --closed-bugs --start-date 2014-05-20
