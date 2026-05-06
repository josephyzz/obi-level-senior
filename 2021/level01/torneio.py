"""
Torneio de Tênis.
"""
# https://olimpiada.ic.unicamp.br/pratique/ps/2021/f1/torneio/
# Points 100/100
# t = 0,024s / 0,1s
# memory 4.12 MB/ 64 MB

# Record = 07min

# By josephyzz

from collections import Counter

resultado_do_jogo = [input() for i in range(6)]

c = Counter(resultado_do_jogo)

p_vencidas = c['V']


if p_vencidas in [5, 6]:
    print(1)
elif p_vencidas in [3, 4]:
    print(2)
elif p_vencidas in [1, 2]:
    print(3)
else:
    print(-1)
