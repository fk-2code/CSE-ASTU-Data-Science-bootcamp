text=input('enter text:')
vowel=0
lists=["a","e","i","o","u"]
for i in text:
    for vowels in lists:
        if i==vowels:
            vowel+=1
print(vowel)


