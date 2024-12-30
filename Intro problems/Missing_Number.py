n = int(input())
elements = sum(list(map(int, input().split())))
nsum = n*(n+1)/2
print(int(nsum - elements))