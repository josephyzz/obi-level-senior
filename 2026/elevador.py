n = int(input())

paradas = list(map(int, input().split()))

current_parada = paradas[0]
t = 0
for i in range(1, len(paradas)):
    if current_parada > paradas[i]:
        t += current_parada - paradas[i]
    if current_parada < paradas[i]:
        t += paradas[i] - current_parada

    current_parada = paradas[i]

print(t)
