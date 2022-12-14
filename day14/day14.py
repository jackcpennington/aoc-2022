with open("day14/input.txt", 'r') as f:
    rocks = [line.strip().split(' -> ') for line in f.readlines()]


cave = {(0, 500): 'X'}

for rock in rocks:
    for start, end in list(zip(rock, rock[1:])):
        start_j, start_i = list(map(int, start.split(',')))
        end_j, end_i = list(map(int, end.split(',')))

        delta_i, delta_j = end_i - start_i, end_j - start_j

        cave[(start_i, start_j)] = '#'

        if delta_i > 0:
            for i in range(1,delta_i+1):
                cave[(start_i+i, start_j)] = '#'
        elif delta_i < 0:
            for i in range(-1,delta_i-1, -1):
                cave[(start_i+i, start_j)] = '#'
        elif delta_j > 0:
            for j in range(1,delta_j+1):
                cave[(start_i, start_j+j)] = '#'
        else:
            for j in range(-1,delta_j-1, -1):
                cave[(start_i, start_j+j)] = '#'




mini, maxi = min(i for i,_ in cave.keys()), max(i for i,_ in cave.keys())
minj, maxj = min(j for _,j in cave.keys()), max(j for _,j in cave.keys())


def print_cave():
    cave_img= [['.' for j in range(minj, maxj+1)] for i in range(mini,maxi+1)]

    for i in range(len(cave_img)):
        for j in range(len(cave_img[0])):
            if (i+mini,j+minj) in cave.keys():
                cave_img[i][j] = cave[(i+mini,j+minj)]
        print("".join(cave_img[i]))

    print()

max_depth = maxi
sand_count = 0
while True:
    sand_count +=1
    sand_pos = (0,500)
    prev_sand_pos = (-1, 500)
    while sand_pos != prev_sand_pos:
        #check down
        if not (sand_pos[0]+1, sand_pos[1]) in cave.keys():
            prev_sand_pos = sand_pos
            sand_pos = (sand_pos[0]+1, sand_pos[1])
        elif not (sand_pos[0]+1, sand_pos[1]-1) in cave.keys():
            prev_sand_pos = sand_pos
            sand_pos = (sand_pos[0]+1, sand_pos[1]-1)
        elif not (sand_pos[0]+1, sand_pos[1]+1) in cave.keys():
            prev_sand_pos = sand_pos
            sand_pos = (sand_pos[0]+1, sand_pos[1]+1)
        else:
            cave[sand_pos] = 'O'
            prev_sand_pos = sand_pos
        #print_cave()
        if sand_pos[0] > max_depth:
            print_cave()
            print(sand_count-1)
            exit()

