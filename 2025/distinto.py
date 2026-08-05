P = int(input())

chocolates = [0] * P
for index in range(P):
    bolinhas = 0
    L, A, B = map(int, input().split())  # A = Min, B = Max
    valores_livres = sorted([i for i in range(A, (B + 2))], reverse=1)

    for i in range(len(valores_livres)):
        if bolinhas < L:
            bolinhas += valores_livres[i]
            valores_livres.pop(i)
        else:
            chocolates[index] += 1

print(chocolates)
