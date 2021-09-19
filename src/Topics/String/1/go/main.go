package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"sort"
	"strings"
)

func main(){
	FindWord()
}
// https://contest.yandex.ru/contest/22449/run-report/51785761/
// TODO: WA 11

// Задача: Найти самое длинное слово в строке
// Если самых длинных слов несколько вернуть первое
// На входе в первой строке: длина текста, во второй строка. Пример: data/input_*.txt
func FindWord(){
	inputString := InputFile("../data/input_3.txt")
	sortStrings := SortInputString(inputString)
	word := LongestWord(sortStrings)
	//fmt.Println(sortStrings)
	fmt.Println(word.str)
	fmt.Println(word.len)
}

type Word struct {
	str string
	len int
}


func LongestWord(arr []Word) Word {
	maxNum := arr[len(arr)-1].len
	var result []Word
	for i := len(arr)-1; i > 0; i-- {
		//fmt.Println("--- ",maxNum, arr[i])
		if arr[i].len == maxNum {
			result = append(result, arr[i])
		} else {
			break
		}
	}
	return result[len(result)-1]

}

func SortInputString(arr []string) []Word{
	var result []Word
	for i := 0; i < len(arr); i++ {
		word := &Word{}
		word.str = arr[i]
		word.len = len(arr[i])
		result = append(result, *word)
	}
	// Сортируем, сохраняя порядок одинаковых слов
	sort.SliceStable(result, func(i, j int) bool{
		return result[i].len < result[j].len
	})
	return result
}

func InputFile(path string) []string {
	file, err := os.Open(path)
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()
	scanner := bufio.NewScanner(file)
	scanner.Scan()
	//letters, _ := strconv.Atoi(scanner.Text())
	scanner.Scan()
	inputString := strings.Split(scanner.Text(), " ")
	return inputString
}