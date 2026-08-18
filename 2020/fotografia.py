a, l = map(int, input().split())

n = int(input())

molduras = []
for _ in range(n):
    x, y = map(int, input().split())
    molduras.append((x, y))

for i, m in enumerate(molduras):
    if a <= m[0] and l <= m[1]:
        molduras[i] = (m[0] - a, m[1] - l)
    if a <= m[1] and l <= m[0]:
        molduras[i] = (m[1] - a, m[0] - l)
    else:
        molduras[i] = (-1, -1)

possiveis = [i for i in molduras if i != (-1, -1)]

if possiveis:
    menor = min(possiveis)
    print(molduras.index(menor) + 1)
else:
    print(-1)
