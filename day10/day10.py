with open("day10/input.txt", 'r') as f:
    ops = [line.strip().split(' ') for line in f.readlines()]

x = 1
cycle_counter = 0
cycle_idxs = [20, 60, 100, 140, 180, 220]
strength_signals = []
for op in ops:

    match op[0]:
        case "addx":
            cycles = 2
            value = int(op[1])
        case _:
            cycles = 1
            value = 0

    for i in range(cycles):
        if cycle_counter + i + 1 in cycle_idxs:
            strength_signals.append((cycle_counter+1+i)*x)

    cycle_counter += cycles
    x += value

print(sum(strength_signals))


mid_pixel = 2
cycle_counter = 1
crt = []
for op in ops:
    match op[0]:
        case "addx":
            cycles = 2
            value = int(op[1])
        case _:
            cycles = 1
            value = 0

    for i in range(cycles):
        crt.append('#' if cycle_counter+i in [mid_pixel-1,mid_pixel,mid_pixel+1] else '.')
        if (cycle_counter+i)%40 == 0:
            mid_pixel += 40

    cycle_counter += cycles
    mid_pixel += value

for row in[crt[i:i + 40] for i in range(0, len(crt), 40)]:
    print("".join(row))
