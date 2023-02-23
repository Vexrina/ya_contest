n = int(input())#кол-во клавиш
c = list(map(int,input().split()))# id клавиши
r = list(map(int,input().split()))#номер ряда
k = int(input())#колво символов в реферате
s = list(map(int,input().split()))#буквы реферата
result = 0
cr = {}
for i in range(len(c)):
    cr[c[i]] = r[i]

for i in range(1, len(s)):
    if cr[s[i]]!=cr[s[i-1]]:
        result += 1
    
print(result)