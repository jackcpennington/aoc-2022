with open("day2/input.txt", 'r') as f:
    lines = [line.strip().split(" ") for line in f.readlines()]

    def select(x):
        match x:
            case 'X':
                return 1, 'A'
            case 'Y':
                return 2, 'B'
            case 'Z':
                return 3, 'C'

    total = 0

for x, y in lines:
    score, y2 = select(y)

    if y2 == x:
        total += score + 3
    elif (y2 == 'B' and x == 'A') or(y2 == 'C' and x == 'B') or (y2 == 'A' and x == 'C'):
        total += score + 6
    else:
        total += score

print(total)

def win(x):
    match x:
        case 'A':
            return 2
        case 'B':
            return 3
        case 'C':
            return 1

def draw(x):
    match x:
        case 'A':
            return 1
        case 'B':
            return 2
        case 'C':
            return 3

def lose(x):
    match x:
        case 'A':
            return 3
        case 'B':
            return 1
        case 'C':
            return 2



total2 = 0
for x, y in lines:
    if y == 'X':
        total2 += lose(x)
    elif y == 'Y':
        total2 += draw(x) + 3
    elif y == 'Z':
        total2 += win(x) + 6
    print(total2)

print(total2)

