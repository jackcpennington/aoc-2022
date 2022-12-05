with open("day5/input.txt", 'r') as f:
    crates, instructions = f.read().split('\n\n')

instructions = [list(map(int, list(filter(lambda x: x.isdigit(), instruction.split(' '))))) for instruction in  instructions.strip('\n').split('\n')]

crates = [list(line) for line in crates.split('\n')[:-1]]
crates2 = []
for line in crates:
    del line[3::4]
    crates2.append(line[1:-1:3])

crates2 = [list(filter(lambda x: x != ' ', tower[::-1])) for tower in list(map(list, zip(*crates2)))]
for move, fromm, to in instructions:

    crates2[to-1] += crates2[fromm-1][-move:] #[::-1] for part 1 
    crates2[fromm-1] = crates2[fromm-1][:-move]


print("".join([x[-1] for x in crates2]))
