import json

file = open('./data4.json', 'r')
jdata = json.load(file)

only_data = [i["_source"]["layers"]["data"] for i in jdata if i["_source"]["layers"].get("data")]

res = ""
for item in only_data:
  item = item["data.data"].replace(':', '')
  res += item

for i in range(0, len(res), 2):
  c = res[i:i+2]
  n = int(c, 16)
  if (n >= 33 and n < 127):
    d = res[i:i+2]
    d = bytearray.fromhex(d).decode()
    print(d, end="")
  else:
    d = res[i:i+2]
    de = bytearray.fromhex(d).decode(encoding='ascii', errors='backslashreplace') 
    print(f"[{d}]", end="")


print(bytearray.fromhex(res).decode(encoding='ascii', errors='backslashreplace'))


