from courier import print_store, print_shop, to_store, to_shop
from class_request import Request

def main():
    print("Здравствуйте! Давайте начнем!")

    while True:
        print_store()
        print_shop()

        user_input = input(
            "Введите запрос в формате 'Доставить 3 печеньки из склада в магазин'\n"
            "Введите 'стоп' или 'stop', если хотите закончить:\n"
        )
        if user_input in ("stop", "стоп"):
            break

        to = Request(user_input).to
        from_ = Request(user_input).from_
        amount = Request(user_input).amount
        product = Request(user_input).product
        if to == 'склад':
            to_store(product=product, amount=amount)
        else:
            to_shop(amount=amount, product=product)


if __name__ == "__main__":
    main()
