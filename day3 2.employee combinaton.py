import random
c=input("ENTER THE INITIAL COMBINATION --> ")
l=[]
f=1
for i in range(1,len(c)+1):
    f*=i
    i=1
while i<=f:
    k=1
    a=str(c[random.randint(0,len(c)-1)])
    while k<len(c):
        m=str(c[random.randint(0,len(c)-1)])
        if m not in a:
            a+=m
            k+=1
    if a not in l:
        l.append(a)
        i+=1
for a in l:
    print(a)
Footer
