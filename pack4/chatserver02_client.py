# 채팅 클라이언트

import socket
import threading
import sys

def handle(socket):
    while True: #서버가 보내는 메세지 계속 받기
        data = socket.recv(1024)
        if not data : continue
        print(data.decode('utf-8'))
        
sys.stdout.flush()  # 파이썬의 표준 출력은 버퍼링이 된다. 이때 버퍼를 비우기

name = input('채팅 아이디를 입력 : ')
cs = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cs.connect(('192.168.0.75', 5000)) #host와 port. 이게 실행되는 순간 챗서버의 어쎕트와 만남
cs.send(name.encode('utf-8'))

th = threading.Thread(target=handle, args=(cs,))
th.start()

while True: #내가 메세지 보내기
    msg = input(":")
    sys.stdout.flush() #버퍼 비우기
    if not msg:continue
    cs.send(msg.encode('utf-8'))
        
cs.close()