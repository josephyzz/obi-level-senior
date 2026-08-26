n = int(input())

plano = [[0 for i in range(n)] for i in range(n)]


def camada(k, n):
    for i in range(k - 1, n - k + 1):
        plano[k - 1][i] = k
        plano[n - k][i] = k
        plano[i][k - 1] = k
        plano[i][n - k] = k


for i in range(1, 2 + n // 2):
    camada(i, n)

for i in range(n):
    for j in range(n - 1):
        print(plano[i][j], end=" ")
    print(plano[i][n - 1])
