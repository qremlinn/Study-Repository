def filter_decore(fn):
    def wrapper():
        fn()
        print(f"--------{fn.__name__}--------")

    return wrapper


@filter_decore
def eng_filter():
    string = input("Введите строку: ")
    sogl = 0
    glas = 0

    for i in string:
        if i.isalpha():
            if i in "AEIOUYaeiouy":
                glas += 1
            else:
                sogl += 1

    print(f"Согласных букв в этой строке: {sogl}")
    print(f"Гласных букв в этой строке: {glas}")


@filter_decore
def rus_filter():
    string = input("Введите строку: ")
    sogl = 0
    glas = 0

    for i in string:
        if i.isalpha():
            if i in "БВГДЖЗЙКЛМНПРСТФХЦЧШЩбвгджзйклмнпрстфхцчшщ":
                sogl += 1
            else:
                glas += 1

    print(f"Согласных букв в этой строке: {sogl}")
    print(f"Гласных букв в этой строке: {glas}")


def filter_decore(fn):
    def wrapper():
        fn()
        print(f"--------{fn.__name__}--------")

    return wrapper


while True:
    ask = input("Какой язык хотите разобрать?\n"
                "eng - английский\n"
                "rus - русский\n"
                "Чтобы выйти введите 0\n")

    if ask == "eng":
        eng_filter()
    elif ask == "rus":
        rus_filter()
    elif ask == "0":
        break
    else:
        print("Посмотрите еще раз варианты ввода...")
        print("-------------------------------------")
