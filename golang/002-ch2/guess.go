// guess 프로그램은 플레이어가 난수를 맞히는 게임입니다.
package main

import (
	"fmt"
	"bufio"
	"os"
	"log"
	"math/rand"
	"strconv"
	"time"
	"strings"
)

func main() {
	// 플레이어가 추측할 1에서 100 사이의 난수를 지정합니다.
	seconds := time.Now().Unix()
	rand.Seed(seconds)
	target := rand.Intn(100) + 1
	fmt.Println("I've chosen a random number between 1 and 100.")
	fmt.Println("Can you guess it?")

	// 플레이어가 추측한 숫자를 입력할 수 있도록 프롬프트를 띄우고 입력받은 추측값을 저장합니다
	reader := bufio.NewReader(os.Stdin)

	var success bool = false

	for guesses := 10; guesses > 0 ; guesses-- {
		fmt.Println("You have", guesses , "guesses left")
		fmt.Println("Make a guess: ")
		input, err := reader.ReadString('\n')
		if err != nil {
			log.Fatal(err)
		}
		input = strings.TrimSpace(input)
		guess, err := strconv.Atoi(input)
		if err != nil {
			log.Fatal(err)
		}

		// 플레이어가 추측한 숫자가 목표값보다 낮으면 "Oops. Your guess was LOW."
		// 높으면 "Oops. Your guess was HIGH." 를 출력합니다.
		if guess < target {
			fmt.Println("Oops. Your guess was LOW.")
		} else if guess > target {
			fmt.Println("Oops. Your guess was HIGH.")
		} else {
			fmt.Println("Good job! You guessed it!")
			success = true
			break
		}
	}

	if !success {
		fmt.Println("Sorry, You didn't guess my number. It was", target)
	}


	// 플레이어는 최대 10번까지 추측할 수 있습니다. 추측을 할 때마다 플레이어에게 남은 횟수를 알려줍니다.

	// 플레이어가 추측한 숫자가 목표값과 같으면 "Good job! You guessed it!" 을 출력하고 프롬프르틑 종료합니다.

	// 최대 추측 횟수 안에 목표값을 맞히지 못하면 "Sorry, You didn't guess my number. It was: [TARGET]" 을 출력

}
