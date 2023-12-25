# Don't change the following lines
import math
number_of_waves = int(input())
number_of_lines = int(input())
radians_per_line = number_of_waves * 2 * math.pi / number_of_lines

# Loop through each line and print the sine wave
for i in range(number_of_lines):
    radians = i * radians_per_line
    sine_value = math.sin(radians)
    semi_amplitude = 20
    full_amplitude = 2 * semi_amplitude
    x_count = round((sine_value + 1) * semi_amplitude)
    whitespace_count = 40 - x_count
    line = 'X' * x_count
    print(line)
