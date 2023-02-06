def delchar(a,b):
    c=len(a)
    d=""
    for i in range(0,c):
        if a[i] not in b:
            d+=a[i]
            print("String after deletion :",d)
            b=input("Enter character to be deleted :")
            print("String after deletion :",d)



