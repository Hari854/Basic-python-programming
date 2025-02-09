n=int(input("Enter a number="))
c=n
s=0
while n!= 0:
  k = n%10
  s = s+(k**3)
  n= n//10
if c == s:
  print("Armstrong")
else:
  print("Not an Armstrong")