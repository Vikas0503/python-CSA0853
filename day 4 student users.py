t=int(input("ENTER THE TOTAL USERS --> "))
s=int(input("ENTER THE STAFF USERS --> "))
if t>0 or s>0 or t>s:
    nt=s/3
    s=t-(s+nt)
    print("STUDENT USERS --> ",int(s))
else:
    print("INVALID INPUT")
Footer
