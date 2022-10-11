## 클래스의 이해
kor = 100 #전역변수 # 소속이 module

def abc(): #함수 #소속 module
    print('function')
    
class MyClass(): #클래스 #소속 module
    kor = 90 #멤버변수 #소속 MyClass
    #생성자는무조건 있다. 쓸내용이 없어서 안 적을순 있는데, 이경우엔 컴파일러가 알아서 만든다.
    '''
    def __init__(self):
        pass
    '''
    
    def abc(self): #메소드 #소속은 MyClass
        #너는 함수에 소속되어있는 메소드.
        print('method')
        
    def show(self):
        kor=80 #지역변수 #소속은 show 라는 method #show 에서만 유효
        print(self.kor) #90 #self는 자기자신(Class): 메소드 안에 있는 kor 가 아닌 class의 kor.
        print(kor) #80 #로컬 > 인클루딩펑션 > 전역 순서
        #메소드 내 지역변수가 없으면 (kor=80)이 없으면 모듈의 멤버(전역)을 참조한다.
        self.abc() #method
        abc() #function
        #파이썬은 클래스가 파일의 요소 중 하나일 뿐이기 때문에 이런 식의 접근이 가능. 자바랑 다르다.
        
        
my=MyClass()
my.show() #90
