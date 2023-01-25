from product.domain.repositories import ProductRepository, FoodFactoryDishRepository
from product.infrastructure.http_food_factory_dish_repository import HttpFoodFactoryDishRepository
from product.infrastructure.sql_product_repository import SqlProductRepository
from shared.db import database

product_repository: ProductRepository = SqlProductRepository(database)
food_factory_product_repository: FoodFactoryDishRepository = HttpFoodFactoryDishRepository()
