#include <stdio.h>

/*
Returns the sum of the squares of the first n natural numbers
*/
long long sum_of_squares(int n) {
    return n*(n+1)*(2*n + 1) / 6;
}

long long square_of_sum(int n) {
    return n*n*(n+1)*(n+1)/4;
}

long long solve(int n) {
    return square_of_sum(n) - sum_of_squares(n);
}

int main() {
    printf("%i", solve(100));

    return 0;
}