##   클래스의 포함 관계 계속 공부하기
#    로또번호 출력하기

import random

class LottoBall:
    def __init__(self, num):
        self.num=num
        
class LottoMachine:
    def __init__(self):
        self.ballList=[]
        for i in range(1, 46): # 로또 볼 개수는 45개
            self.ballList.append(LottoBall(i)) #머신에서 로또볼 생성
            #이게 포함관계
            
    def selectBalls(self):
        # 볼 섞기 전 출력
        for a in range(45):
            print(self.ballList[a].num, end = " ")
        random.shuffle(self.ballList) #섞기
        print()
        for a in range(45):
            print(self.ballList[a].num, end = " ")
            
        return self.ballList[0:6]
        
            
class LottoUI:
    def __init__(self):
        self.machine=LottoMachine() #포함관계 #로또유아이가 로또머신을 가지고 있다
    
    def playLotto(self):
        input('press enter button')
        selectedBalls=self.machine.selectBalls()
        print('\n the number is...')
        for ball in selectedBalls:
            print('%d '%ball.num, end=" ")
        
if __name__ == '__main__':
    #LU = LottoUI()
    #LU.playLotto() 아래 한 줄로 줄이기 가능
    LottoUI().playLotto()
                    
            