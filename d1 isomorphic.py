def isisomorphic(s1,s2):
    if len(s1)!=len(s2):
        return False
    else:
        d1,d2={},{}
        for i in range(len(s1)):
            a,b=s1[i],s2[i]
            if(a not in d1):
                d1[a]=b
            if(b not in d2):
                d2[b]=a
            if(d1[a]!=b or d2[b]!=a):
                return False
        return True
s1=input("s=")
s2=input("t=")
print(isisomorphic(s1,s2))