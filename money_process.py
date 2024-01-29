class MoneyMechine:
    CURRENCY='TK '
    COIN_VALUES={
        'quarters':100,
        'dimes':50,
        'nickless':50,
    }
    def __init__(self):
        self.profit=0
        self.money_received=0
    def reports(self):
        '''Prints the current profit'''
        print(f"Money: {self.CURRENCY} {self.profit }")
        
    def process_coins(self):
        print("Please complete your payment :")
        for coin in self.COIN_VALUES:
            self.money_received +=int(input(f'How many {coin} ')) * self.COIN_VALUES[coin]
        return self.money_received
    def make_payment(self,Cost):
        self.process_coins()
        if self.money_received>=Cost:
            change=round(self.money_received-Cost,2)
            print(f'here is {self.CURRENCY}{change} in change')
            self.profit +=Cost
            return True
        else:
            print('Sorry there is not enough money')
            self.money_received=0
            return False

