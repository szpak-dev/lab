from shared.shared import ValueObject


class ProductId(ValueObject):
    def __init__(self, product_id: int):
        self._product_id = product_id

    @property
    def value(self) -> int:
        return self._product_id
