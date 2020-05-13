package main

import (
	"fmt"
)

func main() {
	var notes [7]string
	notes[0] = "do"
	notes[1] = "re"
	notes[2] = "mi"
	fmt.Println(notes[0])
	fmt.Println(notes[1])

	var notes2 [7]string = [7]string{"do", "re", "mi", "fa", "so", "la", "ti"}
	fmt.Println(notes2[0], notes2[2], notes2[4])

	notes3 := [7]string{"do", "re", "mi", "fa", "so", "la", "ti"}

	fmt.Println(notes3) // ["do", "re", "mi", "fa", "so", "la", "ti"]
	// %#v 는 변수 있는 그대로 출력.
	fmt.Printf("%#v\n", notes3) // [7]string{"do", "re", "mi", "fa", "so", "la", "ti"}

}
