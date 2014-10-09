LICENSE_FLAGS_WHITELIST = "commercial"

COMMERCIAL_AUDIO_PLUGINS ?= " \
gst-plugins-ugly-mad \
gst-plugins-ugly-mpegaudioparse \
"
COMMERCIAL_VIDEO_PLUGINS ?= " \
gst-plugins-ugly-mpeg2dec \
gst-plugins-ugly-mpegstream \
gst-plugins-bad-mpegvideoparse \
"
CORE_IMAGE_EXTRA_INSTALL += " \
packagegroup-fsl-gstreamer \
gst-plugins-base-videotestsrc \
gst-plugins-bad-fbdevsink \
gst-ffmpeg alsa-utils \
gst-plugins-good-isomp4 \
"
