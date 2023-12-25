
def main():
    filename = "retake\groupA.txt"
    filestream = open_file(filename)
    filelines = filestream.read().splitlines()
    
    results = get_results(filelines)
    print_results(results)

    show_standings = input("Show standings: ")
    if show_standings.lower() == "y":
        standings = generate_standings(results)
        print_standings(standings)

def open_file(filename: str):
    # Opens a given file, returns filestream
    try:
        filestream = open(filename)
        return filestream
    except FileNotFoundError:
        pass

def get_results(filelines: list[str]):
    # Takes in a list of strings containing results returns nested list of results
    results = []
    for lines in filelines:
        results.append(lines.split(";"))
    return results

def print_results(results):
    for result in results:
        country1, country2, score1, score2 = result
        score = f"{score1}:{score2}"
        formated_output = f"{country1:>13}{score:^5}{country2:<13}"
        print(formated_output)

def generate_standings(results):
    standings = {}
    for result in results:
        country1, country2, score1, score2 = result
        update_standings(country1, score1, score2, standings)
        update_standings(country2, score2, score1, standings)
    return standings

def update_standings(country: str, scored: int, conceded: int, standings):
    if country not in standings:
        standings[country] = {"points": 0, "scored": 0, "conceded": 0}
    standings[country]["points"] += calculate_points(scored, conceded)
    standings[country]["scored"] += int(scored)
    standings[country]["conceded"] += int(conceded)
 
def calculate_points(scored, conceded):
    if scored > conceded:
        return 3
    elif scored == conceded:
        return 1
    else:
        return 0

def print_standings(standings):
    for name, info in sorted(standings.items(), key = lambda a: a[1]["points"], reverse=True):
        points = info["points"]
        scored = info["scored"]
        conceded = info["conceded"]
        difference = scored - conceded
        goals = f"{scored}:{conceded}"
        print(f"{name:<13}{points:>2}{goals:>6}{difference:>3}")

if __name__ == '__main__':
    main()