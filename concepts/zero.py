n = int(input())

ops = [int(input()) for i in range(n)]

pilha = []
for x in ops:
    if x == 0 and pilha:
        pilha.pop()
    else:
        pilha.append(x)

print(sum(pilha))
