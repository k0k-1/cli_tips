// author: kip-s
// 2017-05-02
package main

import (
	"fmt"
)

func main() {
	for n := 1; n <= 32; n++ {
		if n%3 == 0 {
			fmt.Print("fizz")
		}

		if n%5 == 0 {
			fmt.Print("buzz")
		} else if n%3 != 0 {
			fmt.Print(n)
		}
		fmt.Println()
	}
}
