/*
Handle Multiple packages.
GOPATH
*/

package main

import (
	"greeting"
	"greeting/deutsch"
)

func main() {
	greeting.Hi()
	greeting.Hello()

	deutsch.Hallo()
	deutsch.GutenTag()
}
