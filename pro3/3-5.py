def f(str1):
    str1# = input()
    r = []
    for i in str1:
        if(ord('0') <= ord(i) <= ord('9')):
            r.append(i)
    print(''.join(r))
    
f("l")
