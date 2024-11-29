```bash
cat ./level04
```

- The Perl script simply creates a routine named `x` that takes the first parameter passed to it and stores it in `y`. Then, it executes `echo $y 2>&1` and prints the result.


- Using curl `http://localhost:4747?x='something'`
the response will be 'something'

- Trying with curl `http://localhost:4747?x='getflag|getflag'`
the command become 'echo getflag | getflag 2>&1'
hance executing `getflag` with the privilege of flag04 user.
