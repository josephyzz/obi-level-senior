A = [int(input()) for _ in range(2)]
B = [int(input()) for _ in range(2)]
C = [int(input()) for _ in range(2)]


primeiro = max(A[0], B[0], C[0])

ultimo = min(A[1], B[1], C[1])

if primeiro > ultimo:
    print(0)
elif primeiro < ultimo:
    print(ultimo - primeiro + 1)
else:
    print(1)
