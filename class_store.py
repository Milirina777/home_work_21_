from abc import ABC

from class_storage import Storage


class Store(Storage, ABC):
    _items = {
        "лапша БП": 35,
        "рис БП": 15,
        "кофе": 25,
        "том-ям": 10,
        "моти": 40,
    }
    _capacity = 50

    @classmethod
    def add(cls, the_name, quantity):
        """Увеличивает запас items с учетом лимита capacity"""
        if cls._capacity >= quantity:
            if the_name in cls._items:
                cls._items[the_name] += quantity
                cls._capacity -= quantity
            else:
                cls._items[the_name] = quantity
                cls._capacity -= quantity
        else:
            print('Недостаточно места на складе')

    @classmethod
    def remove(cls, name, quantity):
        """Транспортирует товары со склада"""
        if name not in cls._items:
            print(f'Нет товара {name} на складе')
        elif cls._items.get(name) < quantity:
            print(f'Не достаточно товара {name} на складе')
        elif name in cls._items:
            cls._items[name] -= quantity
            cls._capacity += quantity
            if cls._items[name] == 0:
                del cls._items[name]

    @classmethod
    def get_free_space(cls):
        """Возвращает количество свободных мест на складе"""
        return cls._capacity

    @classmethod
    def get_items(cls):
        """Возвращает наименование и количество товаров на складе"""
        return cls._items

    @classmethod
    def unique_items_count(cls):
        """Возвращает количество уникальных товаров на складе"""
        return len(set(cls._items))
