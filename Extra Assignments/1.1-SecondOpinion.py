
total_seconds_str = int(input()) # Do not change this line.

if total_seconds_str >= 3600:
    hours = total_seconds_str // 3600
    total_seconds_str %= 3600
else:
    hours = 0

if total_seconds_str >= 60:
    minutes = total_seconds_str // 60
    total_seconds_str %= 60
else:
    minutes = 0

seconds = total_seconds_str

print(hours, ":", minutes, ":", seconds) # Do not change this line.