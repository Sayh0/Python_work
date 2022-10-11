## Method Overriding 재정의

class Parent:
    def printData(self):
        pass
    
#파이썬은 추상클래스 쓰려면 꼭 언급을 해 줘야 한다.

class Child1(Parent):
    def printData(self):
        print('Child1에서 Overriding')

class Child2(Parent):
    def printData(self):
        print('Child2에서 Overriding')
        print('오버라이드는 부모의 메소드를 자식이 재정의하는 것')
        print('똑같은 이름을 가지고 있지만 다양한 형태로 구사 가능')
        
    def abc(self):
        print('Child2의 고유 메소드')
        
c1=Child1()
c1.printData()
print('_---------------------------_')
c2=Child2()
c2.printData()

print('_------------다형성------------_')
#par = Parent() #자바처럼 부모의 변수를 치환할 필요도 없음. 타입이 없음. 들어오는 데이터로 타입이 결정됨.
par=c1 #그냥 아무 변수에게나 넘겨주면 된다.
par.printData()
print()
par=c2
par.printData() #printData() 는 똑같은데 결과는 다름. 다형성의 결과
par.abc() #자바랑 다르게 자식의 고유 메소드도 실행 가능. 자바의 불간섭 원칙 적용 ㄴㄴ.

print()
plist=[c1, c2]
for i in plist:
    i.printData()
    
