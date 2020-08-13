def main(data) -> None:
    arr: list = list(map(int, data.split()))
    print(' '.join(list(map(str, merge_sort(arr)))))


def merge_sort(arr: list) -> list:
    """ 
    1. На вход принимает не отсортированный массив
    2. рекурсивно вызывает сам себя для левой и правой половины не отсортированного массива, 
       пока не получет массив из 1 элемента
    3. Возвращает из рекурсивного вызова функцию слияния и сортировки двух половин массива
    """
    if len(arr) <= 1:
        return arr
    else:
        left: list = arr[:len(arr)//2]
        right: list = arr[len(arr)//2:]
    return merge(merge_sort(left), merge_sort(right))


def merge(left: list, right: list) -> list:
    """ Сливает и сортирует два не остсортированных
    массива left, right в тритий отсортированный """
    res: list = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1
    res += left[i:] + right[j:]
    return res


if __name__ == '__main__':
    main(input())
