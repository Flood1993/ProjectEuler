#include <stdio.h>
#include <math.h>

#define SIZE 1900

int len_path(int a, int b, bool &valid) {
    int c = (int) sqrt(a*a + b*b);
    valid = false;
    if (c*c == a*a + b*b) {
        valid = true;
    }
    return c;
}

bool min_has_integer_len(int a, bool va, int b, bool vb, int c, bool vc) {
    return ((a <= b && a <= c && va)
                || (b <= a && b <= c && vb)
                || (c <= a && c <= b && vc));

}

int gcd(int a, int b) {
    while (b != 0) {
        int new_b = a%b;
        a = b;
        b = new_b;
    }
    return a;
}

// Returns the Cardano triplet obtained from values m, n
// Make sure that only one of m and n can be even and gcd of m, n must be 1
void triplet(int m, int n, int* out) {
    out[0] = m*m - n*n;
    out[1] = 2*m*n;
    out[2] = m*m + n*n;
}

int main() {
    int res = 0;

    for (int x = 1; x <= SIZE; x++) {
        for (int y = 1; y <= x; y++) {
            for (int z = 1; z <= y; z++) {
                bool v1 = false;
                int p1 = len_path(x+y, z, v1);
                bool v2 = false;
                int p2 = len_path(x+z, y, v2);
                bool v3 = false;
                int p3 = len_path(y+z, x, v3);

                if (min_has_integer_len(p1, v1, p2, v2, p3, v3)) {
                    res += 1;
                }
            }
        }
        if (x > 1500) {
            printf("%i %i\n", x, res);
        }
    }
    printf("%i\n", res);

    return 0;
}

/*int main() {
    int t[3] = {0, 0, 0};
    int res = 0;
    
    for (int m = 2; m <= SIZE/2 + 1; m++) {
        for (int n = 1; n < m; n++) {
            if ((m + n) % 2 == 0) {
                continue;
            }
            if (gcd(m, n) != 1) {
                continue;
            }
            triplet(m, n, t);
            int t0 = t[0];
            int t1 = t[1];
            int t2 = t[2];
            while (t[0] <= SIZE && t[1] <= SIZE) {
                int min_len = t[2];

                // Lets suppose t[0] is splitted
                int z = t[1];
                for (int x = 1; x <= t[0]; x++) {
                    y = t[0] - x;
                    
                    
                }
                // Lets suppose t[1] is splitted
                res += t[0]/2 + t[1]/2;
                t[0] += t0;
                t[1] += t1;
                t[2] += t2;
            }
        }
    }

    printf("%i\n", res);

    return 0;
}*/