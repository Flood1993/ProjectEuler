class Score:
    def __init__(self, hit, multiplier):
        self.hit = hit
        self.multiplier = multiplier

    def get_score(self):
        return self.hit * self.multiplier


class CheckoutInfo:
    def __init__(self, last_hit: Score):
        if last_hit.multiplier != 2:
            raise ValueError('Last hit landed must be a double')
        self.first_hit = None
        self.second_hit = None
        self.last_hit = last_hit

    def clone(self):
        result = CheckoutInfo(self.last_hit)
        result.first_hit = self.first_hit
        result.second_hit = self.second_hit
        return result

    def from_points(self):
        total = self.last_hit.get_score()
        if self.first_hit is not None:
            total = total + self.first_hit.get_score()
        if self.second_hit is not None:
            total = total + self.second_hit.get_score()
        return total

    def unique_str_repr(self):
        """
        Sort the 1st and 2nd hits to detect duplicates
        """
        # Sort the 1st and 2nd hit, if needed
        if self.first_hit is not None and self.second_hit is not None:
            if self.first_hit.multiplier > self.second_hit.multiplier:
                self.first_hit, self.second_hit = self.second_hit, self.first_hit
            elif self.first_hit.multiplier == self.second_hit.multiplier:
                if self.first_hit.hit > self.second_hit.hit:
                    self.first_hit, self.second_hit = self.second_hit, self.first_hit

        str_values = []
        if self.first_hit is not None:
            str_values.append(f'{self.first_hit.hit},{self.first_hit.multiplier}')
        if self.second_hit is not None:
            str_values.append(f'{self.second_hit.hit},{self.second_hit.multiplier}')
        str_values.append(f'{self.last_hit.hit},{self.last_hit.multiplier}')

        return '-'.join(str_values)


all_scores = []
all_possible_checkouts = []
for i in range(1, 21):
    all_scores.append(Score(i, 1))
    all_scores.append(Score(i, 2))
    all_scores.append(Score(i, 3))

    all_possible_checkouts.append(CheckoutInfo(Score(i, 2)))

# Bulls-eye
all_scores.append(Score(25, 1))
all_scores.append(Score(25, 2))

all_possible_checkouts.append(CheckoutInfo(Score(25, 2)))

to_add = []
for score in all_scores:
    for checkout in all_possible_checkouts:
        clone = checkout.clone()
        clone.first_hit = score
        to_add.append(clone)
all_possible_checkouts.extend(to_add)

to_add = []
for score in all_scores:
    for checkout in all_possible_checkouts:
        clone = checkout.clone()
        clone.second_hit = score
        to_add.append(clone)
all_possible_checkouts.extend(to_add)

solution = set()
for checkout in all_possible_checkouts:
    solution.add(checkout.unique_str_repr())
print(f'Total checkouts: {len(solution)}')

all_checkouts_less_than_100 = [checkout for checkout in all_possible_checkouts if checkout.from_points() < 100]

print(f'Solution (with duplicates): {len(all_checkouts_less_than_100)}')

solution = set()
for checkout in all_checkouts_less_than_100:
    solution.add(checkout.unique_str_repr())
print(f'Solution: {len(solution)}')
