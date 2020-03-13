str1 = list(input())
N = len(str1)
for i in range(N):
    if str1[i].isalpha():
        if str1[i].isupper():
            str1[i] = str1[i].lower() 
        else:
            str1[i] = str1[i].upper()
print(''.join(str1)[ : -1])
