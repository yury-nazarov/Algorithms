package main

import (
	"fmt"
	"sort"
	"strings"
)


// Больше примеров в тестах: go test
func main() {

	// Для дебага
	result := Counter("aaabbbсссссaaaaa")
	expect :=  "a8b3с5"


	if result == expect {
		fmt.Println(result, "==", expect)
	} else {
		fmt.Println(result, "!=", expect)
	}
}

func Counter(s string) string {
	// Write your code here

	// Считаем кол-во букв в строке и складываем в мапу
	storage := make(map[string]int)
	arr := strings.Split(s, "")
	for i := 0; i < len(arr); i++ {
		storage[arr[i]] += 1
	}

	// Формируем слайс из структур, для удобной сортировки на следующем шаге
	type Item struct {
		char 	string
		count 	int
	}
	var itemContainer []Item
	for k, v := range storage {
		itemContainer = append(itemContainer, Item{char: k, count: v})
	}

	// Сортируем в алфавитном порядке, с учетом заглавных букв
	sort.Slice(itemContainer, func(i, j int) bool {
		return itemContainer[i].char < itemContainer[j].char
	})

	// Меняем структуру на строку и удаляем старый слайс
	result := make([]string, len(itemContainer))
	for i := 0; i < len(itemContainer); i++ {
		result[i] = fmt.Sprintf("%s%d", itemContainer[i].char, itemContainer[i].count)
	}
	itemContainer = nil

	// Объединяем в строку и возвращаем
	return strings.Join(result[:], "")
}