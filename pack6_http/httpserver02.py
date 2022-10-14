# 웹 서버 구축

from http.server import CGIHTTPRequestHandler, HTTPServer
# CGIHTTPRequestHandler : 동적으로 웹서버를 운영 가능
# DGI : 웹서버와 외부프로그램 사이에서 정보를 주고받는 방법 또는 규약

port = 8888

class Handler(CGIHTTPRequestHandler):
    cg_directories = ['/cgi-bin'] #튜플로 작성해도 상관없음
    
serv = HTTPServer(('127.0.0.1', port), Handler)
print("Web Service Started...")
serv.serve_forever()