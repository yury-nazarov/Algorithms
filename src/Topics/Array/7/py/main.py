# Time  complexity: O(n) т.к. итерируемся по всему входящему массиву
# Space complexity: O(1) т.к. используем 4 дополнительные переменные для хранения значений

def main(nums):
    # Для запуска дебага изменить на True
    dflag = False

    # Т.к. даже если ве числа равны в последовательности, это будет 1
    count = 1
    max_subseq = 0

    for i in range(len(nums)-1):
        if nums[i] < nums[i+1]:
            count += 1
            debug(dflag, f"Последовательность возрастает т.к. {nums[i]} < {nums[i+1]}")
        else:
            if count > max_subseq:
                max_subseq = count
                debug(dflag, f"Записываем наибольшую последовательность в max_subseq: {max_subseq}")
            count = 1
            debug(dflag, f"Сбрасываем счетчик, т.к. {nums[i]} >= {nums[i + 1]}")

    # Если последовательность только возрастает, записываем максимум после проверки всех вариантов
    if count > max_subseq:
        max_subseq = count
        debug(dflag, f"Переписываем максимальный счетчик, т.к. {count} > {max_subseq}")
    return max_subseq


def debug(flag: bool, mgs: str):
    if flag:
        print(mgs)



if __name__ == '__main__':
    arr = [1, 3, 5, 4, 2, 3, 4, 5]
    print(main(arr))