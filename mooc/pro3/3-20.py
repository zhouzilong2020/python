str1 = list(input().strip())
len_str = len(str1)
l = 0
r = len_str-1

print(''.join(str1))
while l < r:
    if str1[l] == str1[r]:
        l+=1
        r-=1
    else:
        print("No")
        break
if l >= r:
    print("Yes")
