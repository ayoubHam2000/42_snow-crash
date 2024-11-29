
```bash
level13@SnowCrash:~$ ls -l
total 8
-rwsr-sr-x 1 flag13 level13 7303 Aug 30  2015 level13
```

```bash
level13@SnowCrash:~$ file level13 
level13: setuid setgid ELF 32-bit LSB executable, Intel 80386, version 1 (SYSV), dynamically linked (uses shared libs), for GNU/Linux 2.6.24, BuildID[sha1]=0xde91cfbf70ca6632d7e4122f8210985dea778605, not stripped
```

```bash
level13@SnowCrash:~$ ./level13 
UID 2013 started us but we we expect 4242
```

Using GDB, we can easily see that there is a call to `getuid()`, which returns the real user ID of the calling process. The returned ID is that of `level13` (`2013`), which is not equal to `4242`.

```bash
level13@SnowCrash:~$ id
uid=2013(level13) gid=2013(level13) groups=2013(level13),100(users)
```

## Method 1

We can use gdb to change the returned value of `getuid()` by changing the value of the register `eax` from 2013 to 4242.

```
disassemle main
b main
... ni until we surpass getuid() call
set $eax=4242
step
```

## Method 2

Change the behavior of `getuid()` by linking the executable by our dynamic library.

```c
int getuid()
{
  return 4242;
}
```

```bash
gcc --shared -o /tmp/getuid.so /tmp/main.c
export LD_PRELOAD='/tmp/getuid.so'
```
