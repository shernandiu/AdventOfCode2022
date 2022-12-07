with open("input/day7.sql", 'r') as f:
    lines = [x.strip() for x in f.readlines()]


class Dir:
    def __init__(self, name: str) -> None:
        self.parent = None
        self.name = name
        self.subdir = dict()
        self.files = dict()
        self.size = 0

    def add(self, dir):
        if type(dir) == Dir:
            self.subdir[dir.name] = dir
            self.size += dir.size
            dir.parent = self
        else:
            self.files[dir[1]] = dir[0]
            self.size += int(dir[0])
            if self.parent is not None:
                self.parent.update(int(dir[0]))

    def update(self, ammount):
        self.size += ammount
        if self.parent is not None:
            self.parent.update(ammount)


mainDir = Dir('/')
index = mainDir
dirs = set()
for a in lines:
    match a.split(' '):
        case '$', 'ls':
            pass
        case '$', 'cd', '..':
            index = index.parent
        case '$', 'cd', '/':
            index = mainDir
        case '$', 'cd', x:
            index = index.subdir[x]
        case 'dir', x:  # found dir
            if x not in index.subdir.keys():
                dirx = Dir(x)
                index.add(dirx)
                dirs.add(dirx)
        case x:         # found file
            index.add(x)

needed = 30_000_000-(70_000_000-mainDir.size)
min_dir = min(s.size for s in dirs if s.size >= needed)
print(sum(s.size for s in dirs if s.size <= 100_000))
print(min_dir)
