#include <stdio.h>
#include <math.h>

int main() {
    long long n = 600851475143;

    long long limit = (long long) sqrt(n);

    long long res = -1;

    for (int i = 3; i < limit; i += 2) {
        if (n % i == 0) {
            n /= i;
            limit = (long long) sqrt(n);
            res = i;
        }
    }

    if (n > res)
        res = n;

    printf("%i", res);

    return 0;
}