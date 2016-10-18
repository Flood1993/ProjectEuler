#include <iostream>

int main() {
    unsigned int res = 0;

    for (unsigned int i = 1; i <= 1073741824; i++) {
        if ((i ^ (2*i) ^ (3*i)) == 0) {
            res++;
        }
    }

    printf("%u\n", res);

    return 0;
}