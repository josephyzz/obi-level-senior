# 2022

n = int(input())

matriz = []
for i in range(n):
    line = list(map(int,input().split()))
    matriz.append(line)

zeros = []
for i in range(n):
    for j in range(n):
        if matriz[i][j] == 0:
            zeros.append((j, i))


for cord in zeros:
    valor = (n * (n ** 2 + 1)) //2
    x, y = cord
    if x == y:
        for i in range(n):
            valor -= matriz[i][i]
    else:
        for l in matriz[y]:
         valor -= l
        
    print(valor)
    print(y + 1)
    print(x + 1)




