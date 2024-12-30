n = input()
m = 0
l = "X"
c = 0
for s in n:
    if s!=l:
        l = s
        c = 1
    else:
        c+=1
    m = max(c, m)
print(m)

