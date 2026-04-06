def is_prime(n):
    if n <=1:
        return False
    for i in range(2,int(n**0.5) +1):
        if n%i==0:
            return False
    return True
num=int(input("enter a number:"))
if is_prime(num):
    print("it is prime")
else:
    print("it is not prime")


