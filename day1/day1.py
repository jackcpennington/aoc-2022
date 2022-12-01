with open("day1/input.txt", 'r') as f:
    nums = [[int(num) for num in group.split("\n")]  for group in f.read().split("\n\n")]

p1 = max(map(sum, nums))
p2 = sum(sorted(map(sum, nums))[-3:])

print(p1, p1)