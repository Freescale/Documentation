$ cd ~/test/
$ arm-poky-linux-gnueabi-gcc helloworld.c
$ ls
a.out                                                 helloworld.c
$ ./a.out
-bash: ./a.out: cannot execute binary file
$ file a.out
a.out: ELF 32-bit LSB executable, ARM, version 1 (SYSV), dynamically linked (uses shared libs), for GNU/Linux 2.6.16, not stripped
