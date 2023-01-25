from product.domain.models import FoodFactoryDish
from product.domain.repositories import FoodFactoryDishRepository


class HttpFoodFactoryDishRepository(FoodFactoryDishRepository):
    async def get_by_id(self, product_id: int) -> FoodFactoryDish:
        ...
