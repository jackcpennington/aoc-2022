with open("day13/input.txt", 'r') as f:
    pairs = [[eval(packet) for packet in pair.split('\n')] for pair in f.read().strip().split('\n\n')]


    def evall(left, right, left_rest, right_rest):
        #print(left, right, left_rest, right_rest)

        if isinstance(left, int) and isinstance(right, int):
            if left != right:
                return left < right
            if left_rest == []:
                return True
            if right_rest == []:
                return False
            else:
                return evall(left_rest[0], right_rest[0], left_rest[1:], right_rest[1:])

        if isinstance(left, list) and isinstance(right, list):
            if left == [] and right == []:
                return evall(left_rest[0], right_rest[0], left_rest[1:], right_rest[1:])
            if left == []:
                return True
            if right == []:
                return False
            return evall(left[0], right[0], [left[1:]]+left_rest, [right[1:]]+right_rest)

        if isinstance(left, int) and isinstance(right, list):
            return evall([left], right, left_rest, right_rest)

        if isinstance(left, list) and isinstance(right, int):
            return evall(left, [right], left_rest, right_rest)


counter = 0
for idx, pair in enumerate(pairs):
    left, right = pair
    leftt = left if left != [] else []
    rightt = right if right != [] else []
    left_rest = left[1:] if left != [] else None
    right_rest = right[1:] if right != [] else None


    if evall(leftt, rightt, left_rest, right_rest):
        counter += idx + 1


print(counter)
