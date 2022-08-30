from aggregate_children import Cart


class CartVersioned(Cart):
    def __init__(self):
        super().__init__()
        self._version = 0

    def get_version(self):
        return self._version
