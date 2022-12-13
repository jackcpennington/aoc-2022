with open("day13/input.txt", 'r') as f:
    packets = [eval(packet.strip()) for packet in f.readlines() if packet.strip() != ""]


packets.append([[2]])
packets.append([[6]])


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



n = len(packets)
swapped = False
for i in range(n-1):
    for j in range(0, n-i-1):

        left, right = packets[j], packets[j+1]
        leftt = left if left != [] else []
        rightt = right if right != [] else []
        left_rest = left[1:] if left != [] else None
        right_rest = right[1:] if right != [] else None

        if not evall(leftt, rightt, left_rest, right_rest):
            swapped = True
            packets[j], packets[j+1] = packets[j+1], packets[j]

    if not swapped:
        break

key = 1
for idx, packet in enumerate(packets):
    if packet == [[2]] or packet == [[6]]:
        key *= (idx+1)

print(key)
