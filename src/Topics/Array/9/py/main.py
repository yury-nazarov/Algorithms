# Time  complexity: O(n) - т.к. один раз итерируемся по массиву
# Space complexity: O(1) - используем дополнительную переменную monotonic
# Solution: Добовляем дополнительную переменную monotonic в которой содержатся значения от 0-2,
#           означающие текущее состояние последовательности (значения равны, возрастает или убывает)
#           На каждом шаге, когда последовательность возрастает или убывает, проверяем что monotonic
#           не в отличном от текущей систуации состоянии. Если в отличном - возвращаем False,
#           т.к. последовательность более не является монотонной.


# Для запуска дебага изменить на True
DEBUG_FLAG = False


def main(nums: [int]) -> bool:
    # 0 - равны
    # 1 - возростает
    # 2 - убывает
    monotonic = 0

    for i in range(len(nums) - 1):
        if nums[i] == nums[i+1]:
            debug(f"Значения равны")

        elif nums[i] < nums[i+1]:
            debug(f"Последовательность возрастает, monotonic: {monotonic}")
            if monotonic == 2:
                return False
            monotonic = 1

        elif nums[i] > nums[i+1]:
            debug(f"Последовательность убывает, monotonic: {monotonic}")
            if monotonic == 1:
                return False
            monotonic = 2

    return True


def debug(mgs: str):
    if DEBUG_FLAG:
        print(mgs)


if __name__ == '__main__':
    arr = [1, 3, 2]
    print(main(arr))