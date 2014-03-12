How can I contribute to the project?
------------------------------------

* Subscribe to the `list <http://freescale.github.io/#contributing>`_
* Check the ``README`` file of the layer you are trying to patch, it has the 
  steps to start contributing. In resume, create your commits locally, 
  format them into patches (``git format-patch``) and send them to the 
  list (``git send-email``)

How can I build an image?
-------------------------

Steps are detailed on `fsl-community-bsp-platform <https://github.com/Freescale/fsl-community-bsp-platform>`_ repository.


Bitbake encountered an error, what can I do?
--------------------------------------------

A final answer can not be given due to the full range of possible errors. Some suggestions:

* Check on the mailing list if this error has been reported
* Clean-State the recipe raising the problem: ``bitbake -c cleansstate $PN`` where ``PN``
  is the recipe's name.
* Check the log carefully and look at ``log`` files pointed by ``bitbake``


Which packages are included on an images?
-----------------------------------------------

Generate the `dot` file and filter native packages::

    $ bitbake -g <image name> && cat pn-depends.dot | grep -v 'native'

where ``<image name>`` is the name of the image you are building, i.e. ``core-image-minimal``


Which packages are available to be installed?
---------------------------------------------

Use the ``bitbake-layers`` script::

    $ bitbake-layers show-recipes


Which layers do I have configured?
----------------------------------

Use the ``bitbake-layers`` script::
    
    $ bitbake-layers show-layers

How do I add a package into an image?
-------------------------------------

Two ways:

* Append ``IMAGE_INSTALL_append = " package-name-1 package-name-2 ..."`` into your 
  ``local.conf`` file. Just make sure there is a space as the beginning!

* Append ``CORE_IMAGE_EXTRA_INSTALL = "package-name-1 package-name-2 ..."`` into your
  ``local.conf`` file


How can I build an image containing mainline Linux Kernel?
----------------------------------------------------------

* Append ``PREFERRED_PROVIDER_virtual/kernel = "linux-fslc"`` on your ``local.conf``
  file.

* Clean the Kernel's provider and bake the image again::

    $ bitbake -c cleansstate virtual/kernel
    $ bitbake $IMAGE_NAME

How can I switch to Soft Floating-Point?
----------------------------------------

By default, the system is configure as Hard Float-Point, so to change to Soft Float-Point,
append ``DEFAULTTUNE_mx6 = "cortexa9-neon"`` to your ``local.conf`` file (or machine file).

How do I enable Chromiun?
-------------------------

How do I enable QT5.2?
----------------------

How can I modify source code and compile?
-----------------------------------------

* Do any code change under the corresponding `tmp/work <http://www.yoctoproject.org/docs/current/dev-manual/dev-manual.html#finding-the-temporary-source-code>`_ folder

* Force compiling and build::

    $ bitbake -c compile -f <recipe name>
    $ bitbake <recipe name>

  where ``<recipe name>`` is the name of the recipe involved.

How can I create a patch?
-------------------------

Yocto was not intended as a package development framework but in case you need to patch 
a recipe, follow `the Kernel patching <http://www.yoctoproject.org/docs/current/dev-manual/dev-manual.html#patching-the-kernel>`_ guide. For Yocto Project, the Kernel is like any
other recipe, so this guide can be applied to any recipe.

How do I create a layer?
------------------------

* Create the layer with the ``yocto-layer`` script::

    $ yocto-layer create <layer name>

  where ``layer name`` is the name of the layer you want, resulting in ``meta-<layer name>``.

* Enable your `layer <http://www.yoctoproject.org/docs/current/dev-manual/dev-manual.html#enabling-your-layer>`_

What are the host's packages needed for Yocto Project?
------------------------------------------------------

* Make sure your Linux Host is `supported <http://www.yoctoproject.org/docs/1.5.1/ref-manual/ref-manual.html#detailed-supported-distros>`_

* Packages `needed <http://www.yoctoproject.org/docs/1.5.1/ref-manual/ref-manual.html#required-packages-for-the-host-development-system>`_


How can I save space after a built?
-----------------------------------

* Append ``INHERIT += "rm_work"`` to your ``local.conf`` file. This feature will indicate
  ``bitbake`` to remove the working folder ``tmp/work`` after (bit)baking so next 
  time you create an image, it will basically execute all recipes' tasks except the 
  fetching step.

* In case you just need a particular file system's type, append ``IMAGE_FSTYPES = "tar.bz2"``
  to your ``local.conf``.

Where do I check for known bugs?
----------------------------------

The known bugs are handled using the `Yocto Project Bugzilla <https://bugzilla.yoctoproject.org/buglist.cgi?quicksearch=meta-fsl-arm>`_


Are there prebuilt images available?
------------------------------------

Kindly provided by `O.S. Systems <http://ci.ossystems.com.br/public/fsl-community-bsp/>`_
