from order import Order


class Customer:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) and len(value) < 1 or len(value) > 15:
            raise TypeError("Name must be a string between 1 and 15 characters")
        self._name = value

    def orders(self):
        return [order for order in Order.all_customers if order.customer == self]

    def coffees(self):
        return list(
            {order.coffee for order in Order.all_customers if order.customer == self}
        )

    def create_order(self, coffee, price):
        return Order(self, coffee, price)
