l1=[]
l2=[]
c1=[]
c2=[]
n=int(input("Enter the number of elements in L1="))
for i in range(0,n):
    a=int(input("Enter the elements="))
    l1.append(a)
    c1.append(l1[i])
print(c1)
m=int(input("Enter the number of elements in L2= "))
for i in range(0,m):
    b=int(input("Enter the elements="))
    l2.append(b)
    c2.append(l2[i])
print(c2)
c3=c1+c2
c3.sort()
print(c3)