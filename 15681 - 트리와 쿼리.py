"""
두가지 과정이 필요하다. 트리를 만드는 과정, 또 부분트리의 수를 구하는 과정 이 두가지를 재귀를 이용한 함수로 구현한다.
 트리는 사이클이 없기 떄문에 한 점에서 시작해 다시 그 점으로 돌아오지 않기때문에 재귀로 구현이 가능하다.
 트리를 만드는 함수(make_tee)는 트리의 첫점 루트에서 시작한다. 이 함수는 점과 그 부모를 필요로 한다. 첫점,즉 루트는 부모가 없기 때문에
부모에 0을 대입한다. 그 점과 연결된 점들이 만약 자신의 부뫄 아니라면 그 점의 자손에 연결된 점을 추가한뒤 연결된 점과 연결된 점의 부모가된 원래의점
을 재귀함수에 대입한다. 이 과정이 마지막 층의 점까지 된다면 루트에서 시작하는 트리를 구할 수 있다.
 트리의 길이를 구하는 함수 역시 구할 수 있다. 한 점이 있다면 그 점의 트리의 길이는 자손들을 루트로 하는 트리의 길이와 자기자신도 포함되기에 1을 더한 값일 것이다
 이 역시 재귀를 이용해 구현하면 루트에서 시작해 그의 자손들에 대해 재귀를 통해 자손의 자손,자손의 자소까진 나아가 며 자손트리의 값을 구할 수 있다. 이 때 입력으로
 주어질 점에 대해 그 점의 트리의 길이를 그떄 구하는 것이 아니라 루트로부터 시작되는 갑을 구하면 그 과정에서 그 자손들의 함수 값을 모두 구할 수 있기때문에 미리
 구해놓는다. 그리고 구하고 싶은 점이 입력할때마다 그 값을 적어놓은 배열에서 그 값을 보여주면 된다.
"""
import sys
n,r,q =map(int,sys.stdin.readline().split())
connect = [[] for _ in range(n+1)]
sys.setrecursionlimit(2000000)
for _ in range(n-1):
    a,b = map(int,sys.stdin.readline().split())
    connect[a].append(b)
    connect[b].append(a)
springs = [[] for _ in range(n+1)]
def make_tree(num,parent):
    for i in connect[num]:
        if i != parent:
            springs[num].append(i)
            make_tree(i,num)
quary = [0 for _ in range(n+1)]
def findquary(n):
    result = 1
    for i in springs[n]:
        x = findquary(i)
        result += x
    quary[n] = result
    return result
make_tree(r,0)
findquary(r)
for _ in range(q):
    a = int(sys.stdin.readline())
    print(quary[a])