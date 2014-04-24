Machine Mantainers
==================

Since FSL Community BSP Release 1.6 (Daisy), the maintainer field in machine configuration file of
meta-fsl-arm and meta-fsl-arm-extra machines is mandatory for any new board to be added.

So now on, every new board must have someone assigned as maintainer.
This ensures, in long term, all boards with a maintainer assigned.
Current orphan boards are not going to be removed unless it causes maintenance
problem and the fix is not straightforward.

The maintainer duties:
 * The one with casting vote when a deadlock is faced.
 * Responsible to keep that machine working (that means, booting and with some stability)
 * Keep kernel, u-boot updated/tested/working.
 * Keep release notes updated
 * Keep test cycle updated
 * Keep the most usual images building and booting

When a build error is faced, the maintainer will "fix" it. For those maintainers with kernel control (meta-fsl-arm-extra),
it is expected that they properly fix the kernel issue (when it's a kernel issue). However anything out of community control
should be worked around anyway.

Machines with maintainers
-------------------------
.. include:: machines-with-maintainers.inc

Machines without a maintainer
-----------------------------
.. include:: machines-maintainers.inc
