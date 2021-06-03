"""

"""
import sys
text = sys.stdin.readline().rstrip()
pattern = sys.stdin.readline().rstrip()
def fx(pattern):
    ans = [0]
    j = 0
    for i in range(1,len(pattern)):
        while pattern[i] != pattern[j] and j >0:
            j = ans[j-1] #접미사가 일치하지 않으면 j에 그 전 수의 접미사를 대입
        if pattern[i] == pattern[j]:
            j +=1
            ans.append(j)
        else:
            ans.append(0)
    return ans
fi = fx(pattern)
j = 0
result = []
for i in range(len(text)):
    while text[i] != pattern[j] and j > 0:
        j = fi[j-1]
    if text[i] == pattern[j]:
        if j < len(pattern)-1:
            j += 1
        else:
            result.append(i-j+1)
            j = fi[j]
len_text = len(text)
len_pattern = len(pattern)
if result:
    print(len(result))
    print(*result)
else:
    print(0)