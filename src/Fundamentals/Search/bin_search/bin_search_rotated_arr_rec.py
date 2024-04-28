"""

Бинарный поиск в сдвинутом списке
Возвращает индекс искомой позиции или -1 если элемент не найден


РАБОЧИЙ ВАРИАНТ

"""

def main(fn):
    with open(fn, 'r') as f:
        data = f.read().split('\n')
        x = int(data[1])
        arr = list(map(int, data[2].split(' ')))
        print(bin_search(arr, 0, len(arr)-1, x))


def bin_search(arr: list, left: int, right: int, x: int):
    m = (left+right)//2

    if arr[m] == x:
        return m

    if right < left:
        return -1

    if len(arr[left:right+1]) == 2:
        index: int = bin_search(arr, left, m, x)
        if index == -1:
            index = bin_search(arr, m+1, right, x)
        return index

    elif arr[left] < arr[m]:
        if x >= arr[left] and x < arr[m]:
            return bin_search(arr, left, m, x)
        else:
            return bin_search(arr, m+1, right, x)

    elif arr[left] > arr[m]:
        if x > arr[m] and x <= arr[right]:
            return bin_search(arr, m+1, right, x)
        else:
            return bin_search(arr, left, m, x)

    else:
        return -1


if __name__ == '__main__':
    main('input.txt')