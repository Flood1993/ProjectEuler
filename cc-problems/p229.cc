#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

int main() {
    int limit = 2000000000;
    int sqr_limit = (int) sqrt(limit);

    printf("Limit is %i\n", sqr_limit);

    bool * nums = (bool *) malloc(sizeof(bool) * limit);
    bool * nums2 = (bool *) malloc(sizeof(bool) * limit);
    bool * nums3 = (bool *) malloc(sizeof(bool) * limit);
    bool * nums7 = (bool *) malloc(sizeof(bool) * limit);
    memset(nums, false, limit * sizeof(bool));
    memset(nums2, false, limit * sizeof(bool));
    memset(nums3, false, limit * sizeof(bool));
    memset(nums7, false, limit * sizeof(bool));

    printf("Arrays allocated successfully\n");

    for (int i = 1; i <= 44721; i++) {
        long a = i*i;
        for (int j = i; j <= 44721; j++) {
            long b = j*j;

            if (a + b < limit){
                nums[a + b] = true;
                //nums[b + a] += 1;
            }

            if (a + 2*b < limit)
                nums2[a + 2*b] = true;
            if (b + 2*a < limit)
                nums2[b + 2*a] = true;

            if (a + 3*b < limit)
                nums3[a + 3*b] = true;
            if (b + 3*a < limit)
                nums3[b + 3*a] = true;

            if (a + 7*b < limit)
                nums7[a + 7*b] = true;
            if (b + 7*a < limit)
                nums7[b + 7*a] = true;
        }
    }

    int cnt = 0;

    for (int i = 0; i < limit; i++) {
        if (nums[i] && nums2[i] && nums3[i] && nums7[i]) {
            cnt++;
        }
    }

    free(nums);
    free(nums2);
    free(nums3);
    free(nums7);

    printf("%i\n", cnt);

    return 0;
}