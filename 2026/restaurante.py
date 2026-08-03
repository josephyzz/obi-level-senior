grupos = list(map(int, input().split()))


total_por_grupos = [grupos[i - 1] * i for i in range(1, 5)]

total_mesas = grupos[3]


if total_por_grupos[0] >= grupos[2]:
    total_por_grupos[0] -= grupos[2]
    total_mesas += grupos[2]


print(grupos)
print(total_por_grupos)
