Preparing the host environment
==============================

Before downloading the source code, first you need to make sure your host PC has
the required packages to run the Yocto tools.

**Debian/Ubuntu**

The essential packages you need for a supported Ubuntu distribution are shown in
the following command::

    $ sudo apt-get install gawk wget git-core diffstat unzip texinfo \
      build-essential chrpath libsdl1.2-dev xterm curl

**Fedora**

The essential packages you need for a supported Fedora distribution are shown in
the following command::

    $ sudo yum install gawk make wget tar bzip2 gzip python unzip perl patch \
      diffutils diffstat git cpp gcc gcc-c++ glibc-devel texinfo chrpath \
      ccache SDL-devel xterm

Or, take a look `here
<http://www.yoctoproject.org/docs/current/yocto-project-qs/yocto-project-qs.html>`_
if you use openSUSE or CentOS.

Download the source code
========================

Install repo, the repository management tool from Google::

    $ mkdir ~/bin
    $ curl http://commondatastorage.googleapis.com/git-repo-downloads/repo > ~/bin/repo
    $ PATH=$PATH:~/bin
    $ chmod a+x ~/bin/repo

Download the BSP source::

    $ mkdir fsl-community-bsp
    $ cd fsl-community-bsp
    $ repo init -u https://github.com/Freescale/fsl-community-bsp-platform -b daisy
    $ repo sync

.. note:: Required disk space for installing repo as of 2014-02-24 is about
          238MB. It may take up to 15 minutes to get the source code, depending
          on your Internet connection speed.

If you only need to update the source code to a new version, like daisy, just do::

    $ repo init -b daisy

Although, please **always** start a new/clean/fresh build directory, otherwise the
different version may result in weird build errors for several packages. As an
example, this tends to happen to the *avahi* package.
