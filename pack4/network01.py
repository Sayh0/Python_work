## 네트워킹 프로그래밍
## TCP PROTOCOL 기반의 socket(네트워크를 위한 통신 채널 지원 클래스 또는 함수)

import socket

print(socket.getservbyname('http', 'tcp')) #포트번호가 출력됨
print(socket.getservbyname('telnet', 'tcp'))
print(socket.getservbyname('ftp', 'tcp'))
print(socket.getservbyname('SMTP', 'tcp'))
print(socket.getservbyname('pop3', 'tcp'))

print(socket.getaddrinfo('www.naver.com', 80, proto=socket.SOL_TCP))
# 네이버가 가지고 있는 IP Address 출력 : 
# [(<AddressFamily.AF_INET: 2>, 0, 6, '', ('223.130.200.104', 80)), (<AddressFamily.AF_INET: 2>, 0, 6, '', ('223.130.195.95', 80))]
# 네이버는 서버를 여러 개 가지고 있는걸 알 수 있다.

