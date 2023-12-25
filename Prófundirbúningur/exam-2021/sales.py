def main():
    filename = input("Enter file name: ")
    file_object = open_file(filename)
    if file_object is not None:
        filelines = file_object.read().splitlines()
        total_store = input("Show totals per store (y/n)? ")

        results = get_results(filelines)
        print_results(results)

        if total_store.lower() == "y":
            print_total_per_store(results)
    else:
        print(f"File {filename} not found")

def open_file(filename):
#Opens the given file, returning its file object if found, otherwise None
    try:
        file_object = open(filename, 'r')
        return file_object
    except FileNotFoundError:
        return None

def get_results(filelines):
    results = []
    for lines in sorted(filelines):
        results.append(lines.split(";"))
    return results

def print_results(results):
    for line in results:
        total_sales = float(line[1]) + float(line[2]) + float(line[3])
        print(f"{line[0]:<15}{float(line[1]):>12.2f}{float(line[2]):>12.2f}{float(line[3]):>12.2f}{float(total_sales):>12.2f}")

def print_total_per_store(results):
    store1, store2, store3 = 0.00, 0.00, 0.00

    for line in results:
        store1 += float(line[1])
        store2 += float(line[2])
        store3 += float(line[3])
    
    print(f"{'Total:':<15}{float(store1):>12.2f}{float(store2):>12.2f}{float(store3):>12.2f}")

if __name__ == "__main__":
    main()
