## 다중상속

class Tiger:
    data="Tiger World"
    
    def cry(self):
        print("Tiger U-Heong")
        
    def eat(self):
        print("like meat")
        
class Lion:
    def cry(self):
        print("Lion G-rrr")
        
    def hobby(self):
        print("Lion likes nap")
        
class Liger1(Tiger, Lion): #다중상속
    pass

a1=Liger1()
a1.cry() # 먼저 적은 클래스의 멤버에 우선순위가 있다.
a1.eat()
a1.hobby()
print(a1.data)

print('--------------')

class Liger2(Lion, Tiger):
    data='Long live the Liger!'
    
    def hobby(self):
        print('Liger loves JAVA')
        
    def showData(self):
        print(self.data, ' ', super().data)
        self.hobby() #현재 클래스에서 hobby를 찾는다. 없으면 부모에서 찾는다.
        super().hobby() #처음부터 부모로 올라간다.
        # hobby() #module의 함수를 부르는 것.
        
a2=Liger2()
a2.cry()
a2.hobby() #자식 클래스에 우선순위
a2.showData()