#include <stdio.h>
#include <math.h>

/*
Prime numbers:
2 3 5 7 11 13 17 19
2**4 <= 20
3**2 <= 20
*/

int main() {
    long long res = pow(2, 4) * pow(3, 2) * 5 * 7 * 11 * 13 * 17 * 19;
    
    printf("%i", res);

    return 0;
}