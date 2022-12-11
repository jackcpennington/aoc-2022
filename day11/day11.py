from functools import reduce

class Monkey:
    def __init__(self, num, items, op, op_value, cond, true_monkey, false_monkey):
        self.num = num
        self.items = items
        self.op = op
        self.op_value = op_value
        self.cond = cond
        self.true_monkey = true_monkey
        self.false_monkey = false_monkey
        self.inspect_count = 0


with open("day11/input.txt", 'r') as f:
    monkeys_raw = [[line.strip() for line in block.split('\n')] for block in f.read().split('\n\n')]


def parse(lines):
    num = lines[0][-2]
    items = list(map(int, lines[1][16:].split(", ")))
    op, op_value = lines[2].split(' ')[-2:]
    cond = int(lines[3].split(' ')[-1])
    true_monkey = lines[4].split(' ')[-1]
    false_monkey = lines[5].split(' ')[-1]
    return Monkey(num, items, op, op_value, cond, true_monkey, false_monkey)

monkeys = []
for m in monkeys_raw:
    monkeys.append(parse(m))

all_conds = reduce(lambda x, y: x * y, [m.cond for m in monkeys])

for m in monkeys:
    m.items = list(map(lambda x: x + all_conds, m.items))

for r in range(10000):
    for m in monkeys:
        for item in m.items:
            m.inspect_count += 1

            if m.op == '+':
                worry = item+item if m.op_value == 'old' else item+int(m.op_value)
            else:
                worry = item*item if m.op_value == 'old' else item*int(m.op_value)

            #worry = worry//3
            worry = worry%all_conds

            receiver = m.true_monkey if worry%m.cond == 0 else m.false_monkey

            for x in monkeys:
                if x.num == receiver:
                    x.items.append(worry)
        m.items = []


print(reduce(lambda x, y: x * y, sorted([m.inspect_count for m in monkeys], reverse=True)[:2]))
