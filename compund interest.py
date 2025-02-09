principal=float(input("principal="))
rate=float(input("rate="))
time=float(input("time="))
def compound_interest(principal, rate, time):
    return principal * ((1 + rate / 100) ** time) - principal

print("Compound Interest (P=",principal,", R=",rate,", T=",time," years):", compound_interest(principal,rate,time))