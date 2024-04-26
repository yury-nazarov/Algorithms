

# Time complexity:  O(n) - т.к. итеритуемсяпо всему массиву
# Space complexity: O(n) - т.к. выделяем память под новый список,
#                               который в худшем случае может быть эквивалентен исходному массиву.
def main(nums: [int]) -> [str]:
    result = []

    # Обрабатываем корнер кейсы
    if len(nums) == 1:
        item = str(nums[0])
        result.append(item)
        return result

    # Что бы не попасть в out of index
    nums.append(0)

    count = 0

    for i in range(len(nums)-1):
        # Если сумма текущего элемента + 1 эквивалентна следующему элементу,
        # считаем что значения последовательно возрастают и просто увеличиваем счетчик
        if nums[i] + 1 == nums[i + 1]:
            count += 1
        else:
            # В противном случае записываем результат в зависимости от диапазона возрастающей последовательности
            if count == 0:
                record = f"{nums[i]}"
            else:
                record = f"{nums[i - count]}->{nums[i]}"
            result.append(record)
            count = 0

    return result


if __name__ == '__main__':
    nums = [-1]
    print(main(nums))