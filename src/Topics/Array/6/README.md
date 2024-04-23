# Наибольшее кол-во конфет

Есть N детей с конфетами. У вас есть массив `candies[int]`, где каждая `candies[i]` -  колличество конфет у конкретного ребенка.
`extraCandies` - целое число, обозночающее кол-во конфет которое вы можете добавить каждому ребенку.

Верните `result[bool]` длиной N, где `result[i]` будет True в случае если `candies[i]` + `extraCandies` 
будет больше среди каждого `candies[i]`.


Пример 1
```shell
Input: candies = [2,3,5,1,3], extraCandies = 3
Output: [true,true,true,false,true] 
```

Пример 2
```shell
Input: candies = [4,2,1,1,2], extraCandies = 1
Output: [true,false,false,false,false]
```


Пример 3
```shell
Input: candies = [12,1,12], extraCandies = 10
Output: [true, false, true]
```

# Задачи
- [1431. Kids With the Greatest Number of Candies](https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/description/)