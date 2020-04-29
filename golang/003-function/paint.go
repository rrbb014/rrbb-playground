package main

import (
	"fmt"
	"log"
)


func paintNeeded(width float64, height float64) (float64, error) {
	if width < 0 {
		return 0, fmt.Errorf("a width %0.2f is invalid", width)
	}
	if height < 0 {
        return 0, fmt.Errorf("a height %0.2f is invalid", height)
	}
	area := width * height
	//fmt.Printf("%.2f liters needed\n", area/10.0)
	return area / 10.0, nil
}

func catchError(err error) {
	if err != nil {
        log.Fatal(err)
	}
}

func main() {
	var amount, total float64
	amount, err := paintNeeded(4.2, -3.0)
	catchError(err)
	amount, err = paintNeeded(4.2, 3.0)
	catchError(err)
	fmt.Printf("%0.2f liters needed\n", amount)
	total += amount
	amount, err = paintNeeded(5.2, 3.5)
	catchError(err)
	fmt.Printf("%0.2f liters needed\n", amount)
	total += amount
	fmt.Printf("Total: %0.2f liters\n", total)
}