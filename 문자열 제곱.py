"""
풀이법 kmp알고리즘의 방법을 이용해서 풀었다.
우선 text의 실패함수를 구한다.
text의 한자씩 비교하는 풀이이다. j는 비교하는 숫자이고 0부터 시작한다. x는 x번째 숫자까지 반복된다는 의미이다. 역시 0부터 시작한다.
kmp알고리즘과 마찬가지로 text[i]와 text[j]가 같거나 j가 0이 될때따기 j를 갱신한다. 이떄 text[j]와 text[i]가 일치하지 않는 다는것은
x번째 숫자까지의 숫자의 반복이 되지 않는다는 것이므로 x의 값을 늘린다. 만약에 text[i]와 text[j]가 일치한다고하자. 그러면 만약 j가 x와 같다면
즉 x번째까지 반복이 되는 것이라면 j를 0으로 갱신해 그다음 문자들에서도 x번째글자까지의 문자가 반봅되는지 확인힌다. 그리고 1번 반복되어다는 뜻이므로
정답을 하나 늘린다. j가 아직 x보다 작다면 j값을 1늘린다. 단약 text[i]와 text[j]가 같지 않다면 지금까지의 반복은 전혀 의미가 없고 앞으로 살펴야 할것은
i번째 까지의 문자들이 이후에 반복되는지를 살펴야한다. 그래서 이경우 정답값을 다시 0으로 갱신하고 x는 i로 갱신한다. 이제 j값을 갱신해야하는데 j값은 x보다 무조건
작아야하기떄문에 작아질때까지 j를 실패함수의 j-1 값으로 갱신한다.
이렇게 루프를 모두 돌면 ans가 있을 것이다. 그리고 어쩌면 j가 아직 x에 도달하지 못하고 끝났을 경우도 있다. 이 경우에는 반복이 되지 않는다는 의미이므로 ans값이
필요가 없다. 결국 j값과 x같아져 0으로 갱신되었을때만 정답값이 의미가 있다.
"""
import sys
def fx(text):
    ans = [0]
    j = 0
    for i in range(1,len(text)):
        while text[j] != text[i] and j >0:
            j = ans[j-1]
        if text[i] == text[j]:
            j += 1
        ans.append(j)
    return ans
text = sys.stdin.readline().rstrip()
while text != '.':
    f = fx(text)
    j = 0
    x = 0
    ans =0
    for i in range(1,len(text)):
        while text[i] != text[j] and j>0:
            j = f[j-1]
            x += 1
        if text[i] == text[j]:
            if j == x:
                j=0
                ans += 1
            else:
                j += 1
        else:
            ans = 0
            x = i
            while j >= x:
                j = f[j-1]
    if j == 0:
        print(ans+1)
    else:
        print(1)
    text=sys.stdin.readline().rstrip()
"""
이 해결방법은 백준에서 시간초과에 결렸다. 다만 pypy3로는 통과했다.
이것보다 더 효율적인 방법은 실패함수의 마지막 값을 구한뒤(이하x) 전체 문자열의 길이(이햐 m)에서 x를 뺸 값(아하w)을 구한다.
그리고 m이 w으로 나누어떨어진다면 이는 w길이의 문자열이 m/w만큼의 반복이라고 볼 수 있다. 
문제를 푸는 과정에서 이 풀이는 생각하지 못했다.
"""