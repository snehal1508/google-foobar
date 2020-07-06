def bfs(x1, y1, map):
    w = len(map[0])
    h = len(map)
    maze = [[None for i in range(w)] for i in range(h)]
    maze[x1][y1] = 1

    li = [(x1, y1)]
    while li:
        x, y = li.pop(0)
        for i in [[1, 0], [-1, 0], [0, -1], [0, 1]]:
          x2, y2 = x + i[0], y + i[1]
          if 0 <= x2 < h and 0 <= y2 < w:
            if maze[x2][y2] is None:
                maze[x2][y2] = maze[x][y] + 1
                if map[x2][y2] == 1:
                  continue
                li.append((x2, y2))

    return maze


def solution(map):
  w = len(map[0])
  h = len(map)
  m1 = bfs(0, 0, map)
  m2 = bfs(h-1, w-1, map)
  maze = []

  cnt = 2 ** 32-1
  for i in range(h):
      for j in range(w):
          if m1[i][j] and m2[i][j]:
              cnt = min(m1[i][j] + m2[i][j] - 1, cnt)
  return cnt
