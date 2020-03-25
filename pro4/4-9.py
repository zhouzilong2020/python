print("[1] apple\n[2] pear\n[3] orange\n[4] grape\n[0] exit", )
price = {'1':3.00, '2':2.50, '3':4.10, '4':10.20}
x = list(map(int, input().split()))

for i, num in enumerate(x):
    if num == 0 or i > 4:
        break
    p = price.get(f'{num}', 0)
    print(f"price = {p:.2f}")
