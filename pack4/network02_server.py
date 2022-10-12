## 서버 무한 루핑
import socket
import sys

HOST="127.0.0.1" #사실 HOST는 공백으로 채워놔도 가느한 주소 알아서 찾아서 알아서 해줌
#HOST = '' #이렇게도 가능
PORT=7878

serversock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    serversock.bind((HOST, PORT))
    serversock.listen(1)    # 동시 접속 최대 수 설정 (1 ~ 5)
    print('server started...')
    
    while True: #무한루프
        conn, addr=serversock.accept() #연결 대기
        print('client info : ',addr[0], addr[1]) #IP address, port number)
        print('message from client : ', conn.recv(1024).decode()) #메세지를 수신 
        
        # 메세지를 송신
        conn.send(('from server : '+str(addr[0])+'너도 잘 지내라~').encode('utf_8'))
        
except socket.error as err:
    print("ERROR : ",err)
    sys.exit() #강제종료
finally:
    serversock.close()
    conn.close()