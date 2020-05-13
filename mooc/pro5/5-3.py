x = int(input())
operator = input()
y = int(input())
dic = {
    '+':'x+y',
    '-':'x-y',
    '*':'x*y',
    '/':"x/y if y != 0 else 'divided by zero'"}
result = eval(dic.get(operator))
if type(result) == str:
    print(result)
else:
    print(f"{result:.2f}")