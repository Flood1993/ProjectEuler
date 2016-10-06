#include <stdio.h>

/*
Return the sum from 0 to end with step s
*/
int sum(int s, int end) {
    int n = int(end/s);

    return (n+1)*n*s / 2;
}

int main() {
    int limit = 999;
    int res = sum(3, 999) + sum(5, 999) - sum(15, 999);

    printf("%i", res);

    return 0;
}