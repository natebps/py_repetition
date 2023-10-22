n = int(input("N: "))
a = int(input("A: "))

mn = mx = a
c = 0
if a < 0 : c = 1

for k in range (n-1):
    if a > mx : mx = a
    if a < mx : mn = a
    if a < 0 : c += 1
print((mx -mn),c)


