def main(data):
    arr: list = list(map(int, data.split()))
    return ' '.join(list(map(str, quick_sort(arr))))


def quick_sort(arr: list) -> list:
    """
    Алгоритм быстрой сортировки
    O(n) - асимптотика в худшем случае
    O(n) - пространственная сложность
    """

    # Базовые случаи
    if len(arr) < 2:
        return arr

    if len(arr) == 2:
        if arr[0] > arr[1]:
            tmp = arr[1]
            arr[1] = arr[0]
            arr[0] = tmp
        return arr

    # Рекурсивные случаи
    # Выбрать базовый элемент, сделать два массива c элементами <= базовый, и > базового
    base: list = [arr[0]]
    les_ot_equal: list = []
    large: list = []

    # Уже идем в историю с O(n) в худшем случае
    for i in arr[1:]:
        if i <= base[0]:
            les_ot_equal.append(i)
        else:
            large.append(i)

    loe = quick_sort(les_ot_equal)
    lar = quick_sort(large)

    return loe + base + lar


if __name__ == '__main__':
    main(input())

