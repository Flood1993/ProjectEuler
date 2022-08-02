from functions import is_probable_prime


def generate_numbers(digits, fixed_digits, fixed_digit):
    """
    Given a number of digits "digits", of which "fixed_digits" are fixed to the value of "fixed_digit",
    this generator will yield all possible numbers which adhere to those conditions.

    Note that non-fixed digits must be other than "fixed_digit".
    """
    if fixed_digits == 0 and digits != 0:
        for digit in range(10):
            if str(digit) != fixed_digit:
                for el in generate_numbers(digits - 1, fixed_digits, fixed_digit):
                    yield str(digit) + el
    elif fixed_digits == 0 and digits == 0:
        yield ""
    elif digits == fixed_digits:
        yield fixed_digit * digits
    else:
        for el in generate_numbers(digits - 1, fixed_digits - 1, fixed_digit):
            yield fixed_digit + el

        for el in generate_numbers(digits - 1, fixed_digits, fixed_digit):
            for digit in range(10):
                if str(digit) != fixed_digit:
                    yield str(digit) + el


def S(digits: int, d: str):
    for fixed_digits in range(digits - 1, -1, -1):
        result = 0
        for n in generate_numbers(digits, fixed_digits, d):
            does_not_start_with_zero = len(str(int(n))) == digits
            if is_probable_prime(int(n)) and does_not_start_with_zero:
                result += int(n)
        if result != 0:
            return result

    return 0


def sum_S(digits: int):
    total = 0
    for fixed_digit in range(10):
        total += int(S(digits, str(fixed_digit)))
    return total


print(sum_S(10))
