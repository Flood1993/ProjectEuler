#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define DIGITS_LIMIT 40

long long step_pand(int last_dig, bool zero, bool nine, int cur_digits, long *memo) {
    long long tmp = 0;
    
    if (cur_digits > DIGITS_LIMIT) {
        return 0;
    }
    
    int hash = 0;
    if (zero) {
        hash += 10000;
    }
    if (nine) {
        hash += 1000;
    }
    hash += last_dig * 100;
    hash += cur_digits;

    if (memo[hash] != -1) {
        return memo[hash];
    }

    if (zero && nine) { // Number is pandigital
        tmp = 1;

        if (last_dig == 0) {
            tmp += step_pand(1, true, nine, cur_digits + 1, memo);
        } else if (last_dig == 9) {
            tmp += step_pand(8, zero, true, cur_digits + 1, memo);
        } else {
            bool next_zero = (last_dig - 1 == 0);
            bool next_nine = (last_dig + 1 == 9);
            tmp += step_pand(last_dig - 1, zero || next_zero, nine , cur_digits + 1, memo);
            tmp += step_pand(last_dig + 1, zero, nine || next_nine, cur_digits + 1, memo);
        }

        memo[hash] = tmp;
        return tmp; // Is this return correct?
    }
    
    if (last_dig == 0) {
        tmp += step_pand(1, true, nine, cur_digits + 1, memo);
    } else if (last_dig == 9) {
        tmp += step_pand(8, zero, true, cur_digits + 1, memo);
    } else {
        bool next_zero = (last_dig - 1 == 0);
        bool next_nine = (last_dig + 1 == 9);
        tmp += step_pand(last_dig - 1, zero || next_zero, nine, cur_digits + 1, memo);
        tmp += step_pand(last_dig + 1, zero, nine || next_nine, cur_digits + 1, memo);
    }

    memo[hash] = tmp;
    return tmp;
}

int main() {
    long long res = 0;

    int size_to_alloc = 12000;
    long *memo = (long *) malloc(size_to_alloc * sizeof(long));
    memset(memo, -1, size_to_alloc * sizeof(long));

    for (int i = 1; i < 9; i++) {
        res += step_pand(i, false, false, 1, memo);
    }
    res += step_pand(9, false, true,  1, memo);

    printf("Result: %ld\n", res);

    free(memo);
    return 0;
}