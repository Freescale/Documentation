.. |check_mark| raw:: html

   <span class="test_result success">&#x2713;</span>

.. |x_mark| raw:: html

   <span class="test_result error">&#x2717;</span>

.. |exclamation_mark| raw:: html

   <span class="test_result warning">?</span>

.. |na_mark| unicode:: U+2014

Test results
============

The test result is a Community effort. Please, see who participated on test cycle
on Acknowledgement Section.

Goals
-----

The principles of the FSL BSP Community test cycle is make sure the integration
of packages provided by Freescale and by community is correct. There is no intention
of stress test for one single kernel feature, or one used case.

The release was tested focusing on following goals:

MUST HAVE:
 * all 35 boards MUST reach the user space prompt
 * all 35 boards MUST have some[#f1]_ stability
 * all IMX6 boards MUST have X11 up and running accelerated

SHOULD HAVE:
 * all boards SHOULD play at least one movie
 * all boards SHOULD encode at least one kind of movie
 * all boards SHOULD have minimal kernel defconfig enabled by default (USB/SDcard/aplay)

BONUS POINT:
 * all IMX6 boards SHOULD have GPU and VPU support for both SFP and HFP
 * all board SHOULD have overnight stability[#f2]_


.. [#f1] some stability now is defined as being alive during the form tests
.. [#f2] overnight stability now is defined by the board being alive after more than 10 hours testing memtester 50M (last question from form, Bonus Point)


Definition
----------

For following tables, please, consider this definition:

 * |x_mark|           : error on every test
 * |check_mark|       : success on every test
 * |exclamation_mark| : at least one error
 * |na_mark|          : not applicable
 * **empty**          : no test reported

MUST HAVE
---------

Three goals provided the very basic features the boards must achieve in order to
be considered 'alive'. Please see the results for each board

.. include:: test-must-have.inc

From the table, the following boards may be considered OK:

 * cfa10036
 * cfa10037
 * cfa10049
 * cfa10055
 * cfa10056
 * cfa10057
 * cfa10058
 * imx28evk
 * imx53qsb
 * imx53ard
 * imx6qsabrelite
 * wandboard-dual

SHOULD HAVE
-----------

The *should have* goals intend to garantee the minimum set of features of a functional
system such as VPU playback, VPU encoding, and minimum kernel config integration.
Please, find the test results on next table.

Aplay results is specily important because aplay does use several part to be functional
audio codec, sdma firmware and integration, spi transfer.

.. include:: test-should-have.inc

The following boards have been tested by one (or more) people, and
submitted the results for accounting.


Bonus Point!
------------

This release is the first one to introduce SFP and HFP binaries for imx6 boards.
The overnight memtester test is a good stress test for both memory and system.

Please, find the test results in the following table:

.. include:: test-bonus-point.inc

