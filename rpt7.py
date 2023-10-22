a = int(input("A: "))
b = int(input("B: "))
s = 0

for i in range(a,b):
    t = 0
    for j in range(i+1,b+1):
        t += (i+j)
    s += (-1)**i *t
print(s)
