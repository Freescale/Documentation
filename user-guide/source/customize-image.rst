Customize the image
===================

Ok, so now you know how to build an image, and even customize it's kernel. But let's say you need a custom image feature instead, one that it's not present by default in any of the stock images. To add it to your image you will need to customize it.

To do so you need to look at *<yocto>/source* and find an image you need to customize:

.. literalinclude:: code-blocks/customize-image/find-image.sh
   :language: console

You can use any of the recipe files above (and packages with 'image' in file name) as the base image where new packages, or new images, may be added.

To show any *available* package locally you can run the following command:

.. literalinclude:: code-blocks/customize-image/list-available-packages.sh
   :language: console

This will dump a list of *every* package available BitBake into the console. To make it easier to find the desired package you can pipe the output to grep, with the name of desired package as argument. For example, let's say you want to add a package that provides touchscreen calibrations, but can't remember it's name. So, by searching for "calibrat":

.. literalinclude:: code-blocks/customize-image/grep-calibrat.sh
   :language: console

You discover that the package you need is *xinput-calibrator*, which is the generic touchscreen calibration program for X.Org.

You now have the package name you want. To put it in the image you can do it in two places:

In order to include the package on all images you are testing, or at least for testing a image with the package before making a more profound change, you can alter the conf/local.conf file the to include the package, in the variable CORE_IMAGE_EXTRA_INSTALL:

.. literalinclude:: code-blocks/customize-image/add-xinput-calibrator-local-conf.sh
   :language: console

This will add the *xinput-calibrator* package as an extra package to be built in all images.

If you want to add it to a specific image, or make the change permanent in your repository, then you have to change the image recipe directly. On this example we're using the *fsl-image-test* recipe:

.. literalinclude:: code-blocks/customize-image/edit-fsl-image-test-recipe.sh
   :language: console

Then include the package name on the IMAGE_INSTALL list variable:

.. literalinclude:: code-blocks/customize-image/add-package-to-image-install.sh
   :language: console

Whichever the way you choose to change the resulting image, you just need to build the image again for it to take effect:

.. literalinclude:: code-blocks/customize-image/bitbake-image.sh
   :language: console

If during the build process you find that an unexpected package is being built, you can print the dependencies of all the packages of a image you need to run:

.. literalinclude:: code-blocks/customize-image/get-image-package-dependencies.sh
   :language: console

This will create several files on the *build* directory, which are:

* pn-buildlist: lists all the names of the packages that will be built by   BitBake;
* pn-depends.dot: lists all the packages names, filenames, versions and direct   dependencies (recursively), that will be built by BitBake;
* package-depends.dot: lists all the packages names, filenames, versions and   direct dependencies (recursively), **including documentation, test and   development libraries**, that will be built by BitBake;
* task-depends.dot: list the dependencies of all packages tasks;

Lastly, to development tools to the image, such as native compiler, linker and debugger, include this on conf/local.conf:

.. literalinclude:: code-blocks/customize-image/add-tool-sdk-feature.sh
   :language: console

Every image created after that will include the development tools. And also, by using the above example of adding a package to the image recipe you can include the development tools in a image recipe, to have a image specialized in development.

Here are a few other extra image features that can be added to the build process, from the Poky description:

* *tools-sdk*: Adds development tools such as gcc, make, pkgconfig and so forth.
* *dev-pkg*: Adds -dev packages for all installed packages. This is useful if   you want to develop against the libraries in the image.
* *tools-debug*: Adds debugging tools such as gdb and strace.

Hob
===

If you don't like command line and you prefer a window-like interface you can take a look on HOB.

See the `Hob documentation <https://www.yoctoproject.org/documentation/hob-manual>`_.  Watch the `Introducing Hob <https://www.youtube.com/watch?v=W3IXTdajqH4>`_ video on YouTube.
