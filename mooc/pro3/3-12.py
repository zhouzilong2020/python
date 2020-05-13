str1 = list(input())
N = len(str1)
A = ord('A')
mid_pos = ord('A')+12
for i in range(N):
    if str1[i].isalpha() and str1[i].isupper():
        ascii_code = ord(str1[i])
        str1[i] = chr(2*mid_pos - ascii_code +1)

print(''.join(str1))