# Задачи
## Topics


* [String](src/Topics/String)
    * [Самое длинное слово в строке](src/Topics/String/1)
    * [Палиндром](src/Topics/String/2)
    * [Подсчет букв и сжатие строки](src/Topics/String/3)
* [Array](src/Topics/Array)
    * [Списочная форма](src/Topics/Array/1)
    * [Общее число](src/Topics/Array/2)
    * [Клумба](src/Topics/Array/3)
    * [Горный массив](src/Topics/Array/4)
    * [Горный массив](src/Topics/Array/4)
    * [Диапазоны чисел](src/Topics/Array/5)
    * [Наибольшее кол-во конфет](src/Topics/Array/6)
    * [Наибольшая возрастающая последовательность](src/Topics/Array/7)
* [Math](src/Topics/Math) 
    * [Квадратная функция](src/Topics/Math/1)
    * [Числа одной четности](src/Topics/Math/2)
    * [Перевод числа из десятичной в двоичную](src/Topics/Math/3)
    * [Степень четверки](src/Topics/Math/4)

# Теория
## Поиск

| Название                                              | Асимптотика (худшее/лучшее)   | Пространственная сожность |  Добавлено |
| -------------                                         | -------------                 | -------------             | ------------- |
| [Bin Search / Бинарный поиск](src/Search/bin_search/) | O(log(n))                     |  O(1)                     | 03.08.2020 | 


## Сортировка

Квадратичные сортировки - сортировки работающие за O(n^2) в худшем случае.

| Название                                                         | Асимптотика (худшее/лучшее)    | Пространственная сожность |  Примечание           | Добавлено |
| -------------                                                    | -------------                  | -------------             | -------------         | ------------- |
| [Selection Sort (Сортировка выбором)](src/Sort/selection_sort/)  | O(n^2) /  O(n^2)               |  O(1)                     |                       | 03.08.2020 |
| [Bubble Sort (Сортировка пузырьком)](src/Sort/buble_sort/)       | O(n^2) /  O(n)                 |  O(1)                     |                       | 03.08.2020 |
| [Insertion Sort (Сортировка вставками)](src/Sort/insertion_sort/)| O(n^2) /  O(n)                 |  O(1)                     |                       | 04.08.2020 | 
| [Quick Sort (Быстрая сортировка)](src/Sort/quick_sort/)          | O(n^2) / O(n)                  | O(n * log n)              |                       | 06.08.2020 |
| [Merge Sort (Сортировка слиянием)](src/Sort/merge_sort/)         | O(n * long n)                  | O(n)                      |                       | 13.08.2020 |
| [Counting Sort (Сортировка подсчетом)](src/Sort/counting_sort/)  | O(n)                           | O(k)                       | За линейное время сортировать массив целых чисел из не очень большого диапазона k | ??.08.2020 |
| [Radix Sort (Поразрядная сортировка)](src/Sort/radix_sort/)      | O(n)                           | O(1)                       | Нужно заранее знать индексы k, m    | ??.08.2020 |


## Проверка

Запуск тестов

```
cd /dit/with/tests
python3 -m unittest main_tests.py
```