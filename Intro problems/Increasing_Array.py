n = int(input())
e = list(map(int, input().split()))
c = 0
for i in range(1, n):
    a, b = e[i-1], e[i]
    if a > b:
        c += a-b
        e[i] = a
print(c)
