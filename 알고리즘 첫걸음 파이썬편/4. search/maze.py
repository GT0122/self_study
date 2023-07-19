import copy

maze = [[9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9],
        [9, 0, 0, 0, 9, 0, 0, 0, 0, 0, 0, 9],
        [9, 0, 9, 0, 0, 0, 9, 9, 0, 9, 9, 9],
        [9, 0, 9, 9, 0, 9, 0, 0, 0, 9, 0, 9],
        [9, 0, 0, 0, 9, 0, 0, 9, 9, 0, 9, 9],
        [9, 9, 9, 0, 0, 9, 0, 9, 0, 0, 0, 9], 
        [9, 0, 0, 0, 9, 0, 9, 0, 0, 9, 1, 9],
        [9, 0, 9, 0, 0, 0, 0, 9, 0, 0, 9, 9],
        [9, 0, 0, 9, 0, 9, 0, 0, 9, 0, 0, 9],
        [9, 0, 9, 0, 9, 0, 9, 0, 0, 9, 0, 9],
        [9, 0, 0, 0, 0, 0, 0, 9, 0, 0, 0, 9],
        [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9]]

maze_copy = copy.deepcopy(maze)
pos = [[1, 1, 0]]
# 너비 우선 탐색
while pos :
    x, y, depth = pos.pop(0)
    if maze[x][y] == 1 :
        print('BFS')
        print(depth)
        break

    maze[x][y] = 2

    if maze[x - 1][y] < 2 :
        pos.append([x - 1, y, depth + 1])
    if maze[x + 1][y] < 2 :
        pos.append([x + 1, y, depth + 1])
    if maze[x][y - 1] < 2 :
        pos.append([x, y - 1, depth + 1])
    if maze[x][y + 1] < 2 :
        pos.append([x, y + 1, depth + 1])

# 깊이 우선 탐색
def search(x, y, depth) :
    if maze[x][y] == 1 :
        print('DFS')
        print(depth)

    maze[x][y] = 2

    if maze[x - 1][y] < 2 :
        search(x - 1, y, depth + 1)
    if maze[x + 1][y] < 2 :
        search(x + 1, y, depth + 1)
    if maze[x][y - 1] < 2 :
        search(x, y - 1, depth + 1)
    if maze[x][y + 1] < 2 :
        search(x, y + 1, depth + 1)

    maze[x][y] = 0

maze = copy.deepcopy(maze_copy)
search(1, 1, 0)

# 우수법 깊이 우선 탐색
dir = [[1, 0],  [0, 1], [-1, 0], [0, -1]]

x, y, depth, d = 1, 1, 0, 0

maze = copy.deepcopy(maze_copy)
while maze[x][y] != 1 :
    maze[x][y] = 2

    for i in range(len(dir)) :
        j = (d + i - 1) % len(dir)
        if maze[x + dir[j][0]][y + dir[j][1]] < 2 :
            x += dir[j][0]
            y += dir[j][1]
            d = j
            depth += 1
            break
        elif maze[x + dir[j][0]][y + dir[j][1]] == 2 :
            x += dir[j][0]
            y += dir[j][1]
            d = j
            depth -= 1
            break
print('right-hand DFS')
print(depth)