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