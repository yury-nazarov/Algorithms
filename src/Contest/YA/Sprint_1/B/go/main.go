package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
	"strings"
)

func main(){
	fmt.Println(IsWin("input.txt"))
}

// Задача: На вход подается 3 числа, функция вернет WIN если все числа одной четности,
// в противном случае FAIL
//
// Решение: Основано на двух счетчиках, четный и нечетный.
// Если в финале один из них == 0, возвращаем WIN, иначе FAIL
func IsWin(path string) string{

	arr := InputFile(path)
	var even 	int 	// default 0
	var notEven int 	// default 0

	for i := 0; i < len(arr); i++ {
		if arr[i] % 2 == 0 {
			even += 1
		}else {
			notEven += 1
		}
	}

	if even == 0 || notEven == 0 {
		return "WIN"
	}
	return "FAIL"
}

func InputFile(path string) []int {
	file, err := os.Open(path)
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()
	scanner := bufio.NewScanner(file)
	scanner.Scan()
	return toInt(strings.Split(scanner.Text(), " "))
}

func toInt(arr []string) []int {
	var result []int
	for i := 0; i < len(arr); i++ {
		num, err := strconv.Atoi(arr[i])
		if err != nil {
			log.Fatal(err)
		}
		result = append(result, num)
	}
	return result
}
