n = int(input())
a = list(map(int, input().split()))

total = sum(a)
prefix = 0

for i in range(n-1):
    prefix += a[i]
    if prefix == total - prefix:
        print(i+1)
        break
