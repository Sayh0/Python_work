from abc import *

class Bike(metaclass = ABCMeta):
    def __init__(self, name):
        self.name = name
    @abstractmethod
    def pay(self):
        pass
    @abstractmethod
    def display(self):
        pass
    def name_print(self):
        print(self.name + '님', end='')
        
class Bicycle(Bike):
    def __init__(self, name, wheel, price):
        Bike.__init__(self, name)   
        self.wheel = wheel;
        self.price = price;
    def pay(self):
        return self.wheel * self.price
    def display(self):
        self.name_print();
        print(' 자전거 바퀴 가격 총액은 ' + str(self.pay()) +'원입니다.')
gildong = Bicycle('길동', 2, 50000);
gildong.display();