/*
Given a number and a step, the first three terms of the series would be:
n + 2*s
n + s
n
When squared:
(n + 2s)² - (n + s)² - n² 
= n² + 4s² + 4ns - (n² + 2ns + s²) - n² 
= n² + 4s² + 4ns - n² - 2ns - s² - n² 
x = - n² + 3s² + 2ns

For example, n = 6, s = 3:
- 36 + 3*9 + 2*18 = 27

Now, given x = 27, we want to find how many different values of n and s satisfy the formula:
x = - n² + 3s² + 2ns
La n es la que resta. La n empieza en 1. La s tiene que ir subiendo mientras el resultado sea <= 1000000

Create list of 1000000 elements

n even s even:
    x even
n even s odd:
    x odd
n odd s even:
    x odd
n odd s odd:
    x even

27 ->
n = 20, s = 7
n = 6, s = 3

*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {
    int* nums = (int *) malloc(1000000 * sizeof(int));
    memset(nums, 0, 1000000 * sizeof(int));

    int n_limit = 2000000000;

    for (int n = 1; n <= n_limit; n++) {
        // TODO: Calculate the highest and lowest values of s which stay in range.
        // Then, apply the algorithm only to those values (instead of starting at 1).
        int s = 1;
        long prod = 3*s*s + 2*n*s - n*n;
        while (prod < 1000000) {
            if (prod >= 0) {
                nums[prod] += 1;
            }

            s += 1;
            prod = 3*s*s + 2*n*s - n*n;
        }
    }

    int res = 0;

    for (int i = 0; i < 1000000; i++) {
        if (nums[i] == 10) {
            res += 1;
        }
    }

    printf("%i\n", res);

    free(nums);

    return 0;
}