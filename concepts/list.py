# Listas

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Ordernação e extensão
lista.sort(reverse=1)
lista.extend([10, 11, 12])

print(lista)

# maximo
print(max(lista))

# Minimo
print(min(lista))

# Filter
filtered = filter(lambda a: a > 5, lista)

# Ao invés de sempre usar loops use filter
print(list(filtered))
