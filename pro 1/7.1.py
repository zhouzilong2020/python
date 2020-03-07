A, B, C = input().split()
A, B, C = int(A), int(B), int(C)
if A > B:
    A, B = B, A
if A > C:
    A, C = C, A
if B > C:
    B, C = C, B
print(f"{A}->{B}->{C}")