""" Counting Sort / Сортировка подсчетом """


def counting_sort(arr):
    # Создаем массив из нулей, +1 т.к. исходный массив начинается с 0
    count = [0 for _ in range(max(arr)+1)]  # [0, 0, 0, 0]

    for i in range(len(arr)):
        # Увеличиваем счетчик для нужного индекса
        count[arr[i]] += 1

    result = []

    # Добавляем в финальный массив кол-во каждого числа,
    # сколько мы насчитали в счетчике
    for i in range(len(count)):
        for _ in range(count[i]):
            result.append(i)

    print(result)


if __name__ == '__main__':
    counting_sort([2, 1, 1, 2, 3, 5, 5, 2, 1, 10])

