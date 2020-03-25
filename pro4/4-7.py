N = int(input())
if N >0:
    scores = list(map(int, input().split()))
    cnt = 0
    for i, score in enumerate(scores):
        if score >= 60:
            cnt+=1
    print(f"average = {sum(scores)/N:.1f}")
    print(f"count = {cnt}")
else:
    print("average = 0.0")
    print("count = 0")