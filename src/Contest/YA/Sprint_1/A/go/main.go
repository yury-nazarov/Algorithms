package main

import (
	"bufio"
	"fmt"
	"log"
	"math"
	"os"
	"strconv"
	"strings"
)

// Вывод на экран
func main(){
	res := Run("input.txt")
	fmt.Println(res)
}

// Основная функция запускающая код и что то возвращающая. Ее и будем тестировать.
func Run(path string) int{
	readInputData := Input(path)
	prepareInput := Preparer(readInputData)
	result := Calc(prepareInput)
	return result
}

// Читаем файл, и возвращаем массив строк
func Input(path string) []string{
	file, err := os.Open(path)
	if err != nil {
		log.Fatal(err) // it is print + os.Exit(Sprint_1)
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)
	scanner.Scan()
	return strings.Split(scanner.Text(), " ") // В этом случае нужен Flush? Или он только при записи?
}

// Вспомогательная функция, для преобразования массива строк в массив интов
func Preparer(arr []string) []int {
	var result []int
	for i :=0; i < len(arr); i++ {
		n, _ := strconv.Atoi(arr[i])
		result = append(result, n)
	}
	return result
}

// y = ax^2 + bx + c
func Calc(arr []int) int{
	a := arr[0]
	x := arr[1]
	b := arr[2]
	c := arr[3]
	result := a * int(math.Pow(float64(x), 2)) + b * x + c
	return result
}