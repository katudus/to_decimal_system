# Мини-проект: Перевод чисел из любой системы счисления в десятичную
from datetime import datetime

start_time = datetime.now()

NUM_16 = "0123456789ABCDEF"


def to_decimal_system(num, form):
    num = num[::-1]
    if form == 16:
        return sum(NUM_16.find(num[i]) * form**i for i in range(len(num)))
    return sum(int(n) * form**i for i, n in enumerate(num))


def from_decimal_system(num, form):
    num = int(num)
    res = ""
    while num != 0:
        res += NUM_16[num % form]
        num //= form
    return res[::-1]


print("Перевод чисел из любой системы счисления (2-9, 16) в десятичную и наоборот.")

while True:
    operation_from_10 = input("\nЕсли перевод из 10 системы в другую постaвьте '+':\n")
    if operation_from_10 == "+":
        system = input("Введите будущую систему счисления:\n")
    else:
        system = input("Введите исходную систему счисления:\n")
    while not system.isdigit():
        system = input("Попробуйте еще раз:\n")
    system = int(system)

    number = input("Введите число:\n").upper()

    if operation_from_10 == "+":
        print(f"Результат:\n{from_decimal_system(number, system)}")
    else:
        print(f"Результат:\n{to_decimal_system(number, system)}")

    end_time = datetime.now()
    print(
        "Duration: {}".format(end_time - start_time)
    )  # Вывод затраченного времени на выполнение вычислений

    if input("\nНажмите '+' чтобы завершить программу.\n") == "+":
        break


# #def search_system():
#     return [
#         a
#         for a in range(10)
#         if 8 * a**1 + 8 * a**0
#         == ((3 * a**1) + (2 * a**0))
#         + ((2 * a**1) + (2 * a**0))
#         + ((1 * a**1) + (6 * a**0))
#         + ((1 * a**1) + (7 * a**0))
#     ]

# #print(search_system())
