c = int(input())  # km por litro
d = int(input())  # distancia a percorrer
t = int(input())  # quanto tem

litros = d / c

compra = litros - t

if compra < 0:
    compra = 0

print(f"{compra:.1f}")
