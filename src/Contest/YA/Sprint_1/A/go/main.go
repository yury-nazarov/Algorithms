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

func main(){
	res := Run("input.txt")
	fmt.Println(res)
}

// Задача: Написать код, вычисляющий: y = ax2 + bx + c.
// a, b, c, x - числа в файле data/input_*.txt
func Run(path string) int{
	readInputData := Input(path)
	prepareInput := Preparer(readInputData)
	result := Calc(prepareInput)
	return result
}

// Читаем файл и возвращаем массив строк
func Input(path string) []string{
	file, err := os.Open(path)
	if err != nil {
		log.Fatal(err) // it is print + os.Exit(Sprint_1)
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)
	scanner.Scan()
	return strings.Split(scanner.Text(), " ")
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

// Вычисляем: y = ax^2 + bx + c
func Calc(arr []int) int{
	a := arr[0]
	x := arr[1]
	b := arr[2]
	c := arr[3]
	result := a * int(math.Pow(float64(x), 2)) + b * x + c
	return result
}