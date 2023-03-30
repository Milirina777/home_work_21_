from abc import ABC, abstractmethod

class Storage(ABC):
    """Абстрактный класс с методами и полями"""

    @property
    @abstractmethod
    def _items(self):
        pass

    @property
    @abstractmethod
    def _capacity(self):
        pass

    @abstractmethod
    def add(self, the_name, quantity):
        """Увеличивает запас items"""
        pass

    @abstractmethod
    def remove(self, the_name, quantity):
        """Уменьшает запас items"""
        pass

    @abstractmethod
    def get_free_space(self):
        """Возвращает количество свободных мест"""
        pass

    @abstractmethod
    def get_items(self):
        """Возвращает содержание склада в словаре {товар: количество}"""
        pass

    @abstractmethod
    def unique_items_count(self):
        """Возвращает количество уникальных товаров"""
        pass
