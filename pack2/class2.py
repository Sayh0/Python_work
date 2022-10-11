## 클래스-2

class Car: # Car type의 객체에서 참조가 가능한 멤버 필드 선언
    handle=0
    speed=0
    
    def __init__(self, name, speed): #파이썬은 전부 public이라 세터게터 안 써도 됨
        self.name = name    
        self.speed = speed
        
    def showData(self): #지역변수라 그냥 불러도 됨.
        km='kilometer'
        msg='speed : '+str(self.speed)+km + ', 핸들은 '+str(self.handle)
        return msg
        
print(id(Car)) #Car의 주소
print(Car.handle) # 객체이기 때문에 객체변수로 부를 수 있음. #클래스의 이름도 사실 객체변수
print(Car.speed) 
#method를 부르려면 어떻게 해야 하지?

print()
car1=Car('tom',10) #BoundmethodCall이라 self 생략.
#자바였으면 Car car1=new Car(); 
#생성자 호출 후 객체 생성. Car 와 독립된 주소.
#car type의 새로운 객체(car1)에 들어있는 tom 은 Car의 멤버가 아니다.
#비슷하게, 프로토타입인 Car의 speed는 0, Car type으로 생성된 객체인 car1의 스피드는 10이다.

print(car1.handle, car1.name, car1.speed) #0 tom 10
# car1 에 없으면 모체 클래스에서 찾는다. Car에 handle 있으니까 그걸 데려온다.
# 자바는 설계도에 손댈 수 없다. 파이썬에서는 객체변수의 이름으로 자유롭게 만들 수 있다.
car1.color='보라' #color 는 car1 에 만들어진다. 원형 클래스 Car에는 없음.
print('car1.color : %s'%car1.color)
print('-----------------------------------------')
# car2=Car() #이런건 없다

car2=Car('james', 20)
print(car2.handle, car2.name, car2.speed) #0 james 20
#car2 에선 color를 참조할 수 없다. car1 거니까.

print('주소 : ', id(Car), id(car1), id(car2))
#주소 :  2223847490992 2223860240592 2223860240736 # 모두 다름
#자바에서는 원형 클래스의 서례도를 직접 탐조하는 것을 막아둠. new 키워드로만 접근 가능
#C는 new 할수도 안 할수도 있음.
#파이썬은 그냥~~~쓸수있음.

print()
print('-----------------------------------------')
print(car1.showData()) #speed : 10kilometer
print(car2.showData()) #speed : 20kilometer       # Bound method call
print(Car.showData(car2)) #speed : 20kilometer    # print(car2.showData()) 와 같음. unBound method call
#원형클래스의 showData를 호출하지만, car2의 주소를 가져가기 때문에 주체는 car2가 된다.
print()
car2.speed=100
Car.handle=1 #원형(프로토타입)멤버를 변경함
car1.handle=2 #car1만 핸들으 ㄹ선언
print('car2: ', car2.showData()) #car2:  speed : 100kilometer, 핸들은 1
print('car1: ',car1.showData()) #car2:  speed : 100kilometer, 핸들은 1
# 타입만 같을 뿐 서로 독립.

print()
print('-----------------------------------------')