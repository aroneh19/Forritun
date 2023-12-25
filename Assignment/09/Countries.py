import sys

COUNTRIES_OF_THE_WORLD = "countries.txt"
INPUT_PROMPT = "Enter a suffix for a country: "

def main():
    counter = 0
    country_suffix = get_suffix()
    with open(COUNTRIES_OF_THE_WORLD) as file:
        lines = file.read().splitlines()
    for line in lines:
        if line.endswith(country_suffix):
            counter += 1
            print(line)
    print(f"{counter} countries with suffix {country_suffix} in total.")

def get_suffix():
    sys.stderr.write(INPUT_PROMPT)
    return input()

main()