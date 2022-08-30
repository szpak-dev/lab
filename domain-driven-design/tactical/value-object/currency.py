class Currency:
    _iso_codes = ['EUR', 'USD']

    def __init__(self, iso_code):
        if iso_code not in self._iso_codes:
            raise Exception('Unknown currency')

        self._iso_code = iso_code

    def is_equal_to(self, currency):
        return currency.get_iso_code() == self._iso_code

    def get_iso_code(self):
        return self._iso_code
