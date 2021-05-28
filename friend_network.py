import sys
class unionfind:
    def __init__(self):
        self.dic = {}
        self.parent = [-1]
        self.rank = [-1]
        self.lens = 1
    def append(self,n):
        self.dic[n] = self.lens
        self.parent.append(self.lens)
        self.rank.append(1)
        self.lens += 1
        return self.dic[n]
    def find(self, w):
        a = self.dic[w]
        while self.parent[a] != a:
            a = self.parent[a]
        return self.parent[a]
    def union(self,x,y):
        if x != y:
            if self.rank[x] < self.rank[y]:
                self.parent[x] = self.parent[y]
                self.rank[y] += self.rank[x]
                return self.rank[y]
            else:
                self.parent[y] = self.parent[x]
                self.rank[x] += self.rank[y]
                return self.rank[x]
        else:
            return self.rank[x]
    def find_friends(self,q,e):
        try:
            X = self.find(q)
        except:
            X = self.append(q)
        try:
            Y = self.find(e)
        except:
            Y = self.append(e)
        num_friends = self.union(X,Y)
        return num_friends

if __name__ == "__main__":
    T = int(sys.stdin.readline())
    for _ in range(T):
        un = unionfind()
        F = int(sys.stdin.readline())
        for _ in range(F):
            x,y = sys.stdin.readline().split()
            print(un.find_friends(x,y))
