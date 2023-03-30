class Request:
    def __init__(self, string):
        self._from = None  # откуда везем (строка)
        self._to = None  # куда везем (строка)
        self._amount = None  # количество (товара)
        self._product = None  # наименование (товара)
        self.string = string  # поступающая строка

        # определяем что, сколько, откуда и куда везем
        try:
            data = self.string.split(' ')
            for i in data:
                if i.isdigit():
                    self._amount = (int(i))
                    self._product = (data[data.index(i) + 1])
                if i.lower() == 'из' or i.lower() == 'со':
                    if data[data.index(i) + 1] in ['склад', 'склада']:
                        self._from = 'склад'
                        self._to = 'магазин'
                    elif data[data.index(i) + 1] in ['магазин', 'магазина']:
                        self._to = 'магазин'
                        self._from = 'склад'

                elif i.lower() == 'в' or i.lower() == 'на':
                    if data[data.index(i) + 1] in ['склад', 'склада']:
                        self._to = 'склад'
                        self._from = 'магазин'
                    elif data[data.index(i) + 1] in ['магазин', 'магазина']:
                        self._from = 'склад'
                        self._to = 'магазин'
        except Exception as e:
            raise print(e, 'ошибка ввода данных')

    @property
    def from_(self):
        """Возвращает пункт отправление"""
        return self._from

    @from_.setter
    def from_(self, new_from):
        """Определяет пункт отправления"""
        self._from = new_from

    @property
    def to(self):
        """Возвращает пункт назначения"""
        return self._to

    @to.setter
    def to(self, new_to):
        """Определяет новый пункт назначения"""
        self._to = new_to

    @property
    def amount(self):
        """Возвращает количество товара"""
        return self._amount

    @amount.setter
    def amount(self, new_amount):
        """Определяет новое количество товара"""
        self._amount = new_amount

    @property
    def product(self):
        """Возвращает наименование товара"""
        return self._product

    @product.setter
    def product(self, new_product):
        """Определяет новое наименование товара"""
        self._product = new_product
