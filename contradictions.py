from class_request import Request

def check_input(user_input):
    """Проверка ввода параметров от пользователя"""
    if Request(user_input).to is None:
        print('Непонятен пункт назначения. Попробуйте снова...')
    if Request(user_input).from_ is None:
        print('Непонятен пункт отправления. Введите, пожалуйста, снова...')
    if Request(user_input).amount is None:
        print('Неясно количество товара. Введите, пожалуйста снова...')
    if Request(user_input).product is None:
        print('Непонятен пункт отправления. Введите, пожалуйста снова...')
    if user_input.lower() == 'хватит':
        print('спасибо, что воспользовались услугами нашей службы доставки')
        exit()
