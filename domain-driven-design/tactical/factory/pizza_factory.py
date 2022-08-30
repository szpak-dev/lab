from pizza import Pizza, Topping, prices


class PizzaFactory:
    @staticmethod
    def build_margherita(size):
        topping_price = prices[size] / 4
        toppings = [Topping('cheese', topping_price)]

        return Pizza(size, 'tomato', False, toppings)

    @staticmethod
    def build_tuna(size, double_cheese):
        topping_price = prices[size] / 4

        toppings = [
            Topping('cheese', topping_price),
            Topping('tuna', topping_price),
            Topping('olives', topping_price),
            Topping('onion', topping_price),
        ]

        if size == 'big':
            double_cheese = True
            toppings.append(Topping('onion', 0))

        return Pizza(size, 'tomato', double_cheese, toppings)
