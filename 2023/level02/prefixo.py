n = int(input())
w1 = input()

m = int(input())
w2 = input()

resp = 0
i = 0

while True:
    if i == n or i == m:
        break
    if w1[i] == w2[i]:
        resp += 1
        i += 1
    else:
        break

print(resp)
