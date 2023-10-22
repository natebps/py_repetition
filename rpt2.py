q = int(input("Number:"))
for k in range(2,q):
    if q%k==0:
        print(q,'composite')
        break
else:
    print(q,'prime')