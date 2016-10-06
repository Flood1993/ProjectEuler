#include <stdio.h>

/*
Returns the sum of the even Fibonacci numbers below n.

The series is considered to start with 1, 2...
*/
int sum_even_fib(int n) {
    int a = 1;
    int b = 2;

    int sum = 2;

    while (b < n) {
        int c = a + b;
        a = b;
        b = c;

        if (b % 2 == 0)
            sum += b;
    }

    return sum;
}

int main() {
    printf("%i", sum_even_fib(4000000));

    return 0;
}