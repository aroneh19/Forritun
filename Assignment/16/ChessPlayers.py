from collections import defaultdict

def get_lines_from_files(filename):
    try:
        with open(filename)as file:
            return file.read().splitlines()
    except FileNotFoundError:
        return []

def get_players(lines):
    players = defaultdict(tuple)

    for line in lines:
        rank, name, country, rating, bith_year, = line.split("; ")
        last_name, first_name, = name.split(",")
        full_name = f"{first_name} {last_name}"
        players[full_name] = (int(rank), country, int(rating), int(bith_year))
    return players

def get_player_by_country(lines):
    d = defaultdict(list)

    for line in lines:
        _,name, country, rating, _ = line.split("; ")
        last_name, first_name, = name.split(",")
        full_name = f"{first_name} {last_name}"
        d[country].append((full_name, int(rating)))
    return d

def print_players_by_country(players_by_country):
    print(s := "players by country:")
    print("-" * len(s))

    for country, players in sorted(players_by_country.items()):
        player_count = len(players)
        avg = sum(rating for name, rating in players) / player_count
        print(f"{country} ({player_count}) ({round(avg, 1)}):")

        for name, rating in players:
            print(f"{name:>40} {rating:>10}")

def main():
    filename = input("Enter filename: ")
    lines = get_lines_from_files(filename)

    players_by_country = get_player_by_country(lines)
    print_players_by_country(players_by_country)

if __name__ == "__main__":
    main()