def selection_sort(arr):
    """
    Сортировка выбором по убыванию
    [-3, -1, 2, -2, 1, 3] => [3, 2, 1, -1, -2, -3]
    """
    for i in range(len(arr)-1):
        need_replace = False
        max_elem = arr[i]
        for j in range(i, len(arr)):
            if arr[j] > max_elem:
                need_replace = True
                max_elem = arr[j]
                max_pos = j
        if need_replace:
            tmp = arr[i]
            arr[i] = max_elem
            arr[max_pos] = tmp
    return arr


if __name__ == '__main__':
    result = selection_sort([-3, -1, 2, -2, 1, 3])
    print(result)

