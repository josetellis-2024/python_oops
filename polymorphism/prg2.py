class Order:
    def __init__(self,order_id):
        self.__order_id=order_id
        
class Customer(Order):
    def __init__(self,order_id):        
        super().__init__(order_id)
        print("Customer class constructor")

c=Customer(1000)
print(Customer.mro())



