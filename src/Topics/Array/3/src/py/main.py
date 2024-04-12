
# Time complexity:  O(n) - т.к. итеритуемсяпо всему массиву
# Space complexity: O(1) - т.к. выделяем память только под переменную count
def main(flowerbed: [int], n: int) -> bool:
    # Проверяем корнер кейсы
    if len(flowerbed) == 0:
        return False

    # для обработки корнер кейсов, когда мы можем высадить цветок в первую или последнюю не занятую клумбу
    flowerbed.insert(0, 0)
    flowerbed.append(0)
    count = 0
    # Итерируемся по клумбам, за исключением 0 и последней, что бы не попасть в out of range
    for i in range(1, len(flowerbed)-1):
        # Что бы посадить цветок, нам нужны три свободные подряд клумбы
        if flowerbed[i-1] == flowerbed[i] == flowerbed[i+1] == 0:
            # Высаживаем цветок в свободную клумбу
            flowerbed[i] = 1
            # Увеличиваем счетчик
            count += 1
    if count >= n:
        return True
    else:
        return False


if __name__ == '__main__':
    arr = [0, 0, 1, 0, 1]
    n = 1
    print(main(arr, n))

