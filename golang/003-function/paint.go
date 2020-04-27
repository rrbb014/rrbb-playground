package main

import (
	"fmt"
)

var meterPerLiter float64

func paintNeeded(width float64, height float64) float64 {
	area := width * height
	//fmt.Printf("%.2f liters needed\n", area/10.0)
	return area / meterPerLiter
}

func main() {
	meterPerLiter = 10.0
	fmt.Printf("%.2f", paintNeeded(4.2, 3.0))
	//fmt.Println(area)    // area's variable scope는 paintNeeded 함수 내부라서 에러
	paintNeeded(5.2, 3.5)
	paintNeeded(5.0, 3.3)
}
