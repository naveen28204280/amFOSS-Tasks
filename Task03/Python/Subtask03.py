n=int(input("Enter a number: "))
if n%2==0:
    n=n+1
    print("This is an even number but here's the pattern for the next number:")
k=n//2
for i in range(k+1):
    print(" "*(k-i) + "*"*((2*i)+1))
for i in range(k):
    print(" "*(i+1)+ "*"*(n-2*(i+1)))