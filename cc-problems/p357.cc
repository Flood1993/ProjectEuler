#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/*
d + n/d is prime. Let's say d=30

5 + 30/5 -> 5+6 -> 11 (5 + 6) = 5*6
5 + 25/5 -> 5+5 -> 10 (5 + 5) i*j = 5*5
5 + 5/5 -> 5+1 -> 6 (5+1) i*j = 5*1
*/

#define LIMIT 100000001

int main() {
    long long sum = 0;

    bool * primes = (bool *) malloc(LIMIT * sizeof(bool));
    memset(primes, true, LIMIT * sizeof(bool));

    primes[0] = false;
    primes[1] = false;

    for (int i = 2; i < LIMIT; ++i) {
        if (!primes[i]) // Composite
            continue;
        else // Prime: Set all multiples as not prime
            for (int j = 2*i; j < LIMIT; j += i)
                primes[j] = false;
    }

    printf("Primes generated ok. p[7] %i, p[42] %i\n", primes[7], primes[42]);

    bool * valid_numbers = (bool *) malloc(LIMIT * sizeof(bool));
    memset(valid_numbers, true, LIMIT * sizeof(bool));
    valid_numbers[0] = false; // Positive numbers

    printf("valid numbers: 0 %i, 30: %i\n", valid_numbers[0], valid_numbers[30]);

    for (int i = 1; i < LIMIT; i++) {
        //if (primes[i]) {
            for (int j = 1; j <= LIMIT / i; j++) {
                if (!primes[i + j]) {
                    valid_numbers[i*j] = false;
                }
            }
        //}
    }

    printf("valid numbers: 0 %i, 1 %i, 2 %i, 3 %i, 30: %i\n",
            valid_numbers[0],
            valid_numbers[1],
            valid_numbers[2],
            valid_numbers[3],
            valid_numbers[30]);

    for (int i = 0; i < LIMIT - 1; i++)
        if (valid_numbers[i])
            sum += i;

    printf("%ld\n", sum);
    free(primes);
    free(valid_numbers);

    return 0;
}