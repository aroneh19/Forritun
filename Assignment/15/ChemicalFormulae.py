from typing import Tuple

UI = False


def main():
    formula_1, formula_2 = get_formulae()

    chemical_set_1 = get_chemicals_in_formula(formula_1)
    chemical_set_2 = get_chemicals_in_formula(formula_2)

    state_common_chemicals(chemical_set_1, chemical_set_2)


def get_formulae(user_interface: bool = UI) -> Tuple[str]:
    """Asks the user for two chemical formulae, and returns them."""

    formula_1 = input("Enter a chemical formula:\n" if user_interface else "")
    formula_2 = input("Enter another chemical formula:\n" if user_interface else "")

    return formula_1, formula_2


def get_chemicals_in_formula(chemical_formula: str) -> set:
    """Returns the set of element found in the formula."""
    i = 0
    chemicals = set()

    while i < len(chemical_formula):
        if i + 1 < len(chemical_formula) and chemical_formula[i + 1].islower():
            chemicals.add(chemical_formula[i:i + 2])
            i += 2
        else:
            chemicals.add(chemical_formula[i])
            i += 1

        while i < len(chemical_formula) and chemical_formula[i].isdigit():
            i += 1

    return chemicals


def state_common_chemicals(chemical_set_1: set, chemical_set_2: set) -> None:
    """Prints the chemicals common to both sets, in alphabetical order."""
    common_chemicals = sorted(chemical_set_1.intersection(chemical_set_2))
    print(', '.join(common_chemicals))


if __name__ == "__main__":
    main()
