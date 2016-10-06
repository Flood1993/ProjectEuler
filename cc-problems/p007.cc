#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {
    int limit = 200000;
    char * sieve = (char *) malloc(limit * sizeof(char));
    memset(sieve, 1, limit);
    
    sieve[0] = 0;
    sieve[1] = 0;

    for (int i = 2; i < limit/2; i++)
        if (sieve[i] == 1)
            for (int j = 2*i; j < limit; j += i)
                sieve[j] = 0;

    int cnt = 0;
    for (int i = 0; i < limit; i++) {
        if (sieve[i] == 1) {
            cnt += 1;

            if (cnt == 10001) {
                printf("%i", i);
                break;
            }
        }
    }

    free(sieve);

    return 0;
}