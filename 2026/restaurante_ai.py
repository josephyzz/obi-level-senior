g1, g2, g3, g4 = map(int, input().split())

mesas = 0

# Grupos de 4: cada um ocupa uma mesa inteira
mesas += g4

# Grupos de 3: cada um ocupa uma mesa, sobrando 1 lugar
mesas += g3
sobra_g3 = g3  # lugares livres (1 cada)
usados = min(sobra_g3, g1)
g1 -= usados

# Grupos de 2: formam pares (2+2 = mesa cheia)
mesas += g2 // 2
if g2 % 2 == 1:
    mesas += 1  # mesa com 2 lugares livres
    usa = min(2, g1)
    g1 -= usa

# Grupos de 1 restantes: de 4 em 4
mesas += (g1 + 3) // 4

print(mesas)
