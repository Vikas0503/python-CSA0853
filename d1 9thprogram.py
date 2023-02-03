E=[]
L=[]
T=int(input("number of people entered on cruise T:"))
print("Guestes entered are:")
for i in range(T):
    e=int(input("E:"))
    E.append(e)
print("Guestes left are:")
for i in range(T):
    l=int(input("L:"))
    L.append(l)
Sum=0
Max=0
for i in range(T):
    Sum+=E[i]-L[i]
    Max=max(Sum,Max)
print("Maximum number of guestes on cruise:",Max)
