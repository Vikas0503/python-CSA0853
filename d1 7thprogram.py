def length(n,start):
    if(n==0):
        return 1
    count=0
    for i in range(start,5):
        count=count+length(n-1,i)
    return count
def vowelString(n):
    return length(n,0)
n=int(input("Enter the value of N="))
if(n<0):
    print("INVALID INPUT")
    print("NEGATIVE VALUE")
    print("ENTER A POSITIVE INTEGER")
else:
    print(vowelString(n))