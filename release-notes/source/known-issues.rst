.. include:: variables.inc

************
Known Issues
************

.. only:: html

   ALL
   ===
   1. Fail to build imx-lib/imx-vpu/imx-test/gst-fsl-plugin when building
      against linux-fslc

   2. Weston/Wayland/Directb for SOC_FAMILY: imx5 or mxs or imx3 is not
      hardware accelerated and has not been tested.

   3. Hob is known to not work with with |project_name|. Some of known issues
      are problems generating the SD Card images and handling the GPU drivers.

   IMX28
   =====
   1. Touch screen (with x11 at least) is not completely calibrated

   2. **mfgtools** supported n |project_name| does not include support for
      i.mx28 (but it´s easy to be included and your patch is appreciated)

   3. Pendrive is not automatically mounted, but once you mount it
      everything works fine

   IMX6
   ====
   1. **perf** and **oprofile** are not supposed to work due to hardware issue
      (YOCTO5148 and YOCTO4511)

   Bugzilla
   ========
   The list of open bugs on Bugzilla Yocto Project on time of the writing of
   this document is on next table.

   Open
   ----
   In order to see the current bug list, please use following URL:
   https://bugzilla.yoctoproject.org/buglist.cgi?quicksearch=meta-fsl-arm

   .. table:: List of open bugs

      .. include:: open_bugs.inc

   Closed
   ------
   See the list of issues closed in latest development release in the following
   table:

   .. table:: List of closed bugs

      .. include:: closed_bugs.inc

.. only:: not html

   The list of known issues for the |project_name| can be seen at the following
   URL:

   https://bugzilla.yoctoproject.org/buglist.cgi?quicksearch=meta-fsl-arm

   It has not been included here as it changes every time bug fixes are
   included during the maintenance cycle of the release and it would
   be outdated most of time.
