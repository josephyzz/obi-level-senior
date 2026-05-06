"""
Zero para Cancelar.
"""
# https://olimpiada.ic.unicamp.br/pratique/ps/2021/f1/zero/
# Point 100/100
# t = 0,017s / 1,4s
# memory 4.8 MB/ 64 MB

# By josephyzz

n = int(input())
sequencia = [int(input()) for i in range(n)]


sequencia.reverse()

sum = 0
num_zeros = 0
for numero in sequencia:
    if numero == 0:
        num_zeros += 1
    else:
        if num_zeros > 0:
            num_zeros -= 1
        else:
            sum += numero

print(sum)
