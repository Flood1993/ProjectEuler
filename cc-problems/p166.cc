/*
Lets define our grid as:
a b c d
e f g h
i j k l
m n o p
*/

#include <stdio.h>

int main() {
    long long sol = 0;

    for (int a = 0; a < 10; a++)
        for (int b = 0; b < 10; b++)
            for (int c = 0; c < 10; c++)
                for (int d = 0; d < 10; d++) {
                    int sum = a + b + c + d;

                    for (int e = 0; e < 10; e++)
                        for (int i = 0; i < 10; i++) {
                            int m = sum - i - e - a;
                            if (m < 0 || m > 9)
                                continue;

                            for (int f = 0; f < 10; f++)
                                for (int g = 0; g < 10; g++) {
                                    int h = sum - g - f - e;
                                    if (h < 0 || h > 9)
                                        continue;

                                    int j = sum - m - g - d;
                                    if (j < 0 || j > 9)
                                        continue;

                                    for (int k = 0; k < 10; k++) {
                                        int l = sum - k - j - i;
                                        if (l < 0 || l > 9)
                                            continue;

                                        int n = sum - j - f - b;
                                        if (n < 0 || n > 9)
                                            continue;

                                        int o = sum - k - g - c;
                                        if (o < 0 || o > 9)
                                            continue;

                                        int p = sum - m - n - o;
                                        if (p < 0 || p > 9)
                                            continue;

                                        if (a+f+k+p == sum && d+g+j+m == sum && b+f+j+n == sum && c+g+k+o == sum && d+h+l+p == sum && i+j+k+l == sum && m+n+o+p == sum)
                                            sol++;
                                    }
                                }
                        }
                }

    printf("%i", sol);

    return 0;
}