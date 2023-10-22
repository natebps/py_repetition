s=n=0
t = float(input("N: "))
while True:    
    if t< 0 : break
    s += t
    n += 1
    t = float(input("N: "))
print("avg= ", (s/n))