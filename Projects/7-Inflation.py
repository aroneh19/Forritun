# Define the main function, which serves as the entry point of the program
def main():
    try:
        filename = get_filename() # Get the filename from user input
        print_tuples(filename) # Print the data tuples read from the file
        data_tuples = add_to_tuples(filename) # Create a list of data tuples with additional information
        display_tuples(data_tuples) # Display the data tuples with additional information
        difference_in_index(data_tuples) # Calculate and print the difference in index for each year
    except FileNotFoundError:
        quit() # Handle the case where the file is not found by quitting the program

# Function to get the filename from user input
def get_filename():
    filename = input()
    return filename

# Function to print data tuples from a file
def print_tuples(filename):
    if filename is None:
        quit()

    try:
        with open(filename, "r") as file:
            for line in file:
                split = line.split()
                time = split[0]
                index = float(split[1])
                data_tuple = (time, index)
                print(data_tuple)
    except FileNotFoundError:
        quit()

# Function to read and process data from a file, creating data tuples with additional information
def add_to_tuples(filename):
    data_tuples = []
    first_index = 0
    last_index = 0
    last_year = None

    try:
        with open(filename, "r") as file:
            for line in file:
                split = line.split()
                current_year = int(split[0][:4])
                price = float(split[1])

                if last_year is None:
                    first_index = price
                    last_year = int(current_year)

                if current_year != last_year:
                    data_tuples.append((last_year, first_index, last_index))
                    first_index = price
                    last_year = current_year

                last_index = price

        # Append the last data tuple
        data_tuples.append((last_year, first_index, last_index))
    except FileNotFoundError:
        quit()

    return data_tuples

# Function to display data tuples
def display_tuples(data_tuples):
    for data_tuple in data_tuples:
        print(data_tuple)

# Function to calculate and print the difference in index for each year
def difference_in_index(data_tuples):
    for i in range(len(data_tuples)):
        year, first_index, last_index = data_tuples[i]
        year = int(year)

        # Calculate inflation rate
        inflation = round(((last_index - first_index) / first_index) * 100, 2)
        print((year, inflation))

# Check if the script is executed as the main program
if __name__ == "__main__":
    main()
