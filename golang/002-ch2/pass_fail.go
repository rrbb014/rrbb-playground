// pass_fail 프로그램은 성적의 합격 여부를 알려 줍니다
package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
	"strings"
)

func main() {
	fmt.Println("Enter a grade: ")
	reader := bufio.NewReader(os.Stdin)
	// 1st option: Use blank identifier("_")
	//input, _ := reader.ReadString('\n')

	// 2nd option: Handle error
	input, err := reader.ReadString('\n')
	if err != nil {
		log.Fatal(err)
	}
	input = strings.TrimSpace(input)
	grade, err := strconv.ParseFloat(input, 64)
	if err != nil {
		log.Fatal(err)
	}

	var status string 
	if grade >= 60 {
		status = "passing"
	} else {
		status = "failed"
	}
	fmt.Println(status)
}
