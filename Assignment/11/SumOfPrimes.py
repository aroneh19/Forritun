def prime_sum(list):
    result = 0
    for i in list:
        if is_prime(i):
            result += int(i)
    return result

def is_prime(number_to_check: int) -> bool:
    """Returns True if the number n is prime, False otherwise."""

    if number_to_check < 2:
        return False

    potential_factor = 2
    while potential_factor**2 <= number_to_check:
        if number_to_check % potential_factor == 0:
            return False

        potential_factor += 1

    return True