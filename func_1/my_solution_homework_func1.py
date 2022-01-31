def plus(a, b): return a + b


def minus(a, b): return a - b


def divide(a, b): return a / b


def multiply(a, b): return a * b


def calc(a, b):
    sign = input("Введите знак: ")
    try:
        if sign == "+":
            print(plus(a, b))
        elif sign == "-":
            print(minus(a, b))
        elif sign == "/":
            print(divide(a, b))
        elif sign == "*":
            print(multiply(a, b))
        else:
            print("Такого знака нет в этом калькуляторе!")
    except ZeroDivisionError:
        print("На ноль делить нельзя!")


calc(int(input("Введите 1-е число: ")), int(input("Введите 2-е число: ")))
