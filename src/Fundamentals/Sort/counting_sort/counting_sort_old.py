def counting_sort(arr: list) -> list:
    #print('--------')
    # Диапазон
    scope = max(arr) + 1
    #print(scope)

    # Массив из нулей
    count: list = [0] * scope
    #print(count)

    # Увеличиваем
    for i in arr:
        count[i] += 1
        #print(i, count[i])

    #print(count)
    #print(arr, arr[:])
    # Удаляем изначальный массив. Зачем? Память почистить?
    arr[:] = []
    #print(arr, arr[:])
    #print('--')
    for number in range(scope):
        # Интересное решение коекатенировать массив.
        # Я не уверен что это безопасная для памяти операция.
        # т.е. в результате конкатинации будет создаватся новый объект списка.
        # Делаем из текущего элемента последовательности массив из одного элемента
        # умножаем на текущее значение массива count с этим индексом
        # Если count отличен от 0, конкатенируем полученный массив из одного элемента с arr
        arr += [number] * count[number]
        #print(arr, [number], count[number])

    return arr


if __name__ == '__main__':
    #result = counting_sort([-3, -1, 2, -2, 1, 3])
    result = counting_sort([76, 55, 3, 2, 88, 5, 76])
    print(result)
