def f(str1):
    str1# = input()
    r = []
    for i in str1:
        if(ord('0') <= ord(i) <= ord('9')):
            r.append(i)
    # 输出要是一个整数，注意前导0问题：008---->8
    print(int(''.join(r)))
