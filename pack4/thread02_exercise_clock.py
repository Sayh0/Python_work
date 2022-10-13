## thread 활용 : 디지털 시간 출력해주는 프로그램
import time

now=time.localtime()
print(now)
print('{}년 {}월 {}일 {}시 {}분 {}초'.format(now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec))

print('----------------')

import threading

def cal_show():
    now=time.localtime()
    print('{}년 {}월 {}일 {}시 {}분 {}초'.format( 
        now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec))
    
def my_run():
    while True:
        now2=time.localtime()
        if now2.tm_min == 3 : break # 3분째에 while문 탈출
        cal_show()
        time.sleep(1)

th=threading.Thread(target=my_run) #실행된 결과인 my_run() 이 아닌 그냥 함수 my_run을 주는 것에 주의 
th.start()

th.join()
print('program terminated')