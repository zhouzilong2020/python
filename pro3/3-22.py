word1 = input().split()
word2 = input().split()
word1 = list(''.join(word1))
word2 = list(''.join(word2))
cnt = {}

if len(word1) != len(word2):
    print("no")
else:
    for i in word1:
        if i not in cnt:
            cnt[i] = 1
        else:
            cnt[i] += 1

    for i in word2:
        if i not in cnt or cnt[i] == 0:
            print("no")
            break
        else:
            cnt[i]-=1
    else:
        print("yes")