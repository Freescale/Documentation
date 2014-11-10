Weston
======

In order to test Weston, the reference implementation of a Wayland compositor, use the image *core-image-weston*

Add the following to conf/local.conf::

    DISTRO_FEATURES_remove = "x11"

And bake the image::

	$ bitbake core-image-weston

Remember to use a clean build-dir when changing `DISTRO_FEATURES`


Simple tests
------------

In order to access Weston examples via a console::

    $ export XDG_RUNTIME_DIR=/var/run/user/root
    $ weston-simple-shm => basic wayland example
    $ weston-simple-egl => basic wayland example. To make sure egl integration works fine
    $ weston-terminal => To make sure cairo integration works fine.

Enabling multibuffering
-----------------------

::

    $ export FB_MULTI_BUFFER=2
    $ /etc/init.d/weston restart

How to start with `gal2d` compositor::

    $ /etc/init.d/weston stop
    $ weston –tty=1 –use-gl=0 –use-gal2d=1 &

Using Multi (extended) display, make sure `/dev/fb0` and `/dev/fb1` has
same color depth::

    $ /etc/init.d/weston stop
    $ weston –tty=1 –use-gl=0 –use-gal2d=1 –device=”dev/fb0,/dev/fb2” &

Using QT5, need to build meta-qt5 with qtwayland package. Then run
with::

    $ hellogl_es2 –platform wayland-egl
