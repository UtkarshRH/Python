'''
Create a class called Order Which store item and its price 
Use Dunder Function  __gt__() to convey that :
    Order1>Order2 if price of order1 > price of order2
'''

class Order:
    def __init__(self,item,price) :
        self.item = item
        self.price = price
    
    def __gt__(self,odr2):   # Here we create the dunder function using the dumder function 
        return self.price > odr2.price
    

odr1 = Order("Chips",20)
odr2 = Order("tea",10)

print(odr1 > odr2)