NXT = list(map(int,input().split()))
notideal = list(map(int,input().split()))

sculpt_ind = {}
for i in range(len(notideal)):
    sculpt_ind[i]=abs(notideal[i]-NXT[1])

sorted_sculpt = {k: v for k, v in sorted(sculpt_ind.items(), key=lambda item: item[1])}
ideal = []
for k, v in sorted_sculpt.items():
    if v == 0:
        ideal.append(k+1)
    if NXT[2]>0:
        if v<NXT[2]:
            NXT[2]-=v
            ideal.append(k+1)


if len(ideal)==0:
    print(0)
    print()
else:
    print(len(ideal))
    for item in ideal:
        print(item, end=' ')