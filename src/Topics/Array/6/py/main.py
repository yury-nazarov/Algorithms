
# Time  complexity: O(n) - т.к. итеритуемся по массиву
# Space complexity: O(n) - т.к. в результате собираем дополнительный массив
#                          (хотя в некоторых кейсах, это не считатется за дополнительную сложность)

def main(candies: [int], extra_candies: int) -> [bool]:
    result: [bool] = []

    # Ребенок даже с дополнительными конфетами, не может соревноватся с одним жиробасиком
    max_candies = max(candies)

    for i in range(len(candies)):
        item = candies[i] + extra_candies
        if item < max_candies:
            result.append(False)
        else:
            result.append(True)

    return result
