# Создаем функции для с вычислениями
def plus(a, b): return a + b


def minus(a, b): return a - b


def divide(a, b): return a / b


def multiply(a, b): return a * b


# Создаем класс
class Calculator:
    answer = None  # Статическое свойство для вывода истории

    def __init__(self, num_1, num_2, sign):  # Инициализируем наши динамические свойства
        self.num_1 = num_1
        self.num_2 = num_2
        self.sign = sign

    def calc(self):  # Создаем метод с вычислениями
        self.answer = None
        try:
            if self.sign == "+":
                self.answer = plus(self.num_1, self.num_2)
                print(f"Ваш ответ: {self.answer}")
            elif self.sign == "-":
                self.answer = minus(self.num_1, self.num_2)
                print(f"Ваш ответ: {self.answer}")
            elif self.sign == "/":
                self.answer = divide(self.num_1, self.num_2)
                print(f"Ваш ответ: {self.answer}")
            elif self.sign == "*":
                self.answer = multiply(self.num_1, self.num_2)
                print(f"Ваш ответ: {self.answer}")
            else:
                print("Такого знака нет в этом калькуляторе!")

        except ZeroDivisionError:
            print("На ноль делить нельзя!")


# 2 переменные для эстетически красивого вывода истории
HISTORY = []
COUNTER = 0
while True:
    ask = input("                    Калькулятор                 _ □ х\n"
                "Запуск - 1;\n"
                "История - 2;\n"
                "Выход - 0.\n")
    if ask == "1":
        # Создаем обьект
        calc_obj = Calculator(int(input("Введите число: ")),
                              int(input("Введите второе число: ")), input("Введите знак: "))
        # Вызываем метод нашего класса
        calc_obj.calc()
        # Заносим в строку наши значения
        x = str(calc_obj.num_1) + " " + calc_obj.sign + " " + str(calc_obj.num_2) + " = " + str(calc_obj.answer)
        HISTORY.append(x)  # Добавляем его в наш список истории

    elif ask == "2":  # Проходимся по списку и выводим историю наших вычислений
        print("------------------------------")
        for i in HISTORY:
            COUNTER += 1
            print(f"{COUNTER}. {i}")
        print("------------------------------")

    elif ask == "0":
        print("---------ВЫХОД----------")
        break
