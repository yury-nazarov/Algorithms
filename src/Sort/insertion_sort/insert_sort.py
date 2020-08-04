"""
Insertion Sort / Сортировка вставками
"""


def insertion_sort(arr):
    for i in range(1, len(arr)):

        # В new_element кладем текущую проверяемую позицию
        new_element = arr[i]
        #  Начиная с i-1
        j = i - 1

        # Все элементы, которые больше new_element
        while j >= 0 and arr[j] > new_element:
            # Сдвигаем в право на 1
            arr[j+1] = arr[j]
            # Пока не закончится обратный отсчет от i-1 до 0
            j -= 1

        # На освободившееся место записываем  new_element
        arr[j+1] = new_element
    return arr


if __name__ == '__main__':
    arr = [3, 2, 1, -1, -2, -3]
    print(insertion_sort(arr))

