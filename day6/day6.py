with open("day6/input.txt", 'r') as f:
    buffer = f.read().strip()

for i in range(len(buffer)):
    marker = set(buffer[i:i+14])

    if len(marker) == 14:
        print(marker, i+14)
        break
