Creating a toolchain for your board
===================================

To help you develop for your board you can build a toolchain image. The
toolchain includes all the necessary programs and libraries you defined to be
used on the board.

To create the package just run BitBake with this image:

.. literalinclude:: code-blocks/toolchain/bitbake-meta-toolchain.sh
   :language: console

As any other image, it does take some time to build.

By using the meta-compiler image the called compiler, linker, and other programs
are going to be the ones generated with the toolchain. Also, all the compiled
binaries are going to be generated for the board architecture. This makes
developing and testing programs for the board much easier than generating a
complete image everytime you want to change anything.

In the next section you will learn how to use the toolchain to develop for the
board architecture.

Why do I have to create a toolchain?
************************************

The Yocto Project tools are not intended to be used to package development. They
are used to *create* Linux distributions. It's intended to be a image builder, a
rootfs creator. See more about what The Yocto project is about on the Project's
`about page <https://www.yoctoproject.org/about>`_ and `here
<http://mulhern-at-yocto.dreamwidth.org/2252.html>`_

So, Yocto itself should not be used to "develop" a new package. Although, Yocto
can help creating a environment for development like meta-toolchain or Eclipse
ADT.
