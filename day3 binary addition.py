a=(input("ENTER BINARY NUMBER 1 --> "))
b=(input("ENTER BINARY JUMBER 2 --> "))
aint=0
bint=0
for i in range(len(a)):
    aint+=int(a[i])*2**i
for i in range(len(b)):
    bint=int(b[i])*2**i
c=bin(aint+bint)
cc=""
for i in range(1,len(str(c))):
    if c[i]!='b':
        cc+=str(c[i])
print("THE OUTPUT IS ",cc)
