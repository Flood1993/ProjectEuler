#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

#define N 40000000

int main() {
    bool * primes = (bool *) malloc(N * sizeof(bool));
    memset(primes, true, N * sizeof(bool));
    primes[0] = false;
    primes[1] = false;
    for (int i = 2; i < N; i++) {
        if (primes[i]) {
            for (int j = 2*i; j < N; j += i) {
                primes[j] = false;
            }
        }
    }

    printf("Checking primes: p(0) %i, p(7) %i, p(50) %i\n", primes[0], primes[7], primes[50]);

    long * nums = (long *) malloc(N * sizeof(long));
    memset(nums, 0, N * sizeof(long));

    for (int i = 1; i < N; i++) {
        nums[i] = i;
    }
    for (int i = 2; i < N; i++) {
        if (primes[i]) {
            for (int j = i; j < N; j += i) {
                nums[j] = (nums[j] * (i-1)) / i; // TODO: This could be dangerous
            }
        }
    }

    printf("Checking totients: t(7) %i, t(18) %i\n", nums[7], nums[18]);

    long res = 0;

    int * steps = (int *) malloc(N * sizeof(int));
    memset(steps, -1, N * sizeof(int));
    steps[1] = 1;
    for (int i = 2; i < N; i++) {
        int tot = nums[i];
        steps[i] = steps[tot] + 1;

        if (steps[i] == 25 && primes[i]) {
            res += i;
        }
    }

    printf("Checking lens: l(5) %i, l(18) %i\n", steps[5], steps[18]);

    printf("Sol: %lu\n", res);

    free(nums);
    free(primes);
    free(steps);

    return 0;
}