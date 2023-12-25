def read_countries_from_file(filename):
    countries_dict = {}
    try:
        with open(filename, 'r') as file:
            for country in file:
                country = country.strip()
                length = len(country)
                if length in countries_dict:
                    countries_dict[length].append(country)
                else:
                    countries_dict[length] = [country]
        return countries_dict
    except FileNotFoundError:
        print(f"File {filename} not found!")
        return None


def main():
    file_name = input().strip()
    countries_dict = read_countries_from_file(file_name)

    while not countries_dict:
        file_name = input().strip()
        countries_dict = read_countries_from_file(file_name)

    more_queries = True
    while more_queries:
        query = int(input().strip())
        if query in countries_dict:
            print(", ".join(countries_dict[query]))
        else:
            print(f"No country name of length {query} exists.")
        more_queries = input().strip() == 'y'


if __name__ == "__main__":
    main()
