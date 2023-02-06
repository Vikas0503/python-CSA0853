m=input("ENTER THE MONTH --> ")
d=int(input("ENTER THE DAY --> "))
m=m.lower()
season=""
if m in "january february march april may june july august septmber october november december" and d>0 and d<=31:
    if m in "april may":
        season="SUMMER"
    if m=="march" and d>=20:
        season="SUMMER"
    if m=="june" and d<21:
        season="SUMMER"
    if m in "july august":
        season="SPRING"
    if m=="june" and d>=21:
        season="SPRING"
    if m=="september" and d<22:
        season="SPRING"
    if m in "october november":
        season="FALL"
    if m=="september" and d>=22:
        season="FALL"
    if m=="december" and d<21:
        season="FALL"
    if m in "january february":
        season="WINTER"
    if m=="dember" and d>=21:
        season="WINTER"
    if m=="march" and d<20:
        season="WINTER"
    print("THE SEASON IS --> ",season)
else:
    print("INVALID INPUT")
Footer
