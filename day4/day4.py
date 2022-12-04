with open("day4/input.txt", 'r') as f:
    pairs = [[list(map(int, elf.split('-'))) for elf in pair.strip().split(',')] for pair in f.readlines()]


cnt = 0
for elf1, elf2 in pairs:
    if elf1[0] <= elf2[0] and elf1[1] >= elf2[1]:
        cnt += 1
    elif elf2[0] <= elf1[0] and elf2[1] >= elf1[1]:
        cnt += 1

print(cnt)

cnt2 = 0
for elf1, elf2 in pairs:
    if elf1[1] < elf2[0] or elf1[0] > elf2[1]:
        pass
    else:
        cnt2 +=1

print(cnt2)
