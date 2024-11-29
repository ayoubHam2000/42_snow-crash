
Find flags owned by flag00.

```bash
level00@SnowCrash:~$ find / -user flag00 2> /dev/null
/usr/sbin/john
/rofs/usr/sbin/john
```

```bash
level00@SnowCrash:~$ cat /usr/sbin/john
cdiiddwpgswtgt
```

- Using Caesar Cipher
- https://cryptii.com/pipes/caesar-cipher
- With 11 rotation: nottoohardhere

```
level00@SnowCrash:~$ su flag00
Password: 
Don't forget to launch getflag !
flag00@SnowCrash:~$ getflag
Check flag.Here is your token : x24ti5gi3x0ol2eh4esiuxias
```