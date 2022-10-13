# DB에서 트랜잭션이 시작되면 엉키지 않게 막아주는 것이 필요. << 데드락
# 여러 스레드 간 공유자원 충돌 방지
# Synchronize. 동기화. 줄서는 개념. - 하나의 스레드가 자원을 사용하는 동안 다른 스레드는 공유자원 사용을 대기.

import threading, time

g_count = 0 # 전역변수는 자동으로 스레드의 공유자원읻 된다.
lock = threading.Lock()

def threadCount(id, count):
    global g_count 
    for i in range(count):
        lock.acquire() #스레드간 충돌 방지용. 현재 스레드가 공유자원을 점유하고 있는 동안 다른 스레드는 대기상태.
        print('id:%s ===> count:%s, g_count:%s'%(id, i, g_count))
        time.sleep(0.1)
        g_count += 1 
        lock.release() #처리 끝나면 공유자원 점유 해제를 위해 lock 해제.
        
for i in range(1,6):
    threading.Thread(target=threadCount, args=(i, 5)).start()
    #스레드를 5개 만들고 각각의 스레드에 id를 부여
    
time.sleep(2)
print('after processing... final g_count : ', g_count)
print('program terminated')
    
