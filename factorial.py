def factorial(n):
    if n < 0:
        return"factorial cannot do negative numbers"
    elif n==0 or n==1:
        return 1
    else:
        return n* factorial(n-1)
num=int(input())
fact=factorial(num)
print(fact)