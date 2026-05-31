"""
Garamana
"""
# https://olimpiada.ic.unicamp.br/pratique/ps/2020/f1/garamana/
# # Points 100/100
# t = 0,026s / 0,1s
# memory 4.0 MB/ 64 MB

# By josephyzz

# TODO:
# 1 : Contar as repetição em p
# 2 : Comparar os p com os de a
# 3 : Caso tenha letra diferente de P return N

from collections import Counter

p = input()
a = input()

freq = Counter(p)

passed = True

for c in a:
    if c == '*':
        continue

    if freq[c] > 0:
        freq[c] -= 1
    else:
        passed = False

print('S' if passed else 'N')
