"""
유니온 파운드를 이용해 이들을 표시하자.
그리고 새롭게 잇는 점 a와 b에 대해 만약 a와 b가 같은 루트부모를 가지고 있다면 a와 b의 부모를 찾아올라가면 어느 한점에서는 만나게 되어있다.
만나는 점에서 a까지, 만나는 점에서 b까지 와 ab를 잇는 선분을 가지고 사이클을 만들 수 있다.
따라서 새로 긋는 선분의 두 점이 같은 루트 부모를 가지고 있다면 새로 그어진 선분은 새로운 사이클을 만들어 낸다.
"""
import sys
n,m =map(int,sys.stdin.readline().split())
class unionfind:
    def __init__(self,a):
        self.parents = [x for x in range(a)]
        self.rank = [1 for _ in range(a)]
    def find(self,A):
        parent = self.parents[A]
        if parent == A:
            return parent
        else:
            return self.find(parent)
    def union(self,A,B):
        parentA = self.find(A)
        parentB = self.find(B)
        if self.rank[parentA] < self.rank[parentB]:
            self.parents[parentA] = parentB
            self.rank[parentB] += self.rank[parentA]
        else:
            self.parents[parentB] = parentA
            self.rank[parentA] += self.rank[parentB]
p = unionfind(n)
ans = 0
for num in range(1,m+1):
    a,b = map(int,sys.stdin.readline().split())
    find_a,find_b = p.find(a),p.find(b)
    if find_a == find_b:
        ans = num
        break
    p.union(a,b)
print(ans)