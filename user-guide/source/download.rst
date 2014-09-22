Preparing the host environment
==============================

Before downloading the source code, first you need to make sure your host PC has
the required packages to run the Yocto tools.

**Debian/Ubuntu**

The essential packages you need for a supported Ubuntu distribution are shown in
the following command:

.. literalinclude:: code-blocks/download/install-essential-packages-debian-ubuntu.sh
   :language: console

**Fedora**

The essential packages you need for a supported Fedora distribution are shown in
the following command:

.. literalinclude:: code-blocks/download/install-essential-packages-fedora.sh
   :language: console

Or, take a look `here
<http://www.yoctoproject.org/docs/current/yocto-project-qs/yocto-project-qs.html>`_
if you use openSUSE or CentOS.

Download the source code
========================

Install repo, the repository management tool from Google:

.. literalinclude:: code-blocks/download/install-repo.sh
   :language: console

Download the BSP source:

.. literalinclude:: code-blocks/download/download-bsp.sh
   :language: console

.. note:: Required disk space for installing repo as of 2014-02-24 is about
          238MB. It may take up to 15 minutes to get the source code, depending
          on your Internet connection speed.

If you only need to update the source code to a new version, like
|current-branch|, just do:

.. literalinclude:: code-blocks/download/start-new-repo-branch.sh
   :language: console

Please, **always** start a new/clean/fresh build directory when you start
working with a new version, otherwise the different version may result in weird
build errors for several packages. As an example, this tends to happen to the
*avahi* package.
