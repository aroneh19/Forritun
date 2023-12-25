def main():
    vote_dict = {}
    input_str = 0
    
    while input_str != "":
        try:
            input_str = input("Candidate and votes: ")
            if input_str == "": break
            candidate, votes = input_str.lower().split()

            if votes == int(votes):
                votes = int(votes)
            else:
                print("Invalid no. of votes!")
                continue
        except ValueError:
            print("Invalid no. of votes!")
            continue
        
        update_votes(candidate, votes, vote_dict)
    
    print_votes(vote_dict)

def update_votes(candidate: str, votes: int, vote_dict: dict):
    if candidate in vote_dict:
        vote_dict[candidate] += votes
    else:
        vote_dict[candidate] = votes

def print_votes(vote_dict: dict):
    total_votes = 0
    
    for candidate, votes in sorted(vote_dict.items()):
        total_votes += votes
        print(f"{candidate}: {votes}")
    
    print("Total no. of votes:", total_votes)

if __name__ == '__main__':
    main()
