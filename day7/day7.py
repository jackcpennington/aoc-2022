class File:
    def __init__(self, name, parent, size=0):
        self.name = name
        self.children = []
        self.parent = parent
        self.size = size
        self.directory = True if size == 0 else False

with open("day7/input.txt", 'r') as f:
    lines = [line.strip().split(' ') for line in f.readlines()]


fs = File("/", None)
current = fs #current dir
dirs = [fs]

for line in lines[1:]:
    match line[0], line[1]:
        case "$", "cd":
            if line[2] == "..":
                current = current.parent
            else:
                current = [child for child in current.children if child.name == line[2]][0]
        case "$", _:
            pass
        case "dir", _:
            new_dir = File(line[1], current)
            current.children.append(new_dir)
            dirs.append(new_dir)
        case _:
            new_file = File(line[1], current, int(line[0]))
            current.children.append(new_file)

def getSize(file):
    if file.directory == False:
        return file.size
    else:
        return sum([getSize(file) for file in file.children])

sizes = []
for dirr in dirs:
    sizes.append(getSize(dirr))

print(sum(filter(lambda size: size < 100000, sizes)))

fs_size = getSize(fs)
sizes2 = []
boundry = 70000000 - fs_size
mini = 30000000 - boundry

print(min(filter(lambda size: size > mini, sizes)))
