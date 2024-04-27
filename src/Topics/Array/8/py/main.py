# Time  complexity: O(n) т.к. итерируемся по массиву как минимум один раз
# Space complexity: О(n) т.к. под резуьтат создаем отдельный массив

def main(nums) -> [int]:
    # Для запуска дебага изменить на True
    dflag = False

    result = []
    priv_sum = nums[0]
    result.append(priv_sum)

    for i in range(len(nums) - 1):
        debug(dflag, f"Текущее значение priv_sum: {priv_sum} + {nums[i+1]}")
        priv_sum += nums[i+1]
        result.append(priv_sum)
    return result


def debug(flag: bool, mgs: str):
    if flag:
        print(mgs)

