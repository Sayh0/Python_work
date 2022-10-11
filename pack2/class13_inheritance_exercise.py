## 상속
## https://cafe.daum.net/flowlife/RUrO/24 다중상속 문제

class ElecProducts:
    volume=0
    
    def VolumeControl(self, volume): # 이거 오버라이드 안 하면 메소드를 만들 수 없음.
        #자바에서 new 할수 업슨 거나 마찬가지. 추상이 하는 일(파이썬은 사실 추상 잘 안씀)
        pass
    
class ElecTv(ElecProducts):
    def VolumeControl(self, volume):
        self.volume += volume
        print('TV sound volume : ', self.volume)
        
class ElecRadio(ElecProducts):
    def VolumeControl(self, volume):
        tmp = self.volume + volume
        self.volume = tmp
        print('Radio sound volume : ', self.volume)
        
tv=ElecTv()
radio=ElecRadio()
abc=tv
abc.VolumeControl(3)

abc=tv
abc.VolumeControl(3)
