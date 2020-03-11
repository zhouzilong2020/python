
char = input()
str1 = input()
pos = []
i = 0
cnt = str1.count(char)
while i != -1 and cnt >0:
    i = str1.find(char, i)
    cnt-=1
    pos.append(i)
    i+=1
    
if len(pos) == 0 :
    print("Not Found")
else :
    print(f"index = {pos[-1]}")
