q = int(input("Number:"))
found = False
for k in range(2,q):
    if q%k==0:
        print(q,'composite')
        found = True
        break
if not found :
    print(q,'prime')