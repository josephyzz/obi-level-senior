N = int(input())

e_vantajoso = []

for i in range(N):
    E, A, G = input().split()

    if float(A) <= float(G) * 0.7:
        e_vantajoso.append(E)

if e_vantajoso:
    [print(e) for e in e_vantajoso]
else:
    print('*')
