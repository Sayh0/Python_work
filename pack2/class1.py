## class : 새로운 타입을 만드는 것. 객체지향적(중심적)인 프로그래밍
# 객체지향적 프로그래밍 이 뭔지 이해해야 함
# 형식: class 클래스명() : 멤버(필드, 메소드) ~
# 생성자, 소멸자가 있다.
# 접근지정자, 메소드 오버로딩이 없다.
# 다중상속 가능, interface 없음.

print('do something...')
print('모듈의 멤버인 클래스를 선언한다')

class TestClass:    #prototype, 원형 클래스 라고 함
    # new 그런 것 없이 바로 객체로 만들어짐.
    aa = 1 #멤버변수(멤버필드), public    
    
    def __init__(self): #생성자
        print('this is constructor')
        
    def __del__(self): #소멸자
        print('this is destructor')
        # 소멸자는 클래스 끝나면 알아서 메모리에서 방 빼줌
        # 자바의 가비지콜렉터처럼 알아서 작동하기 때문에 사실 쓸 일은 거의 없다.
        
    def printMessage(self): #method
        name= 'korean' #local var
        print(name)
        print(self.aa) #자바에서 this 같은 것
        
print(TestClass(), id(TestClass))
print(TestClass.aa) #1이 바로 나옴. #멤버필드 바로 호출 가능

print()
test=TestClass() #생성자 호출 후 TestClass type 의 객체 생성됨
#인스턴스가 되었다 라고 이해하면됨.
print(test.aa) #멤버필드 호출

#메소드 호출하기
# TestClass.printMessage() #error:메소드 안에 있는 녀석은 반드시 셀프를 가져야 함
test.printMessage() #Bound method call #객체변수(test)가 프린트메세지 안으로 들어간다.
#마치 test.printMessage(test) << self로 들어가 버린~
TestClass.printMessage(test) #UnBound method call. 위와 결과는 같음.
#일반적으론 Bound method call 을 사용
print()
print('--------------------------------------------')
print()
print(type(1)) 
print(type(1.1))
print(type(test)) #<class '__main__.TestClass'> #TestClass 타입.
print(id(test), id(TestClass)) #객체의 주소는 2개 2324830834896 2324818041088
# 원형클래스, 원형클래스로 만든 객체 모두 각각의 공간을 가지고 있다.


