from order_repository import OrderRepository


class EveryThirdOrderFreeDelivery:
    order_repository = OrderRepository()

    def may_free_delivery_be_granted(self, user_id):
        last_two_orders = self.order_repository.get_last_two_orders(user_id)

        if len(last_two_orders) < 2:
            return False

        have_special_items = self._orders_have_item('item_id', last_two_orders)
        have_required_minimum_prices = self._orders_have_price_bigger_then(100, last_two_orders)

        return have_special_items and have_required_minimum_prices

    @staticmethod
    def _orders_have_item(item_id, orders):
        return True

    @staticmethod
    def _orders_have_price_bigger_then(self, value, orders):
        return True
