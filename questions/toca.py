n, m = map(int, input().split())

direction = [(1, 0), (0, 1), (0, -1), (-1, 0)]

mapa = [list(map(int, input().split())) for _ in range(n)]

start_position = None
for index, i in enumerate(mapa):
    if 3 in i:
        j = i.index(3)
        start_position = (index, j)
