from re import L


a = int(input("INPUT NUMBER: "))
l =[]
for i  in range(1,a):
   if i%3 == 0 & i%5 == 0:
    l.append(i+1)
    an_integers = " ".join(str(e)for e in l)
    an_integer =  int(an_integers)
    aa = 3 + 5 + an_integer
    print(aa)

   
   
    
    """s = str(i) 
    m = map(int,s)  
    l = list(m) 
    print(l) """

