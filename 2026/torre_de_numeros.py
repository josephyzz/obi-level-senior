n = str(input())

torre = [n]

while True:
    n = list(str(torre[-1]))

    if len(n) < 4:
        k = 4 - len(n)
        n.extend(["0"] * k)

    n_menor = sorted(n)
    n_maior = sorted(n, reverse=True)

    n_menor = "".join(n_menor)
    n_maior = "".join(n_maior)

    diff = int(n_maior) - int(n_menor)

    if diff in torre:
        break

    else:
        torre.append(diff)

for t in torre:
    print(t)
