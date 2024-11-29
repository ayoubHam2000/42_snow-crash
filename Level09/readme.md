
```bash
level09@SnowCrash:~$ ls -l
total 12
-rwsr-sr-x 1 flag09 level09 7640 Mar  5  2016 level09
----r--r-- 1 flag09 level09   26 Mar  5  2016 token
```

Executing Level09 with different argument gives us a hint of what the original token file content format was. When executing Level09 with abcd, we get aceg.

We can notice that from abcd => aceg
```
a = a + 0
c = b + 1
e = c + 2
d = d + 3
```

Using this code to reverse the process.

```c
#include <unistd.h>
#include <stdio.h>
#include <fcntl.h>

int main(int ac, char **av)
{
  int f = open(av[1], O_RDONLY);

  char c;
  int counter = 0;

  char buf[2];
  while (read(f, buf, 1))
  {
    buf[0] -= counter;
    write(1, buf, 1);
    counter++;
  }
  write(1, "\n", 1);

  return 0;
}
```

We get `f3iji1ju5yuevaus41q1afiuq` to login as flag09 user

