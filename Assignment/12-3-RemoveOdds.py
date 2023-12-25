from typing import List


def extract_evens(int_list: List[int]) -> List[int]:
    new_list =  []
    for i in int_list:
        if i % 2 == 0:
            new_list.append(i)
    return new_list
    """Returns a new list with only the even integers from the given list."""

    # TODO: Implement this function.

    raise NotImplementedError  # TODO: Remove this line when you're done.


def remove_odds(int_list: List[int]) -> None:
    int_list[:] = [i for i in int_list if i % 2 == 0]
    # for i in int_list:
    #     if i % 2 == 1 or i == 1:
    #         int_list.remove(i)
    return None

    # TODO: Implement this function.

    raise NotImplementedError  # TODO: Remove this line when you're done.
