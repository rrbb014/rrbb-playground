package main

import (
	"fmt"
	"log"

	"github.com/rrbb014/rrbbgo/keyboard"
)

func main() {
	fmt.Print("Enter your number: ")
	number, err := keyboard.GetFloat()
	if err != nil {
		log.Fatal(err)
	}
	fmt.Println("Number is:", number)
}
