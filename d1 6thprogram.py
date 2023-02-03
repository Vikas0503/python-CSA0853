def maxArea(A,len):
    area=0
    for i in range(len):
        for j in range(i+1,len):
            area=max(area,min(A[j],A[i])*(j-i))
    return area
b=[]
a=int(input("Enter the number of elements:"))
print("Enter the elements:")
for i in range(0,a):
    c=int(input())
    b.append(c)
print("Array=",b)
print("maximum area of water=",maxArea(b,a))