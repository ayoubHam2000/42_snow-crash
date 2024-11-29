```bash
level14@SnowCrash:~$ ls -l
total 0
```

```bash
level14@SnowCrash:~$ find / -user flag14 2> /dev/null
level14@SnowCrash:~$
```

Mmm... There is not flag nor an executable file, other technics of the previous exercise yield nothing.

Since we now know how to trick an executable into mistaking the user with a debugger, let's see if we can do the same with `getflag`.


Using `strings /bin/getflag` we can notice easily
```
I`fA>_88eEd:=`85h0D8HE>,D
7`4Ci4=^d=J,?>i;6,7d416,7
<>B16\AD<C6,G_<1>^7ci>l4B
B8b:6,3fj7:,;bh>D@>8i:6@D
?4d@:,C>8C60G>8:h:Gb4?l,A
G8H.6,=4k5J0<cd/D@>>B:>:4
H8B8h_20B4J43><8>\ED<;j@3
78H:J4<4<9i_I4k0J^5>B1j`9
bci`mC{)jxkn<"uD~6%g7FK`7
Dc6m~;}f8Cj#xFkel;#&ycfbK
74H9D^3ed7k05445J0E4e;Da4
70hCi,E44Df[A4B/J@3f<=:`D
8_Dw"4#?+3i]q&;p6 gtw88EC
boe]!ai0FB@.:|L6l@A?>qJ}I
g <t61:|4_|!@IF.-62FH&G~DCK/Ekrvvdwz?v|
```


Using `https://dogbolt.org/`
to disassemble `getflag` we can see that we call `ft_des` for each of these strings

- The result of getuid() is stored in $eax.
- Since we are interested in `flag14` (which corresponds to 3014 = 0xbc6),
- we can search for `0xbc6` using GDB.

```
disas main
```
```
0x08048bb6 <+624>:	cmp    $0xbc6,%eax
0x08048bbb <+629>:	je     0x8048de5 <main+1183>
0x08048bc1 <+635>:	jmp    0x8048e06 <main+1216>
```
If the condition is true, we continue at `<main+1183>`.

```
0x08048de5 <+1183>:	mov    0x804b060,%eax
0x08048dea <+1188>:	mov    %eax,%ebx
0x08048dec <+1190>:	movl   $0x8049220,(%esp)
0x08048df3 <+1197>:	call   0x8048604 <ft_des>
```

Checking the value of 0x8049220

```
print (char *)0x8049220
$4 = 0x8049220 "g <t61:|4_|!@IF.-62FH&G~DCK/Ekrvvdwz?v|"
```

We are on the right path so far, since we are interested in decrypting this value `g <t61:|4_|!@IF.-62FH&G~DCK/Ekrvvdwz?v|`

By continuing at 0x8048de5 we get the flag of the user `flag14`

```
jump *0x08048de5
```

```bash
level14@SnowCrash:~$ su flag14
Password: 
Congratulation. Type getflag to get the key and send it to me the owner of this livecd :)
flag14@SnowCrash:~$ 
```