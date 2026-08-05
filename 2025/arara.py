N, M = map(int, input().split())

space = ((N - 1) * 4) + N


print("N" if space > M else "S")
