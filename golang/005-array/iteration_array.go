package main

import (
	"fmt"
)

func main() {
	notes := [7]string{"do", "re", "mi", "fa", "so", "la", "ti"}
	// for-loop 1. index based iteration
	for i := 0; i < len(notes); i++ {
		fmt.Println(i, notes[i])
	}

	// for-loop 2. for range statement
	fmt.Println("for-loop 2")
	for index, value := range notes {
		fmt.Println(index, value)
	}
}
