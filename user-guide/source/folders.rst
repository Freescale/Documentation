Folders
=======

* **fsl-community-bsp**: Base (``BASE``) directory where all Yocto data reside (recipes, source code, built packages, images, etc.)

* **BASE/sources**: Source directory where metadata (layers) reside

* **BASE/build**: Build directory where ``bitbake`` commands are executed

* **BASE/build/tmp**: Target directory for all bitbake commands

* **BASE/build/tmp/work**: Working directory that holds the task output and source from each recipe

* **BASE/build/tmp/deploy**: Deploy directory where bitbake's deployable output files are copied

* **BASE/build/tmp/deploy/images**: Complete and partial images are found under this folder
