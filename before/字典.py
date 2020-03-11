#dict函数
a = [('a','b'),('1','2')]
a = dict(a)
print(a)
#{'a': 'b', '1': '2'}
print ('a' in a)

#字典：：{}
#元组：：()
#序列：：[]

#序列解包 Sequence unpacking
# 为函数的返回值默认为组元组，便可以分别赋值

char = "this is a random string"
if char.endswith('g'):
    print("yes!")
else :
    print("NO")

# 逻辑短路 
# 在所有逻辑运算中 只要满足了条件 则立马返回该值 否则返回另外一个
a = 1
# or中满足一个即可，返回的是1
a = 1 or 2
print(a)
# and要两个都满足，因为a！=2 所以直接返回第二个元素
a = 2 and 111
print(a)


a = input("Your name is?") or "unknown"
print(a)