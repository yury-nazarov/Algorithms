
# Time complexity:  O(n) - т.к. итеритуемсяпо всему массиву
# Space complexity: O(1) - т.к. выделяем память только под переменную rise
# TODO: Решение довольно наивно, можно сделать лаконичней.
def main(mountain: [int]) -> bool:
    # 0 - Начало
    # 1 - подьем
    # 2 - спуск
    rise = 0

    if len(mountain) < 2:
        return False

    for step in range(len(mountain)-1):
        # Плато или равнина не допустимы по условию задачи
        if mountain[step] == mountain[step + 1]:
            return False

        # Карьер, а не гора...
        if mountain[step] > mountain[step + 1] and rise == 0:
            return False

        # Подъем
        if mountain[step] < mountain[step + 1]:
            # Устанавливаем флаг, что мы начали подьем в гору
            if rise == 0:
                rise = 1

            # Если после спуска начался подьем - прекращаем выполнение
            if rise == 2:
                return False

        # Спуск
        if mountain[step] > mountain[step + 1]:
            # После того как начали спускатся, поднятся обратно не можем
            if rise == 1:
                rise = 2

    # Если не было спуска с горы
    if rise == 1:
        return False

    return True

