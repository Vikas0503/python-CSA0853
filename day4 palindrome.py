a=input("ENTER PHRASE --> ")
a=a.lower()
anew=""
for i in a:
    if i.isalpha():
        anew+=i
if anew==anew[::-1]:
    print("PALINDROME!")
else:
    print("NOT PALINDROME")
