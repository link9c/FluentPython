import inspect
from abc import ABC, abstractmethod
from collections import namedtuple

Customer = namedtuple('Customer', 'name fidelity')


class LineItem:
    def __init__(self, product, quantity, price):
        self.product = product
        self.quantity = quantity
        self.price = price

    def total(self):
        return self.price * self.quantity


class Order:
    def __init__(self, customer, cart, promotion=None):
        self.customer = customer
        self.cart = list(cart)
        self.promotion = promotion

    def total(self):
        if not hasattr(self, '__total'):
            self.__total = sum(item.total() for item in self.cart)
        return self.__total

    def due(self):

        if self.promotion is None:
            discount = 0
        else:
            discount = self.promotion.discount(self)
        return self.total() - discount

    def __repr__(self):
        fmt = '<order total:{:.2f} due:{:.2f}>'
        return fmt.format(self.total(), self.due())


class Promotion(ABC):
    @abstractmethod
    def discount(self, order):
        """返回折扣金额"""


class FidelityPromo(Promotion):
    """积分1000活以上的顾客提供5%折扣"""

    def discount(self, order):
        return order.total() * .05 if order.customer.fidelity >= 1000 else 0


class BulkItemPromo(Promotion):
    """单个商品为20个或以上时提供10%折扣"""

    def discount(self, order):
        discount = 0
        for item in order.cart:
            if item.quantity >= 20:
                discount += item.total() * .1

        return discount


class LargeOrderPromo(Promotion):
    """订单中不同商品达到10个或以上提供7%折扣"""

    def discount(self, order):
        discount_items = {item.product for item in order.cart}
        if len(discount_items) >= 10:
            return order.total() * .07
        return 0


promos = [func for name,func in inspect.getmembers(promotions,inspect.isfunction)]

# 获取所有函数名


def best_promo(order):
    return max(promo(order) for promo in promos)

if __name__ == '__main__':
    joe = Customer('John Doe', 0)
    ann = Customer('Ann Smith', 1100)
    cart = [LineItem('banana', 4, .5),
            LineItem('apple', 10, 1.5),
            LineItem('watermello', 5, 5.0)]

    print(Order(joe, cart, FidelityPromo()))
    print(Order(ann, cart, FidelityPromo()))
    banana_cart = [LineItem('banana', 30, .5),
                   LineItem('apple', 10, 1.5)]
    print(Order(joe, banana_cart, BulkItemPromo()))

    long_order = [LineItem(str(item_code), 1, 1.0) for item_code in range(10)]
    print(Order(joe, long_order, LargeOrderPromo()))
    print(Order(joe, cart, LargeOrderPromo()))

    print(Order(joe, long_order, best_promo))
    print(Order(joe, banana_cart, best_promo))
