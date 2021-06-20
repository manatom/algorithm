""" 백준 16496번- 큰 수 만들기
 파이썬에서 제공하는 단순 정렬로는 문제가 해결되지 않는다.
 30과 3을 비교할때 가능한 수 303과 3343중 330이 더 크다. 이런 경우에 3이 30보다 더 크다.
 a와 b를 생각할때 비교해야하는 것은 a+b인 문자열과 b+a인 문자열이다.
 만약 a+b> b+a라면 a가 b보다 더 먼저 와야하고 a+b<b+a라면 b가 더 먼저와야하고 둘이 같다면 아무것이나 먼저와도 상관 없다
 그래서 a+b와 b+a를 비교한다면 두 숫자 중 어떠 숫자가 더 먼저와야하는지 알 수 있다.
 그런데 a>b이고 b>c아면 a>c이다. 그렇기 때문에 일일이 비교하여 정렬할 필요가 없다. 삽입 정렬을 통해 구현했다.
compare 함수의 기댓값x(x번째 만에 찾을 것으로 기대하는 값)는 ∑ k* (1/26)**(k-1) * (25/26) * k이므로1/1/26 =  26,상수시간이다.
최악의 경우 역시
삽입 정렬의 시간복잡도는 n**2이므로 이 알고리즘은 평균적으로 다항식 시간안에 가능하다.
"""
import sys
t = int(sys.stdin.readline())
strings = list(sys.stdin.readline().split())
def compare(a,b):
    x = a+b
    y = b+a
    for i in range(len(x)):
        if x[i] > y[i]:
            return 1
        elif x[i] < y[i]:
            return 0
    return 0
""" 같은 방법 둘을 더하지 않고 각자의 길이에 대한 나머지로 i를 정했다.
    l = max(x,y)
    i = 0
    while i <l:
        if a[i%x] > b[i%y]:
            return 1
        elif a[i%x] < b[i%y]:
            return 0
        else:
            i+=1
    return 0
"""
for i in range(1,len(strings)): #삽입정렬
    x = i
    j = x-1
    while j >=0:
        if conpare(strings[i],strings[j]):
            strings[i],strings[j] = strings[j],strings[i]
            i -= 1
            j -= 1
        else:
            break
strings = list(map(str,strings))
print(int(''.join(strings)))