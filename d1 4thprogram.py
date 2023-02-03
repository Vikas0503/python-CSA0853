try:
	n=int(input("enter any number:"))
	temp=n
	r=0
	while(n>0):
		d=n%10;
		r=r*10+d;
		n=n//10;
	if(temp==r):
		print("true")
		print("the value is a palindrome")
	else:
		print("false")
		print("the value is not a palindrome")
except ValueError:
		print("invalid input")
		print("enter a numeric value")
		