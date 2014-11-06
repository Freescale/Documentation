How can I contribute to the project?
------------------------------------

* Subscribe to the `mailing list <http://freescale.github.io/#contributing>`_
* Check the ``README`` file of the layer you are trying to patch. It lists the
  steps to start contributing. To summarize: create your commits locally,
  format them into patches (``git format-patch``) and send them to the 
  list (``git send-email``)

How can I build an image?
-------------------------

Steps are detailed here: `fsl-community-bsp-platform <https://github.com/Freescale/fsl-community-bsp-platform>`_


BitBake encountered an error, what can I do?
--------------------------------------------

A single answer can not be given due to the full range of possible errors. However, here are some suggestions:

* Check the mailing list to see if this error has been previously reported
* Clean-State the recipe that raised the error: ``bitbake -c cleansstate <PN>`` where ``PN`` is the recipe's name
* Check the log carefully by looking at the ``log`` files listed by the output from ``bitbake``


Which packages are included in an image?
----------------------------------------

Generate the `dot` file and filter out the native packages:

    $ bitbake -g <image-name> && cat pn-depends.dot | grep -v 'native' | more

where ``<image-name>`` is the name of the image you are building, i.e. ``core-image-minimal``


Which packages are available to be installed?
---------------------------------------------

Use the ``bitbake-layers`` script::

    $ bitbake-layers show-recipes | more


Which layers do I have configured?
----------------------------------

Use the ``bitbake-layers`` script::
    
    $ bitbake-layers show-layers

How do I add a package to an image?
-----------------------------------

Two of the ways are:

* Add ``IMAGE_INSTALL_append = " package-name-1 package-name-2 ..."`` to your
  ``local.conf`` file. Make sure there is a space after the opening quote '"'!

* Add ``CORE_IMAGE_EXTRA_INSTALL = "package-name-1 package-name-2 ..."`` to your ``local.conf`` file


How can I build an image containing the mainline Linux Kernel?
--------------------------------------------------------------

* Add ``PREFERRED_PROVIDER_virtual/kernel = "linux-fslc"`` to your ``local.conf``
  file.

* Clean the kernel's provider (state) and bake the image again::

    $ bitbake -c cleansstate virtual/kernel
    $ bitbake $IMAGE_NAME

How can I switch to Soft Floating Point?
----------------------------------------

By default, the system is configured for hard floating point. To change to soft floating point,
add ``DEFAULTTUNE_mx6 = "cortexa9-neon"`` to your ``local.conf`` file (or machine file).

How do I enable Chromiun?
-------------------------

To be added

How do I enable QT5.2?
----------------------

To be added

How can I modify source code and compile it?
--------------------------------------------

* Make your source code changes in the appropriate `tmp/work <http://www.yoctoproject.org/docs/current/dev-manual/dev-manual.html#finding-the-temporary-source-code>`_ folder

* Force compilation and (re)build::

    $ bitbake -c compile -f <recipe name>
    $ bitbake <recipe name>

How can I create a patch?
-------------------------

Yocto was not intended to be a package development framework, but in case you need to patch
a recipe, follow the `kernel patching guide <http://www.yoctoproject.org/docs/current/dev-manual/dev-manual.html#patching-the-kernel>`_ . For the Yocto Project, the kernel is like any other recipe, so this guide can be applied to any recipe.

How do I create a layer?
------------------------

* Create the new layer with the ``yocto-layer`` script::

    $ yocto-layer create <layer-name>

  where ``layer-name`` is the name of the layer you want to create.

* `Enable <http://www.yoctoproject.org/docs/current/dev-manual/dev-manual.html#enabling-your-layer>`_ your layer

What are the host packages needed for Yocto Project?
----------------------------------------------------

* Make sure your Linux host / distribution is `supported <http://www.yoctoproject.org/docs/1.5.1/ref-manual/ref-manual.html#detailed-supported-distros>`_ by the Yocto Project.

* Packages `needed <http://www.yoctoproject.org/docs/1.5.1/ref-manual/ref-manual.html#required-packages-for-the-host-development-system>`_


How can I save space after a build?
-----------------------------------

* Add  ``INHERIT += "rm_work"`` to your ``local.conf`` file. This feature will instruct
  ``BitBake`` to remove the working folder ``tmp/work`` after (bit)baking, so the next
  time you create an image it will basically execute all recipe tasks except the
  fetching step.

* In case you just need a particular file system type, add ``IMAGE_FSTYPES = "tar.bz2"``
  to your ``local.conf``.

Where do I check for known bugs?
--------------------------------

The known bugs are tracked using `Yocto Project Bugzilla <https://bugzilla.yoctoproject.org/buglist.cgi?quicksearch=meta-fsl-arm>`_


Are there prebuilt images available?
------------------------------------

Yes, kindly provided by `O.S. Systems <http://ci.ossystems.com.br/public/fsl-community-bsp/>`_
