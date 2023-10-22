a = int(input("A: "))
b = int(input("B: "))
s = 0

for i in range(a,b):
    for j in range(i+1,b+1):
        s += (-1)**i * (i+j)
print(s)