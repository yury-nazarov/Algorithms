# Time  complexity: O(n) - т.к. итеритуемся по строке в худшем случае один раз
# Space complexity: O(1) - Т.к. используем две дополнительные переменные

def main(s: str) -> bool:
    # Для запуска дебага изменить на True
    dflag = False

    # Если один из счетчиков будет раввен 0 - завершаем выполнение
    a_count = 2
    l_count = 3

    # итерируемся по всем элементам кроме последнего,
    # т.к. будем сравнивать элементы между собой и на последнем элементе
    # попадем в out of range при i+1
    for i in range(len(s)):
        if a_count == 0 or l_count == 0:
            return False

        # Счетчик отсутствий
        if s[i] == "A":
            a_count -= 1

        # Счетчик опозданий
        # Если есть три пропуска подряд и длина строки позволяет связть такой слайс
        if len(s) - i >= l_count and s[i] == s[i+1] == s[i+2] == "L":
            l_count -= 3

    # Если счетчик стал равен 0 на последней итерации
    if a_count == 0 or l_count == 0:
        return False

    return True


def debug(flag: bool, mgs: str):
    if flag:
        print(mgs)
