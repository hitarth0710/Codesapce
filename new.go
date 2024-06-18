package main

import "fmt"

// Function to calculate factorial
func factorial(n int) int {
	if n == 0 {
		return 1
	}
	return n * factorial(n-1)
}

func main() {
	num := 5
	fmt.Printf("Factorial of %d is %d", num, factorial(num))
}
