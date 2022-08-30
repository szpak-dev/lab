class Money:
    def __init__(self, amount, currency):
        if amount <= 0:
            raise Exception('Wrong value')

        self._amount = amount
        self._currency = currency

    def is_equal_to(self, money):
        return money.get_amount() == self._amount and money.get_currency() == self._currency

    def get_amount(self):
        return self._amount

    def get_currency(self):
        return self._currency
