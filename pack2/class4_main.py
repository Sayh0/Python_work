# 가수 한 명을 탄생시키려면...

# import pack2.class4
from pack2.class4 import SingerType #위와 같음.

def process():
    # ImYoungWoong = pack2.class4.SingerType()
    ImYoungWoong = SingerType() #임영웅이라는 싱어타입 객체가 하나 만들어짐
    print('YoungWoong\'s title song :',ImYoungWoong.title_song)
    ImYoungWoong.sing()
    
def process2():
    bts = SingerType()
    bts.sing()
    bts.title_song ="Yet to come"
    bts.sing() #위에서 새로 선언
    bts.co="HYBE"
    print('소속사 : ', bts.co)
    
if __name__ == '__main__': #응용프로그램 시작지점 표시(권장)
    process() 
    print('--------------------')
    process2()