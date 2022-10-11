## 포함관계
# 냉장고에 음식 담기 - 클래스의 포함관계로 구현하기
# 도대체 클래스를 왜 만드는 건지 대답할 줄 알아야 해~!

class Fridge:
    isOpened = False # 냉장고문 개폐여부
    foods = []
    
    def open(self):
        self.isOpend = True
        print('open the Fridge door')
        
    def put(self, thing):
        if self.isOpened: #isOpend == true 일때
            self.foods.append(thing) #포함관계
            print('store the food in Fridge')
            self.food_list()
        else :
            print('the Fridge door is closed.')
            
    def close(self):
        self.isOpend = False
        print('close the Fridge door')
        
    def food_list(self): #음식물 확인
        for f in self.foods:
            print('-')
        print()
        
class FoodData:
    def __init__(self, name, expiry_date):
        self.name = name
        self.expiry_date=expiry_date
        
if __name__ == '__main__':
    f = Fridge()
    
    apple = FoodData('apple', '2022-10-15')
    f.put(apple) #Fridge 의 foods 로 들어감.
    f.open()
    f.put(apple)
    f.close()
    print()
    cola=FoodData('cola', '2023-10-25')
    f.open()
    f.put(cola)
    f.close()

print()    
print('-------------------------------------------')
print()