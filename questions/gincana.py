from collections import deque

n, m = map(int, input().split())

grafos = {i: [] for i in range(1, n + 1)}

for _ in range(m):
    i, j = map(int, input().split())
    if i != j:
        grafos[i].append(j)
        grafos[j].append(i)


visitados = set()
grupos = 0


def search(inicio):
    fila = deque([inicio])
    visitados.add(inicio)

    while fila:
        atual = fila.popleft()
        for amigo in grafos[atual]:
            if amigo not in visitados:
                visitados.add(amigo)
                fila.append(amigo)


for aluno in range(1, n + 1):
    if aluno not in visitados:
        search(aluno)
        grupos += 1

print(grupos)
