How to add the bad/ugly GStreamer plugins
=========================================

Bad and Ugly gstreamer plugins has their own special licensing, so by that reason they cannot be released formally inside a tarball. But you can add it on your own image, and you only need to change the local.conf

Please, add the following code to your local.conf:

.. literalinclude:: code-blocks/bad-ugly-gstreamer-plugins/add-gstreamer-plugins.sh
   :language: console

Please note that this will not install *every* plugin from GStreamer "ugly" or "bad". It will only install the plugins from the list.

If you want more info aboug GStreamer licenses please go to `GStreamer: Licensing advice <http://gstreamer.freedesktop.org/documentation/licensing.html>`_.
