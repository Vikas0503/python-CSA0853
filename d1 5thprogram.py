a=int(input("Enter the number of fresh loaves purchased:"))
b=int(input("Enter the number of day old loaves purchased:"))
r=185
n=a*r
o=(b*r)-(b*r)*(60/100)
tot=n+o
print("Regular Price:",r)
print("Amount of new loaves:",n)
print("Amount of day old loaves:",o)
print("Total amount:",tot)