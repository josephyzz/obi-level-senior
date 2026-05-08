n, c = map(int, input().split())

transmissores = set()
infectados = set()

for _ in range(c):
    lista = list(map(int, input().split()))

    transmissores.add(lista[0])

    for i in range(1, len(lista)):
        infectados.add(lista[i])


paciente_zero = []
for i in transmissores:
    if i not in infectados:
        paciente_zero.append(i)

for i in sorted(paciente_zero):
    print(i)
