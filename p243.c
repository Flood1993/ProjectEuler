#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {
    /*
    FACTS:

    - Resilience is symmetric.
    */
    int LIMIT = 20;
    int NUM = 4;
    int DEN = 10;

    int * list = malloc(LIMIT * sizeof(int));
    memset(list, 0, LIMIT);

    for (int i = 2; i < LIMIT/2; i++) {
        for (int j = i; j < LIMIT; j += i) {
            list[j] += 2;
        }
    }

    for (int i = 2; i < LIMIT; i += 2)
        list[i]--;

    for (int i = 2; i < LIMIT; i++) {
        if ((i - list[i] - 1)*DEN < (i - 1)*NUM)
            printf("%d\n", i);
    }

    free(list);
}
