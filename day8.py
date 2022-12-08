from collections import defaultdict
# text = '''30373
# 25512
# 65332
# 33549
# 35390'''
with open('input/day8.sql', 'r') as f:
    text = f.read()
matrix = [[int(x) for x in i] for i in text.splitlines()]
scenic_score = [[1 for _ in range(len(matrix))] for _ in range(len(matrix))]

visibles = set()


def checkLine(line, index: int, vertical: bool):
    max_tree = -1
    seen_trees = defaultdict(lambda: 0)
    seen_trees[10] = 0
    for i, tree in enumerate(line):
        if tree > max_tree:
            max_tree = tree
            visibles.add((index, i) if not vertical else (i, index))

        scenic_score[index if not vertical else i][index if vertical else i] *= (i - max([distance for tree_h, distance in seen_trees.items() if tree_h >= tree], default=-1))
        seen_trees[tree] = max((seen_trees[tree], i))
    max_tree = -1
    seen_trees = defaultdict(lambda: len(matrix)-1)
    seen_trees[10] = len(matrix)-1
    for i, tree in list(enumerate(line))[::-1]:
        if tree > max_tree:
            max_tree = tree
            visibles.add((index, i) if not vertical else (i, index))

        scenic_score[index if not vertical else i][index if vertical else i] *= min([distance for tree_h, distance in seen_trees.items() if tree_h >= tree], default=len(matrix)) - i
        seen_trees[tree] = min((seen_trees[tree], i))


[checkLine(line, index, False) for index, line in enumerate(matrix)]
[checkLine(colum, index, True) for index, colum in enumerate([[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix))])]

# print(len(visibles))

for i in scenic_score:
    print(' '.join(map(str, i)))

print(f"2) Max = {max([max(row) for row in scenic_score])}")
