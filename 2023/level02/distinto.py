n = int(input())


# ir adicionando item em uma lista
# quando um numero já existe adicionamos a lista em outro lista
# esvaziamos a current_seq
# repetimos

sequencies = []
current_seq = []
for _ in range(n):
    number = int(input())
    if number in current_seq:
        sequencies.append(len(current_seq))
        current_seq = []
        continue
    current_seq.append(number)

print(max(sequencies))
