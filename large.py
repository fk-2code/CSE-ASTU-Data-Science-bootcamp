def find_lar(num):
    largest=num[0]
    for i in num:
        if i > largest:
            largest = i
    return largest
nums=list(map(int,input().split()))
maxi=find_lar(nums)
print(maxi)