#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define DICE_NUMS 4
#define TURNS 40000000

int get_roll(int dice, int &cons_rolls) {
    int a = rand()%dice + 1;
    int b = rand()%dice + 1;
    if (a == b) {
        cons_rolls += 1;
    } else {
        cons_rolls = 0;
    }
    return a+b;
}

int cc(int pos, int &commun_to_draw) {
    if (pos != 2 && pos != 17 && pos != 33)
        return pos;

    if (commun_to_draw == 1){
        commun_to_draw = (commun_to_draw + 1) % 16;
        return 0;
    }
    if (commun_to_draw == 2) {
        commun_to_draw = (commun_to_draw + 1) % 16;
        return 10;
    }
    commun_to_draw = (commun_to_draw + 1) % 16;

    return pos;
}

int ch(int pos, int &chance_to_draw) {
    if (pos != 7 and pos != 22 and pos != 36) {
        return pos;
    }

    if (chance_to_draw == 1) {
        chance_to_draw = (chance_to_draw + 1) % 16;
        return 0;
    }
    if (chance_to_draw == 2) {
        chance_to_draw = (chance_to_draw + 1) % 16;
        return 10;
    }
    if (chance_to_draw == 3) {
        chance_to_draw = (chance_to_draw + 1) % 16;
        return 11;
    }
    if (chance_to_draw == 4) {
        chance_to_draw = (chance_to_draw + 1) % 16;
        return 24;
    }
    if (chance_to_draw == 5) {
        chance_to_draw = (chance_to_draw + 1) % 16;
        return 39;
    }
    if (chance_to_draw == 6) {
        chance_to_draw = (chance_to_draw + 1) % 16;
        return 5;
    } 
    if (chance_to_draw == 7 || chance_to_draw == 8) {
        if (pos == 7) {
            chance_to_draw = (chance_to_draw + 1) % 16;
            return 15;
        }
        if (pos == 22) {
            chance_to_draw = (chance_to_draw + 1) % 16;
            return 25;
        }
        if (pos == 36) {
            chance_to_draw = (chance_to_draw + 1) % 16;
            return 5;
        }
    }
    if (chance_to_draw == 9) {
        if (pos == 7) {
            chance_to_draw = (chance_to_draw + 1) % 16;
            return 12;
        }
        if (pos == 22) {
            chance_to_draw = (chance_to_draw + 1) % 16;
            return 28;
        }
        if (pos == 36) {
            chance_to_draw = (chance_to_draw + 1) % 16;
            return 12;
        }
    }
    if (chance_to_draw == 10) {
        chance_to_draw = (chance_to_draw + 1) % 16;
        return (pos + 37) % 40;
    }
    chance_to_draw = (chance_to_draw + 1) % 16;

    return pos;
}

void get_best_3(int* L, int* res) {
    int b1 = -1, b2 = -1, b3 = -1;
    int v1 = -1, v2 = -1, v3 = -1;

    for (int i = 0; i < 40; i++) {
        if (L[i] > v1) {
            v2 = v1;
            v3 = v2;
            b2 = b1;
            b3 = b2;
            v1 = L[i];
            b1 = i;
        } else if (L[i] > v2) {
            v3 = v2;
            b3 = b2;
            v2 = L[i];
            b2 = i;
        } else if (L[i] > v3) {
            v3 = L[i];
            b3 = i;
        }
    }

    res[0] = b1;
    res[1] = b2;
    res[2] = b3;
}

int main() {
    int cons_rolls = 0;
    int chance_to_draw = 0;
    int commun_to_draw = 0;

    int* squares = (int *) malloc(40 * sizeof(int));
    memset(squares, 0, 40*sizeof(int)); // Set all values to 0.
    int cur_pos = 0;

    for (int i = 0; i < TURNS; i++) {
        cur_pos = (cur_pos + get_roll(DICE_NUMS, cons_rolls))%40;
        cur_pos = cc(cur_pos, commun_to_draw);
        cur_pos = ch(cur_pos, chance_to_draw);
        if (cons_rolls == 3) {
            cur_pos = 10;
            cons_rolls = 0;
        }
        if (cur_pos == 30) {
            cur_pos = 10;
        }
        squares[cur_pos] += 1;
    }

    int res[3] = {0, 0, 0};
    get_best_3(squares, res);
    printf("Top 3: %i%i%i\n", res[0], res[1], res[2]);
    //for (int i = 0; i < 40; i++)
    //    if (squares[i] > 1000000) 
    //        printf("%02i %i\n", i, squares[i]);
    free(squares);
}

// Solution is 101524