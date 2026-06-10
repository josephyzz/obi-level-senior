N = int(input())
array = list(map(int, input().split()))


B = [0] * N
L = 0
R = N - 1
moeda = 0

while L <= R:
    if B[L] < array[L] and B[R] < array[R]:
        B[L] += 1
        B[R] += 1
        moeda += 1
    else:
        if array == B:
            break
        if B[L] == array[L]:
            L += 1
            moeda += 1
        if B[R] == array[R]:
            R -= 1
            moeda += 1

if B == array:
    print(moeda)
else:
    print(-1)
