
Copy the file to my host machine for analysis using Wireshark.
```bash
scp -P 4242 level02@[ip]:[source] ./[distination]
```

- Open the file with wireshark
- Save all the data into json file
- After interpreting the sent and received data using the python script we can extract the password as:

`Password:[20]ft_wandr[7f][7f][7f]NDRel[7f]L0L[0d][00][0d][0a][01][00][0d][0a]`

Interpreting [7f] as backspace character we get

`ft_waNDReL0L`
