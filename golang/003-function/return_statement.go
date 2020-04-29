package main

import (
	"fmt"
)

func double(number float64) float64 {
	return number * 2
}

func status(grade float64) string {
    if grade < 60.0 {
		return "failure"
	}
	return "pass"
}

func main() {
	fmt.Println(status(60.1))
	fmt.Println(status(59))
}