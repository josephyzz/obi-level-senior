from itertools import combinations

n, m = map(int, input().split())

ingredientes = [i for i in range(1, n + 1)]
restricoes = [list(map(int, input().split())) for _ in range(m)]

validas = []
for r in range(1, len(ingredientes) + 1):
    for combo in combinations(ingredientes, r):
        if any(set(restricao).issubset(combo) for restricao in restricoes):
            continue
        validas.append(combo)

print(len(validas))
