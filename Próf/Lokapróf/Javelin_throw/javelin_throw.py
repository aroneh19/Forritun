def main():
    filename = input()
    filestream = open_file(filename)
    
    if filestream: # if there is a file open
        filelines = filestream.read().splitlines()
        
        results = get_results(filelines)
        updated_list = update_results(results)

        print_standings(updated_list)

        highest_average = calculate_highest_average(updated_list)
        if highest_average: # Checks if the highest average is not empty
            print(f"{highest_average[0]}: {round(highest_average[1], 2)}")

def open_file(filename: str):
    # Opens a given file, returns filestream
    try:
        filestream = open(filename)
        return filestream
    except FileNotFoundError:
        return False

def get_results(filelines: list[str]):
    # Takes in a list of strings containing results returns nested list of results
    results = []
    for lines in filelines:
        results.append(lines.split())
    return results

def update_results(results: list[str]):
    standings = {} # Empty dictionary

    for player in results:
        if player[0] not in standings: # Checks if the player is in the dictionary, if not adds them to the dictionary
            standings[player[0]] = {"first_name": "", "last_name": "", "score": ""}
            standings[player[0]]["first_name"] = player[0]
            standings[player[0]]["last_name"] = player[1]
            standings[player[0]]["score"] = player[2]
        else: # If there is a player in the dictionary, then add the score
            standings[player[0]]["score"] += f" {player[2]}"
    return standings

def print_standings(standings: dict): # Prints the standings in a specified format
    for _, info in standings.items():
        first_name = info["first_name"]
        last_name = info["last_name"]
        score = info["score"]
        name = first_name + " " + last_name
        print(f"{name:<20}Throws: {score}")

def calculate_highest_average(standings: dict):
    result = []
    highest_average = 0
    highest_name = ""

    for _, info in standings.items(): # Loop through the standings
        player_score = 0
        name = info["first_name"] + " " + info["last_name"]
        score = info["score"].split()

        if len(score) >= 2: # Calculate the average if they did threw twice
            for i in score:
                player_score += float(i)
            player_score /= len(score)

            if player_score > highest_average: # Check if the player has the highest score so far
                highest_name = name # Updates variables
                highest_average = player_score
    
    result = [highest_name, highest_average]
    if result[1] != 0: # Checks if the player doesn't have a score
        return result
    return False

if __name__ == "__main__":
    main()