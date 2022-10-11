from abc import *

class Employee(metaclass = ABCMeta):
    irum = "이름"
    nai = 0
    @abstractmethod
    def pay(self):
        pass
    
    @abstractmethod
    def data_print(self):
        pass
    
    def irumnai_print(self, irum, nai):
        self.irum=irum
        self.nai=nai
    
class Temporary(Employee):
    ilsu = 0
    ildang = 0
    
    def pay(self,ilsu,ildang):
        self.ilsu=ilsu
        self.ildang=ildang
    
    def data_print(self, irum, nai, ilsu, ildang):
        self.irumnai_print(irum, nai)
        self.pay(ilsu, ildang)
        print("이름 : {}, 나이 : {}, 월급 : {}".format(irum, nai, ilsu*ildang))
        
class Regular(Employee):
    salery = 0
    
    def pay(self, salery):
        self.salery=salery
        
    def data_print(self,irum, nai, salery):
        self.irumnai_print(irum, nai)
        self.pay(salery)
        print("이름 : {}, 나이 : {}, 급여 : {}".format(irum, nai, salery))

class Salesman(Regular):
    sales = 0
    commission = 0
    getMoney = 0
        
    def pay(self, sales, commission):
        self.commission=commission
        self.sales=sales
        self.getMoney=self.salery+(self.sales*self.commission)
        
    def data_print(self, irum, nai, salery, sales, commission):
        self.irumnai_print(irum, nai)
        self.pay(salery, sales, commission)
        print("이름 : {}, 나이 : {}, 수령액 : {}".format(irum, nai, self.getMoney))


t=Temporary()
t.data_print('홍길동', 25, 20, 15000)
r=Regular()
r.data_print('한국인', 27, 3500000)
s=Salesman()
s.data_print('손오공', 29, 1200000, 5000000, 0.25)


