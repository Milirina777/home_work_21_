from class_shop import Shop
from class_store import Store


def to_shop(product, amount):
    """"Транспортировка товара со склада в магазин"""
    shop = Shop()
    store = Store()
    store.remove(product, amount)

    print(f"Курьер забрал {amount} {product} со склада в магазин")
    shop.add(product, amount)
    print(f"Курьер доставил {amount} {product} в в магазин")


def to_store(amount, product):
    """Возврат товара на склад отправления"""
    shop = Shop()
    store = Store()
    shop.remove(product, amount)
    print(f'Курьер взял {amount} {product} из магазина')
    store.add(product, amount)
    print(f"Курьер вернул {amount} {product} на склад")

def print_store():
    """Вывод информации о товарах на складе"""
    store = Store()
    data = store.get_items()
    print('На складе хранится:')
    for i in data:
        print(f'{data[i]} - {i}')

def print_shop():
    """Вывод информации о товарах в магазине"""
    shop = Shop()
    data = shop.get_items()
    print('В магазине хранятся:')
    for i in data:
        print(f'{data[i]} - {i}')
