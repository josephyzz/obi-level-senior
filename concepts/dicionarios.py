carro = dict(marca='Chevrolet', modelo='Tracker', ano=2020)
del carro['marca']
print(carro)

# Se não existir retorna None
print(carro.get('marca'))

# Retorna Chevrolet
print(carro.get('marca', 'Chevrolet'))

# Remova 'marca' caso não exita retorne None
carro.pop('marca', None)

carro.popitem()  # remove a ultima da dict

# Uso do zip

pessoas = ['Marcos', 'Ricardo', 'Ana']
idades = [23, 35, 29]
dict_pessoas = dict()
for nome, idade in zip(pessoas, idades):
    dict_pessoas[nome] = idade
print(dict_pessoas)
