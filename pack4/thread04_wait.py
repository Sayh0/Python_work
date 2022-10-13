# 스레드간 자원공유 + 스레드 활성화 / 비활성화

import threading, time

bread_plate = 0 # 빵접시 - 공유자원
lock = threading.Condition()

class Maker(threading.Thread): #생산자 #Thread 상속받음
    def run(self):
        global bread_plate
        for i in range(30):
            lock.acquire()
            bread_plate +=1
            while bread_plate >= 10:
                print('bread plate is full, waiting...')
                lock.wait() #스레드 비활성화 ( 종료 아님 )
            print('bread baking: ', bread_plate)
            lock.notify() # 스레드 활성화
            lock.release() # 락 해제(점유 해제)
            time.sleep(0.05)
            
class Consumer(threading.Thread): #소비자
    def run(self):
        global bread_plate
        for i in range(30):
            lock.acquire() #acquire - release
            while bread_plate <= 1:
                print('bread plate is empty, waiting...')
                lock.wait() #스레드 비활성화 ( 종료 아님 ) #wait - notify
            bread_plate -=1
            print('bread eating : ', bread_plate)
            lock.notify() # 스레드 활성화
            lock.release() # 락 해제(점유 해제)
            time.sleep(0.05)
            
mak = []; con = []
for i in range(5):  #생산자 수
    mak.append(Maker())
    
for i in range(5):  #소비자 수
    mak.append(Consumer())
    
for th1 in mak:
    th1.start()
    
for th2 in con:
    th2.start()
    
for th1 in mak:
    th1.join()
    
for th2 in mak:
    th2.join()
    
print('today is closed')