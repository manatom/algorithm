"""
중국인의 나머지 정리를 이용한 합동방정식 풀이
- 중국인의 나머지정리는 x = a1 mod(m1) ,x = a2 mod(m2) ... x = an mod(mn)를 만족하는 x값을 구한다.
x를 m1로 나누면 나머지는 a1이 나와야 하고 mn으로 나누면 나머지가 an이 나와야 한다.
그래서 x를 다음과 같이 표시할 수 있다. a1에 대해 x = a1 * 1 + a2 * m2*k2 +a3 * m3* k3 ... 그
다시말해 x를 이루는 다항중에 n번째 항만 mn에 나누어 떨어지지 않고 그 계수가 an아라면 x를 mn으로 나눈 나머지는 a이 될 것이다.
그래서  M 을 m1 * m2 * ... * mn 이라고 하면 M/mn은 mn에 나누어 떨어지지 않으면서 m1,m2,... 에는 나누어떨어질 것이다.
그렇다면 n번째 항에 대해 an * M/mn 으로 하면 M/n을 mn으로 나눈 나머지가 있기 떄문에 나머지가 an이 되지 못한다. an외의 값들을 
1로 만들어야한다. 그런데 M/mn과 mn은 서로 서로소이다. 그렇기 떄문에 M/mn 모둘료 mn은 역을 가진다. 이 역을 찾아 식에 곱하면
an * sn * M/mn (sn은 MN/m mod mn의 역)이 되고 an * sn * M/mn mod mn은 an * 1= an이다.
그래서 x =  a1 * s1 * M/m1 + a2 * s2 * M/m2 ....으로 나타낼 수 있다.
그런데 주의할 점은 나누는 값들이 서로소일떄에만 가능하다는 점이다. 서로간에 1이아닌 공약수가 있으면 모둘료 연산간에 다른 값이 나올 수도
있기떄문이다. 만약 서로 소로소가 아니라면 이들의 공약수를 이용해 값을 수정해야한다 문제에서 주어진 수 15,28,19가 서로소이기때문에 문제에서는
그냥 사용할 수 있다.
각각의 값들은 어렵지 않게 구할 수 있고 따라서 x의 값을 구할 수 있다.
구현...
  구현은 어렵지 않다. 우선 모듈로 역을 구해야하기때문에 확장 유클리드 호제법을 이용해 이들의 베주 전개값을 구하고 그로 모듈로 역을 구하면된다
  그럼 an과 sn은 쉽게 구할 수 있으므로 몇번의 반복문을 통해 x값을 구할 수 있다. 그런데 여기서는 나머지가 0인 경우가 그 나누는 수의 수로 바뀌어야
  한다는 점에서 만약 정답이 0이었다면 정답은 나누는 수들의 곱으로 바꾸어주어야한다. 
"""
def uclid(a,b):
    p = []
    st = [(1,0),(0,1)]
    while b != 0:
        p.append(a//b)
        x = a % b
        a,b = b,x
    for i in range(len(p)-1):
        s = st[-2][0] - p[i] * st[-1][0]
        t =st[-2][1] - p[i] * st[-1][1]
        st.append((s,t))

    return a,st[-1]
def find_yeok(n,m):
    x,z = uclid(n,m)
    return z[0]
def chinense(nums_list):
    p = 1
    for i in nums_list:
        p *= i[1]
    x = 0
    for i in range(len(nums_list)):
        M = p//nums_list[i][1]
        x += nums_list[i][0] * M * find_yeok(M,nums_list[i][1])
    if x %p:
        return x%p
    else:
        return p
x,y,z = map(int,input().split())
li = [(x,15),(y,28),(z,19)]
print(chinense(li))
