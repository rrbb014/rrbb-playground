package main

import (
	"fmt"
	"reflect"
)

func main() {
	var myInt int
	// pointer type은 *<TYPE>
	var myIntPointer *int
	myInt = 1
	// pointer 주소값은 &<VARIABLE>
	myIntPointer = &myInt
	fmt.Println(reflect.TypeOf(&myInt))
	fmt.Println(myIntPointer)
	// pointer값 불러오는것은 *<POINTER VARIABLE>
	fmt.Println(*myIntPointer)

	var myFloat float64
	var myFloatPointer *float64
	myFloat = 2.0
	myFloatPointer = &myFloat
	fmt.Println(reflect.TypeOf(&myFloat))
	fmt.Println(myFloatPointer)
	fmt.Println(*myFloatPointer)

	var myBool bool
	var myBoolPointer *bool
	myBool = true
	myBoolPointer = &myBool
	fmt.Println(reflect.TypeOf(&myBool))
	fmt.Println(myBoolPointer)
	fmt.Println(*myBoolPointer)


	// 함수에서 포인터 사용하기
	fmt.Println("함수에서 포인터 사용하기")

	var myFuncFloatPointer *float64 = createPointer()
	fmt.Println(myFuncFloatPointer)
	fmt.Println(*myFuncFloatPointer)

	// 입력변수 자체를 바꿔보자
	var floatInput float64 = 10.0
	fmt.Println(floatInput)
	globalDouble(&floatInput)
	fmt.Println(floatInput)
	
}

func createPointer() *float64 {
	var myFloat = 98.5
	return &myFloat
}

func globalDouble(input *float64) {
	*input *= 2
}