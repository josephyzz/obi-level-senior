from collections import deque


N, M = map(int, input().split())
grid = []
for _ in range(N):
    grid.append(list(map(int, input().split())))


# altura de (i,j) no turno t = (grid[i][j] + t) % 10
def altura(i, j, t):
    return (grid[i][j] + t) % 10


# Estado: (linha, coluna, turno % 10)
# Como tudo é cíclico com período 10, basta guardar turno % 10
visited = set()
# fila: (turno, linha, coluna)
fila = deque()
fila.append((0, 0, 0))
visited.add((0, 0, 0 % 10))

direcoes = [(-1, 0), (1, 0), (0, -1), (0, 1)]

while fila:
    t, i, j = fila.popleft()

    if i == N - 1 and j == M - 1:
        print(t)
        return

    # Altura atual da célula do jogador ANTES das plataformas subirem
    h_atual = altura(i, j, t)
    proximo_t = t + 1

    # Opção 1: esperar (ficar no lugar)
    estado_espera = (i, j, proximo_t % 10)
    if estado_espera not in visited:
        visited.add(estado_espera)
        fila.append((proximo_t, i, j))

    # Opção 2: mover para vizinho
    for di, dj in direcoes:
        ni, nj = i + di, j + dj
        if 0 <= ni < N and 0 <= nj < M:
            h_destino = altura(ni, nj, t)  # altura ANTES de subir
            if h_destino <= h_atual + 1:
                estado = (ni, nj, proximo_t % 10)
                if estado not in visited:
                    visited.add(estado)
                    fila.append((proximo_t, ni, nj))
