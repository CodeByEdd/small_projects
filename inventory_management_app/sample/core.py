from .inventory_class import Inventory


def run_app():
    cup = Inventory(2, 1234, 10)
    print(cup.get_inventory_quantity())
    print(cup.calculate_total_inventory_price())

if __name__ == '__main__':
    run_app()