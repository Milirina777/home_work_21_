from class_storage import Storage
from abc import ABC


class Shop(Storage, ABC):
    _items = {
        "лапша БП": 5,
        "рис БП": 10,
        "кофе": 2,
        "том-ям": 1,
    }
    _capacity = 20

    @classmethod
    def add(cls, name, count):
        """Увеличивает запас items с учетом лимита capacity"""
        if cls._capacity >= count:
            if name in cls._items:
                cls._items[name] += count
                cls._capacity -= count
            else:
                if cls.unique_items_count() < 5:
                    cls._items[name] = count
                    cls._capacity -= count
                else:
                    print('Магазин не может принять курьера - \nпревышен лимит хранимых на складе наименований товаров')
        else:
            print('Недостаточно места на складе магазина')

    @classmethod
    def remove(cls, name, count):
        """Уменьшает запас items, но не ниже 0"""
        if name not in cls._items:
            print(f'Товара: {name} нет в магазине')
        elif cls._items.get(name) < count:
            print(f'Недостаточно единиц товара - {name} на складе магазина')
        elif cls._capacity + count > 100:
            print('Склад магазина заполнен')

        elif name in cls._items:
            cls._items[name] -= count
            cls._capacity += count
            if cls._items[name] == 0:
                del cls._items[name]

    @classmethod
    def get_free_space(cls):
        """Возвращает свободное пространство на складе магазина"""
        return cls._capacity

    @classmethod
    def get_items(cls):
        """Возвращает наименование и количество товаров на складе магазина"""
        return cls._items

    @classmethod
    def unique_items_count(cls):
        """Возвращает количество уникальных товаров на складе магазина"""
        return len(set(cls._items))

