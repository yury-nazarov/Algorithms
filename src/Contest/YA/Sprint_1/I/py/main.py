
# TODO:
# https://streletzcoder.ru/yavlyaetsya-li-chislo-stepenyu-drugogo-chisla/
# https://www.cyberforum.ru/python-beginners/thread1808719.html
# Это условие того, что n НЕ является степенью 2. Для его понимания рассмотрите примеры, задавая n в двоичном виде.
# Побитовое И чисел n и n - 1


# Проверить, является ли число степенью 4
# Если да вывести True, иначе False
def main():
    is_power_four = is_power("../data/input_1.txt")
    print(is_power_four)


def is_power(path) -> bool:
    n = file_open(path)
    i = 4
    if n == 1:
        return True
    while i <= n:
        if i == n:
            return True
        i *= 4
    return False

# TODO: Подумать над этим вариантом
# def is_power(n: int) -> bool:
#     if n < 4:
#         return False
#     if n & (n - 1):
#         return False
#     else:
#         return True


def file_open(path) -> int:
    with open(path) as f:
        return int(f.readline())


if __name__ == '__main__':
    main()