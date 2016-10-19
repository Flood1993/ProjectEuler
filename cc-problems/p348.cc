#include <stdio.h>
#include <math.h>

// Returns whether a number can be expressed as a sum of a square and a cube
// in exactly four different ways.
bool representable(int x) {
    int limit = pow(x, 1.0/3.0); // Cube root
    int sols = 0;

    for (int i = 2; i < limit; i++) {
        int cube = pow(i, 3);

        int remainder = x - cube;
        if (remainder > 1) {
            int sqrt_remainder = sqrt(remainder);
            if (sqrt_remainder*sqrt_remainder == remainder)
                sols++;
        }
    }

    return sols == 4;
}

int main() {
    // 3, 4 digits
    for (int i = 1; i <= 9; i++)
        for (int j = 0; j <= 9; j++) {
            int num = 101*i
                     + 10*j;
            if (representable(num))
                printf("%i\n", num);

            num = 1001*i
                 + 110*j;
            if (representable(num))
                printf("%i\n", num);
        }

    // 5, 6 digits
    for (int i = 1; i <= 9; i++)
        for (int j = 0; j <= 9; j++)
            for (int k = 0; k <= 9; k++){
                int num = 10001*i
                         + 1010*j
                          + 100*k;
                if (representable(num))
                    printf("%i\n", num);

                num = 100001*i
                     + 10010*j
                      + 1100*k;
                if (representable(num))
                    printf("%i\n", num);
            }

    // 7, 8 digits
    for (int i = 1; i <= 9; i++)
        for (int j = 0; j <= 9; j++)
            for (int k = 0; k <= 9; k++)
                for (int l = 0; l <= 9; l++) {
                    int num = 1000001*i
                             + 100010*j
                              + 10100*k
                               + 1000*l;
                    if (representable(num))
                        printf("%i\n", num);

                    num = 10000001*i
                         + 1000010*j
                          + 100100*k
                           + 11000*l;
                    if (representable(num))
                        printf("%i\n", num);
                }

    // 9 digits
    for (int i = 1; i <= 9; i++)
        for (int j = 0; j <= 9; j++)
            for (int k = 0; k <= 9; k++)
                for (int l = 0; l <= 9; l++)
                    for (int m = 0; m <= 9; m++) {
                        int num = 100000001*i
                                 + 10000010*j
                                  + 1000100*k
                                   + 101000*l
                                    + 10000*m;
                        if (representable(num))
                            printf("%i\n", num);
                    }


    return 0;
}