#include <stdio.h>
#include <stdlib.h>
#include <string.h>

long check(int a, int b, int c, int digits, long *memo) {
    long tmp = 0;

    if (memo[10000*digits + (100*a + 10*b + c)] != -1) {
        return memo[10000*digits + (100*a + 10*b + c)];
    }

    if (a + b + c > 9) {
        memo[10000*digits + (100*a + 10*b + c)] = 0;
        return 0;
    }

    if (digits == 20) {
        memo[10000*digits + (100*a + 10*b + c)] = 1;
        return 1;
    }

    for (int i = 0; i < 10; i++) {
        tmp += check(b, c, i, digits + 1, memo);
    }
    memo[10000*digits + (100*a + 10*b + c)] = tmp;
    return tmp;
}

int main() {
    long RES = 0;

    long *memoization = (long *) malloc(1000 * 10 * 21 * sizeof(long));
    memset(memoization, -1, 1000 * 10 * 21 * sizeof(long));

    for (int c = 1; c < 10; c++) {
        RES += check(0, 0, c, 1, memoization);
    }

    printf("%ld\n", RES);

    free(memoization);

    return 0;
}