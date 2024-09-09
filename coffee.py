from order import Order


class Coffee:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or len(value) < 3:
            raise TypeError("Enter a valid coffee name")
        self._name = value

    def orders(self):
        return [order for order in Order.all_coffees if order.coffee == self]

    def customers(self):
        return list(
            {order.customer for order in Order.all_coffees if order.coffee == self}
        )

    def num_orders(self):
        return len(self.orders())

    def average_price(self):
        return sum([order.price for order in self.orders()]) / len(self.orders())
