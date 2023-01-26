from product.domain.entities import Product
from product.domain.erorrs import ProductCannotBeCreated, ProductNotFound, ProductCannotBeUpdated
from product.domain.event_listeners import FoodFactoryDishListener
from product.domain.models import FoodFactoryDish
from product.domain.repositories import FoodFactoryDishRepository, ProductRepository


class AmqpFoodFactoryDishListener(FoodFactoryDishListener):
    def __init__(self, dish_repository: FoodFactoryDishRepository, product_repository: ProductRepository):
        self._dish_repository = dish_repository
        self._product_repository = product_repository

    async def on_dish_created(self, dish_id: int) -> None:
        dish = await self._get_dish(dish_id)
        await self._assert_product_can_be_created(dish_id)
        await self._update_product_properties(Product(), dish)

    async def on_dish_updated(self, dish_id: int) -> None:
        dish = await self._get_dish(dish_id)
        existing_product = await self._get_updatable_product(dish_id)
        await self._update_product_properties(existing_product, dish)

    async def on_dish_removed(self, dish_id: int) -> None:
        pass

    async def _assert_product_can_be_created(self, dish_id: int) -> None:
        try:
            await self._product_repository.get_by_dish_id(dish_id)
            raise ProductCannotBeCreated
        except ProductNotFound:
            pass

    async def _get_updatable_product(self, dish_id: int) -> Product:
        try:
            return await self._product_repository.get_by_dish_id(dish_id)
        except ProductNotFound:
            raise ProductCannotBeUpdated

    async def _get_dish(self, dish_id: int) -> FoodFactoryDish:
        return await (anext(self._dish_repository.get_by_dish_id(dish_id)))

    async def _update_product_properties(self, product: Product, dish: FoodFactoryDish) -> None:
        product.dish_id = dish.id
        product.name = dish.name
        product.description = dish.description
        product.price = 1.22
        product.calories_per_100g = 123
        product.calories_per_serving = 444
        product.ingredients = dish.ingredients_text
        product.weight = 400

        await self._product_repository.save(product)
