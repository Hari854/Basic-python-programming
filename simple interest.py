principal=float(input("principal="))
rate=float(input("rate="))
time=float(input("time="))
def simple_interest(principal, rate, time):
    return (principal * rate * time) / 100

print("Simple Interest (P=",principal,", R=",rate,", T=",time,"years):", simple_interest(principal, rate, time))