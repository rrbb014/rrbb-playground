package main

import (
	"fmt"
	//"errors"
	"log"
)

func main() {
	height := -2.333333
	err := fmt.Errorf("a height of %0.2f is invalid.", height)
	fmt.Println(err)
	log.Fatal(err)
}