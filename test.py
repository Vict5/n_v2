import os
addr=os.popen("curl https://raw.githubusercontent.com/txt-sys/txt/refs/heads/main/ip.txt").read()
naddr=""
print(addr)
for n in addr:
        if n=='\n':
            break
        else:
            naddr+=n
print(naddr)