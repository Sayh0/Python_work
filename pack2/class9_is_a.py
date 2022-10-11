## 클래스의 상속관계 : 다형성을 구사 가능

class Animal:
    def __init__(self):
        print("Animal' Constructor")
    def move(self):
        print("can move")

#상속        
class Dog(Animal): #자바에서는 extends Animal
    def __init__(self):
        print("'Dog' Constructor")
    def my(self):
        print("Dog")


dog1 = Dog() # 자식 클래스의 생성자가 존재할 때는 부모의 생성자는 명시적으로 작성않는 한 생성되지 않음.
dog1.move() #Animal의 멤버 사용 가능        
dog1.my()    

print('-----------------------')
class Horse(Animal):
    pass

horse1 = Horse() 
horse1.move()   #자바처럼 오버로딩은 안됨


