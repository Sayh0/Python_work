# Client/Server(echo) 프로그래밍
# server

from socket import *

# socket 으로 서버 구성
serverSock=socket(AF_INET, SOCK_STREAM)   # socket(소켓의 종류, 소켓의 유형)
serverSock.bind(('127.0.0.1', 8888))
serverSock.listen(1)    # 동시 접속 최대 수 설정 (1 ~ 5)
print('server started...')

conn, addr=serverSock.accept() #연결 대기
print('addr : ', addr)
print('conn : ', conn)
print('message from client : ', conn.recv(1024).decode()) # 클라이언트가 달고 오는 메세지 수신
conn.close()
serverSock.close()
