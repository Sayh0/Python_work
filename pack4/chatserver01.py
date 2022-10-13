# 멀티 채팅 서버 프로그램 - socket + thread
import socket
import threading

ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ss.bind(('127.0.0.1', 5000))
ss.listen(5)
print('chatting server service started...')

users=[] #클라이언트를 담아둘 통

def chatUser(conn): #스레드 처리함수
    name = conn.recv(1024)
    data = name.decode('utf-8') + '님이 입장하였습니다.'
    print(data)
    try:
        for p in users:
            p.send(data.encode('utf-8'))
            
        while True:
            msg = conn.recv(1024) #메세지가 있으면 출력한다.
            if not msg:continue # 메세지가 없는 경우도 있으니 그럴땐 그냥 continue
            data = name.decode('utf-8') + '님의 메세지 : ' + msg.decode('utf-8')
            print('수신 내용 : ', data)
            for p in users:
                p.send(data.encode('utf-8'))   
    except:
        users.remove(conn)
        data = "---" + name.decode('utf-8') + "님이 퇴장하였습니다. ---"
        print(data)
        if users: #파이썬에서는 0만 아니면 true
            for p in users:
                p.send(data.encode('utf-8'))
        else:
            print('사용자가 없습니다.')
    
while True:
    conn,addr = ss.accept() #여기서 대기하다가 클라이언트가 커넥트 시도하면 승인
    users.append(conn)  # 클라이언트를 저장
    th = threading.Thread(target=chatUser, args=(conn,))
    th.start()