# odd/even pairing
n = int(input())
if n == 1:
    print(1)
elif n == 2 or n == 3:
    print("NO SOLUTION")
else:
    evens = list(range(2, n+1, 2))
    odds = list(range(1, n+1, 2))
    print(*evens, *odds)
# half-half paring

