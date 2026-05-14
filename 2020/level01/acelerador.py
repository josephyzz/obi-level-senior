"""
Acelerador de particula
"""
# https://olimpiada.ic.unicamp.br/pratique/ps/2020/f1/acelerador/
# Points 100/100
# t = 0,032s / 0,1s
# memory 4.16 MB/ 64 MB

# Record = 08min

# By josephyzz

distancia = int(input())

distancia -= 3

while True:
    if distancia >= 8:
        distancia -= 8
    else:
        match distancia:
            case 3:
                print(1)
                break
            case 4:
                print(2)
                break
            case 5:
                print(3)
                break
            case _:
                break
        break
