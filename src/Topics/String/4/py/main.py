# Time  complexity: O(n) - т.к. в худшем случае, придется итерироватся по всей строке
# Space complexity: O(1) - т.к. используем несколько дополнительных переменных

def main(s: str) -> int:
    # Для запуска дебага изменить на True
    dflag = False

    index = len(s)
    last_word_count = 0

    # 0 - пробел в конце
    # 1 - началось слово
    # 2 - пробел после того как началось слово
    flag = 0

    while index > 0:
        index -= 1

        # Завершаем выполнение приложения
        if flag == 2:
            debug(dflag, f"10) flag == 2 (реальное значение: {flag}). last_word_count: {last_word_count}. "
                         f"Завершаем выполнение приложения")
            break

        # Конец строки состоит из пробелов
        if s[index] == " " and flag == 0:
            debug(dflag, f"9) Обрабатываем пробел в конце строки: index: {index}, "
                         f"s[index]: -->{s[index]}<--, "
                         f"flag: {flag}, "
                         f"last_word_count: {last_word_count}")
            continue

        # Последнее слово закончилось
        if s[index] == " " and flag == 1:
            flag = 2
            debug(dflag, f"9) Последнее слово закончилось: "
                         f"flag: {flag}, "
                         f"last_word_count: {last_word_count}")
            break

        # Последнее  слово в строке
        debug(dflag, f"1) Считаем символ для последнего слова: index: {index}, "
                     f"s[index]: -->{s[index]}<--, "
                     f"flag: {flag}, "
                     f"last_word_count: {last_word_count}")

        flag = 1
        last_word_count += 1
        debug(dflag, f"Увеличиваем значение last_word_count: {last_word_count}")

    return last_word_count


# Альтернативный вариант решения
# Time  complexity: O(n) - т.к. в худшем случае, придется итерироватся по всей строке
# Space complexity: O(n) - т.к. split вернет дополнительную структуру - список, равный длине слова.

def v1(s) -> int:
    # Для запуска дебага изменить на True
    dflag = False


    # O(n)
    s = s.rstrip()

    num = s.split()[-1]
    debug(dflag, s)

    return len(num)


def debug(flag: bool, mgs: str):
    if flag:
        print(mgs)

