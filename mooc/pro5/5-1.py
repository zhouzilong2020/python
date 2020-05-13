day = {
    1:"Mon",
    2:"Tue",
    3:"Wed",
    4:"Thu",
    5:"Fri",
    6:"Sat",
    7:"Sun"}
d = int(input())
if (d  in range(1,8)):
    print(f"{day[d]}")
else:
    pass
