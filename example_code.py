#미로탐색 (#2178)
from collections import deque

def bfs(path, start, end, visited) :
  dist = [-1 for _ in range(0, len(path))]
  queue = deque([start])

  visited[start] = True
  dist[0] = 1

  while len(queue) != 0 :
    v = queue.popleft()
    if v == end :
      break

    for next in path[v] :
      if visited[next] == False :
        visited[next] = True
        queue.append(next)
        dist[next] = dist[v] + 1

  return dist[-1]

map1 = [] #맵 만들기
n, m = map(int, input().split())

for _ in range(n) :
  input_map = input()
  map1.append(input_map)

coordinate = [] #좌표 모아놓기

for i in range(n) :
  for j in range(m) :
    if map1[i][j] == "1" :
      coordinate.append((i,j))

dx, dy = [0, 0, -1, 1], [-1, 1, 0, 0]
path = [[] for _ in range(len(coordinate))]
visited = [False for _ in range(len(coordinate))]

for i in range(len(coordinate)) :
  x, y = coordinate[i][0], coordinate[i][1]

  for j in range(0,4) :
    nx, ny = x+dx[j], y+dy[j]
    if (nx, ny) in coordinate :
      b = coordinate.index((nx, ny))
      path[i].append(b)
      path[b].append(i)

answer = bfs(path, 0, len(coordinate), visited)

print(answer)
