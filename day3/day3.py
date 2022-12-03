with open("day3/input.txt", 'r') as f:
    nums = [line.strip() for line in f.readlines()]

alpha = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
total = 0

for line in nums:
    index = len(line)//2

    x, y = set(line[:index]), set(line[index:])

    inter = x.intersection(y)
    total += alpha.index(list(inter)[0])+1

print(total)


chunks = [nums[i:i + 3] for i in range(0, len(nums), 3)]
total2 = 0

for chunk in chunks:
    inter = set.intersection(*map(set, chunk))
    total2 += alpha.index(list(inter)[0])+1

print(total2)
