from socket import *

clientsock=socket(AF_INET, SOCK_STREAM)
clientsock.connect(('192.168.0.75', 7878))   #능동적으로 서버에 접속 
clientsock.send("힘들면힘을놓자".encode(encoding='utf_8')) #엄격한 에러 체크
re_msg=clientsock.recv(1024).decode()
print('수신자료 : ', re_msg)
clientsock.close()