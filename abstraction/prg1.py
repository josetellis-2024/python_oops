from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def pay(self,amount):
        pass

class CreditCardPayment(Payment):
    def pay(self,amount):
        print(f"Paid {amount} using Credit Card")
class UpiPayment(Payment):
    def pay(self,amount):
        print(f"Paid {amount} using UPI")
payment1=CreditCardPayment()
payment1.pay(1000)



payment2=UpiPayment()
payment2.pay(500)
# 100%    