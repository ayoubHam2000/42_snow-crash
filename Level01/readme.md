```bash
level01@SnowCrash:~$ find / -user flag01 2> /dev/null
(nothing)
```

There is a hashed password for the flag01 user inside the `/etc/passwd` file.

```bash
level01@SnowCrash:~$ cat /etc/passwd | grep "flag01"
flag01:42hDRfypTqqnw:3001:3001::/home/flag/flag01:/bin/bash
```

Trying to identify the hash type.
- Method1:
  * https://www.tunnelsup.com/hash-analyzer/
  * Hash type:	DES or 3DES?
- Method2:
  * hash-identifier command
  * DES (Unix)

Crack the password using hashcat tool.

```bash
hashcat -m 1500 -a 3 hash.txt ?l?l?l?l?l?l?l
hashcat -m 1500  hash.txt --show
➜ abcdefg
```

### Extra
Generate hash using mkpasswd command:

```bash
➜  ~ mkpasswd -m des "abcdefg" -S '42'
42hDRfypTqqnw
```
