class Product:

    __price = 0.00
    __item_id = 1

    def __init__(self, price, item_id):
        self.__price = price
        self.__item_id = item_id

    def __str__(self):
        return "ID: {}, Quantity: {}, Price: {}".format(self.__item_id, self.__price)

    def get_price(self):
        return self.__price

    def get_item_id(self):
        return self.__item_id

