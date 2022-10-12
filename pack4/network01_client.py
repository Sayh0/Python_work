## 단순 클라이언트

from socket import *

clientsock=socket(AF_INET, SOCK_STREAM)
clientsock.connect(('192.168.0.75', 8888))   #능동적으로 서버에 접속 
clientsock.send("거기가 서버 맛집인가요?".encode(encoding='utf_8',errors='strict')) #엄격한 에러 체크
clientsock.close()