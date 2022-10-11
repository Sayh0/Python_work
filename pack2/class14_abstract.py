## 추상 클래스(추상 메소드) - 자식 클래스에서 부모 메소드의 이름을 강요하도록 하는 것 
# 추상 클래스의 사용 목적은 자식 클래스에서 메소드의 이름을 강요하기 위함이다(다형성 활욜을 강제하기 위해)

from abc import *

class AbstractClass(metaclass = ABCMeta): #추상 클래스가 됨
    @abstractmethod
    def myMethod(self): #추상 메소드가 됨
        pass
    
    def normalMethod(self):
        print('추상클래스는 일반 메소드를 가질 수도 있긴 하다.')
        
#parent = AbstractClass() #에러. 
# TypeError: Can't instantiate abstract class

class Child1(AbstractClass):
    name = 'I am Child1!'
    
    def myMethod(self): 
        print("Child1에서 추상 메소드에 내용을 적음")
        #추상 메소드를 오버라이드 해야 에러에서 벗어날 수 있음 

c1=Child1()
print(c1.name)
c1.myMethod()

print('------------------------------------')

class Child2(AbstractClass):
    def myMethod(self):
        print('Child2: 추상클래스의 추상 메소드는 오버라이드가 강제적이다.')
        print('오버라이드 해야 에러가 안 난다')
        
    def normalMethod(self):
        print('추상클래스의 일반 메소드는 오버라이드를 해도 되고 안해도 된다.')
        
    def good(self):
        print('Child2의 고유 메소드')
        
c2=Child2()
c2.myMethod()
c2.normalMethod()
c2.good()

print('------------------------------------')

tmp=c1
tmp.myMethod()
print()
tmp=c2
tmp.myMethod()

        