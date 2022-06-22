# Сделайте функцию, которая будет печатать
# читаемое имя переданной ей функции и ее аргументов.
# Вызовите ее для трех функций ниже в цикле
# Подсказка: Имя функции можно получить с помощью func.__name__



def get_name_func(name_func):
    return name_func.__name__


def write(names_func, **kwargs):
    for name_func in names_func:
        print(name_func.replace('_', ' ').capitalize())
    print(kwargs.keys())




def open_browser():
    return get_name_func(open_browser)


def go_to_companyname_homepage():
    return get_name_func(go_to_companyname_homepage)


def find_registration_button_on_login_page():
    return get_name_func(find_registration_button_on_login_page)


call_funcs = open_browser(), go_to_companyname_homepage(), find_registration_button_on_login_page()
write(call_funcs)