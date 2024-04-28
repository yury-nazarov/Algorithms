# QuickSort 
Сортировка Хоара (автор Чарльз Хоар)

Работает на основе принципа разделяй и влавствуй

**Базовые случаи**
- Пустой массив или массив из одного элемента. Можно адрегировать как: `arr < 2`
- Если массив состоит из двух элементов, их необходимо сравнить и раставить по возрастанию

**Рекурсивные случаи**

Входящий массив разбиваем на 
- Базовый элемент (произвольный элемент массива)
- les_or_equal - список из элементов <= базового элемента
- large - список из элементов > базового элемента



# Визуализация

![](img/quick_sort.png)