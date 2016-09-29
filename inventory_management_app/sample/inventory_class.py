from .product_class import Product


class Inventory(Product):

    __total_product_quantity = 0
    __total_inventory_price = 0

    def __init__(self, price, item_id, quantity):
        Product.__init__(self, price, item_id)
        self.__total_product_quantity = quantity

    def get_inventory_price(self):
        return self.__total_inventory_price

    def get_inventory_quantity(self):
        return self.__total_product_quantity

    def calculate_total_inventory_price(self):
        return int(Product.get_price(self)) * int(self.__total_product_quantity)
