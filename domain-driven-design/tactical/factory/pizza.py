sizes = ['small', 'medium', 'big']
sauces = ['tomato', 'bbq']
prices = {'small': 100, 'medium': 150, 'big': 200}


class Topping:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Pizza:
    def __init__(self, size, sauce, double_cheese, toppings):
        self.size = size
        self.sauce = sauce
        self.double_cheese = double_cheese
        self.toppings = toppings

    def total_price(self):
        total = prices[self.size]
        for topping in self.toppings:
            total += topping.price

        if self.double_cheese:
            total += 50

        return total
