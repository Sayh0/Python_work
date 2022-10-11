## 클래스의 상속 관계2
class Person:
    say = "I'm a man~"
    age = '22 years old'
    __kbs='Korea Broadcast Studio' #이건 private 변수. Person 클래스에서만 유효
    
    def __init__(self, age):
        print("'Person's Constructor")
        self.age= age # 새로 만든 객체의 age이기 때문에 클래스의 age와 메모리 주소가 다름
    
    def printInfo(self):
        print('나이:{}, 이야기:{}'.format(self.age, self.say))
        
    def hello(self):
        print("Hi", self.__kbs)
        
print(Person.say, Person.age)
#Person.printInfo() 는 불가능   

print('-------------------')
'''
class Employee(Person):     
    pass

emp=Employee('26') #emplyee의 나이 26이 들어감.
emp.printInfo()
'''

class Employee(Person):
    say = "Working animal ^^" #부모의 say는 은닉화.
    subject = "Worker" 
    
    def __init__(self):
        print('\'Employee\'s Constructor')
        
    def printInfo(self): # 오버라이딩. 부모의 printInfo 메소드는 은닉화된다.
        print('Employee\'s printInfo method')    
    
    def empPrintInfo(self):
        print(self.say, self.age, self.subject)
        print(self.say, super().say) #super는 부모 것 데려온다.
        self.printInfo()
        super().printInfo() #Person 의 PrintInfo
        self.hello() #self에 hello가 없으면 부모로 올라가서 데려온다
        # print(super().say, super().__kbs) 이건 __kbs 때문에 error. private은 상속 안된다.
        
            
# emp = Employee('26') # 생성자가 있는데 거기엔 self만 있어서 추가 인자가 필요 없음. 
# TypeError: __init__() takes 1 positional argument but 2 were given
emp = Employee()
emp.printInfo()
print()
emp.empPrintInfo() #employee 에서 없으면 부모인 Person 에서 찾는다.
print('================================')
class Worker(Person):
    def __init__(self, age):
        print('Worker Constructor')
        super().__init__(age) #명시적으로 부모 생성자 호출
        # age를 가지고 들어감.
        
    def wPrintInfo(self):
        self.printInfo()
        
wor=Worker('28')
print(wor.say, wor.age)
wor.wPrintInfo()

print('===============================')
class Programmer(Worker):
    def __init__(self, age):
        print('Programmer Constructor')
        #super().__init__(age) #Bound call
        Worker.__init__(self, age) #UnBound call
        
    def ProShow(self):
        self.printInfo()
        
pr=Programmer('30')
print(pr.say, pr.age)
pr.ProShow()
print('===============================')
print(type(3))
print(type(pr))
print(type(wor))
print(Programmer.__bases__, Worker.__bases__, Person.__bases__) # 상위 클래스 알아보기
# (<class '__main__.Worker'>,) (<class '__main__.Person'>,) (<class 'object'>,)

