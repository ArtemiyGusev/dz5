# Сделайте функцию, которая будет печатать
# читаемое имя переданной ей функции и ее аргументов.
# Вызовите ее для трех функций ниже в цикле
# Подсказка: Имя функции можно получить с помощью func.__name__


def write(names_func, **kwargs):
    print(names_func.__name__.replace('_', ' ').capitalize())
    for key in kwargs.keys():
        print(key)
    print('---')


def open_browser():
    pass


def go_to_companyname_homepage():
    pass


def find_registration_button_on_login_page():
    pass


call_funcs = open_browser, go_to_companyname_homepage, find_registration_button_on_login_page
for call_func in call_funcs:
    write(call_func, arg1=4, arg2=5)
