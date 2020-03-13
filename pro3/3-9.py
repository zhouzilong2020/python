# 英文辅音字母是除A、E、I、O、U以外的字母。本题要求编写程序，统计给定字符串中大写辅音字母的个数。
# 输入格式：
# 输入在一行中给出一个不超过80个字符、并以回车结束的字符串。
# 输出格式：
# 输出在一行中给出字符串中大写辅音字母的个数。
# 输入样例：
# HELLO World!

# 输出样例：
# 4
vowel = ['A', 'E', 'I', 'O', 'U']
str1 = list(input())
cnt = 0
for i in str1:
    if i.isupper() and i.isalpha() and i not in vowel:
        cnt+=1
print(f"{cnt}")