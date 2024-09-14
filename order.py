from coffee import Coffee
from customer import Customer


class Order:
    all_coffees = []
    all_customers = []

    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price
        Order.all_coffees.append(coffee)
        Order.all_customers.append(customer)

    @property
    def customer(self):
        return self._customer

    @customer.setter
    def customer(self, value):
        if not isinstance(value, Customer):
            raise TypeError("customer must be an instance of Customer class")
        self._customer = value

    @property
    def coffee(self):
        return self._coffee

    @coffee.setter
    def coffee(self, value):
        if not isinstance(value, Coffee):
            raise TypeError("coffee must be an instance of Coffee class")
        self._coffee = value

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if not isinstance(value, float) or value < 1.0 or value > 10.0:
            raise TypeError("price must be a float between 1.0 and 10.0")
        self._price = value

    @classmethod
    def most_aficionado(cls, coffee):
        from order import Order

        customer_spending = {}

        for order in Order.all_customers:
            if order.coffee == coffee:
                if order.customer not in customer_spending:
                    customer_spending[order.customer] = 0
                customer_spending[order.customer] += order.price

        if not customer_spending:
            return None

        most_aficionado = max(
            customer_spending, key=lambda customer: customer_spending[customer]
        )
        return most_aficionado
