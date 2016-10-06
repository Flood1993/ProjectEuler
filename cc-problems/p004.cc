#include <stdio.h>

/*
Returns whether n is a palindrome number.

For this problem, it is guaranteed that n should not be bigger than one million, so we can use int.
*/
bool is_palindrome(int n) {
    return (n%10 == n/100000
            && (n%100) / 10 == (n/10000) % 10
            && (n%1000) / 100 == (n/1000) % 10);
}

int main() {
    int higher = -1;

    for (int i = 999; i > 700; i--) {
        for (int j = i; j > 700; j--) {
            int prod = i*j;

            if (is_palindrome(prod) && prod > higher)
                higher = prod; 
        }
    }
    printf("%i", higher);

    return 0;
}