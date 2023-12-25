# Read exactly four lines of input
line1 = input()
line2 = input()
line3 = input()
line4 = input()

# Define variables for the range of numbers within which we have 'printable' characters.
# As we shift the input characters, we must ensure that they stay within this range.
LOW = ord(" ")  # 32
HIGH = ord("~")  # 126

# Every transmission starts with the line "Hail Caesar!" so the first letter,
# once decrypted, must be H.
first_letter = line1[0]

# Find out what the key is
# Initialize the key to 0
key = 0

# Iterate through all possible shifts
for i in range(LOW, HIGH + 1):
    decrypted = ""

    # Decrypt each character in the current line using the current key
    for char in line1:
        if char == " ":  # Skip spaces
            decrypted += " "
        else:
            decrypted_char = chr(((ord(char) - i - LOW) % (HIGH - LOW + 1)) + LOW)
            decrypted += decrypted_char

    # Check if the first character of the decrypted line matches 'H'
    if decrypted[0] == first_letter:
        key = i
        break

# Use the found key to decrypt all four lines
decrypted_lines = []
for line in (line1, line2, line3, line4):
    decrypted = ""
    for char in line:
        if char == " ":  # Skip spaces
            decrypted += " "
        else:
            decrypted_char = chr(((ord(char) - key - LOW) % (HIGH - LOW + 1)) + LOW)
            decrypted += decrypted_char
    decrypted_lines.append(decrypted)

# Print the decrypted lines
for line in decrypted_lines:
    print(line)
