How to create a custom layer
============================

One of the most important features of Yocto is its ability to handle sublayers. To understand the sublayers in depth please read about it in the `Yocto Project Development Manual <http://www.yoctoproject.org/docs/1.4/dev-manual/dev-manual.html#understanding-and-creating-layers>`_.

Start by creating a *meta-custom* layer directory structure. For example:

.. literalinclude:: code-blocks/custom-layer/custom-layer-structure.sh
   :language: console

Here the custom application example is a helloworld application, but it's possible to create a *recipes-kernel* directory and place there your defconfig, or create a *bbappend* file to apply your patches to the kernel, or even create a *recipes-multimedia* and place there custom application for *GStreamer*, for example.

.. warning:: One important tip: BiBake see expects the recipe file name in the format **PACKAGENAME_VERSION.bb**. It uses the underline character ("_") to split the package name from it's version. So if you call your helloworld application as hello_world_1.0.bb BitBake will think your application is called "hello" and the version is "world_1.0", which is not what you probably want.

Configuring the layer with conf/layer.conf
******************************************

Within this file you define how your layer should behave. A common layer.conf file could like like this:

.. literalinclude:: code-blocks/custom-layer/layer.conf
   :language: console

To be able to use the new layer you must include it into the *build/conf/bblayers.conf* file, as shown bellow:

.. literalinclude:: code-blocks/custom-layer/bblayers.conf
   :language: console

To download an example meta layer with those characteristics you can click here: :download:`meta-layer-custom.tar.gz <downloads/meta-custom.tar.gz>`.

It includes one image definition that will install the Hello World application:

.. literalinclude:: code-blocks/custom-layer/custom-image-hello.sh
   :language: console

When the content of the image tar ball is extracted, an *hello_world* program compiled for the ARM architecture is going to be installed:

.. literalinclude:: code-blocks/custom-layer/hello-world-info.sh
   :language: console
