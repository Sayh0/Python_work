# process : 실행중인 프로그램을 의미. 자신만의 메모리를 확보하고 공유하지 않음
# thread : light weight process 라고도 한다. 하나의 process 내에는 최소 한 개의 thread 가 존재.
# process 내 여러 개의 thread를 운영하여 여러 개의 작업을 동시에 하는 것처럼 느끼게 할 수 있음.
# multi thread로 multitasking 이 가능

import threading, time


def run(id):
    for i in range(1, 51):
        print('id:{} --> {}'.format(id, i))
        time.sleep(0.2)
        
#thread 를 사용하지 않은 경우
#run(1)
#run(2)

# thread를 사용하는 경우
#threading.Thread(target=수행함수명)
th1=threading.Thread(target=run, args=('일')) #argument는 무조건 tuple 타입이어야 한다.
th2=threading.Thread(target=run, args=('이'))
th1.start()
th2.start()
th1.join()
th2.join() #메인스레드 종료까지 대기시킴

print('program terminated')
#스레드는 3개이다. 메인 스레드까지 있다는 것을 까먹지 말자~!