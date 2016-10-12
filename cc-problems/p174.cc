#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {
    int *types = (int *) malloc(1000001 * sizeof(int));
    memset(types, 0, 1000001 * sizeof(int));

    /*
    One way of making them starts with
    4*3
    4*5
    ...
    4*(2k + 1) -> uses less than 10**6 tiles as long as k <= 124999

    The other way is
    4*2
    4*4
    ...
    4*(2k) -> uses less than 10**6 tiles as long as k <= 125000
    */

    for (int i = 1; i <= 124999; i++) {
        int acc = 4 * (2*i + 1);
        types[acc] += 1;
        for (int k = i+1; k <= 124999; k++) {
            acc += 4 * (2*k + 1);
            if (acc > 1000000) {
                break;
            }
            types[acc] += 1;
        }
    }

    for (int i = 1; i <= 125000; i++) {
        int acc = 4 * (2*i);
        types[acc] += 1;
        for (int k = i+1; k <= 125000; k++) {
            acc += 4 * (2*k);
            if (acc > 1000000) {
                break;
            }
            types[acc] += 1;
        }
    }

    printf("1 = %i, 2 = %i\n", types[8], types[32]);

    int res = 0;

    for (int i = 0; i < 1000001; i++) {
        if (types[i] > 0 and types[i] <= 10) {
            res += 1;
        }
    }

    printf("Res: %i\n", res);

    free(types);
    return 0;
}