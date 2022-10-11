class Machine:
    cupCount = 1
    
    def __init__(self, coin, cupCount):
        self.coinIn = CoinIn()
        self.coinIn.coin = coin
        self.cupCount = cupCount
    
    def showData(self):
        msg = self.coinIn.culc(self.cupCount)
        print(msg)


class CoinIn:
    coin = 0
    change = 0
    
    def culc(self, cupCount):
        change = self.coin - cupCount*200
        if change >= 0:
            self.change = change
            return f'커피 {cupCount}잔과 잔돈 {self.change}원'
        return "요금 부족!!"



if __name__ == '__main__':
    coin = int(input('동전을 입력하세요 : '))
    cup = int(input('몇 잔을 원하세요 : '))
    useMuchine = Machine(coin, cup)
    useMuchine.showData()