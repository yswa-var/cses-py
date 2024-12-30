n = int(input())
ans = []

while n!=1:
    ans.append(int(n))
    if n%2==0:
        n = n/2
    else:
        n = n * 3 + 1

ans.append(1)
print(" ".join(map(str, ans)))