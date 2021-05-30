"""
백준 11054번 -가장 긴 바이토닉 부분 수열-
다이나믹 프로그래밍을 이용한 풀이
 이 문제는 다이나믹 프로그래밍을 통해 풀 수 있다.
 - j번째 수까지의 바이토닉 수열은 그 이전 단계의 바이토닉 수열에 j번째 수를 추가한 것이라서 이전 단계의 상태를 이용하여 풀 수 있기 때문에
 다이나믹 프로그래밍을 이용해 풀 수 있다.
 수열에서 j번째 수에 대해 바이토닉 수열을 찾는 경우 그 앞에 있는 수들을 하나하나 대입.
 만약 j번째 수가 그 수(i)보다 크면 바이토닉 수열은 증가하는 수열로만 존재할 수 있다.
 만약 j번째 수가 i보다 작으면 j번째 열까지의 가능한 바이토닉 수열은 i번 째까지 증가하다가 j번째에서 감소하는 수열(increase[i]+1)과
i까지의 바이토닉 수열에서 j를 넣은 수열(decrease[i]+1)로 구분할 수있다.
 이 두가지 경우중 큰 쪽이 j까지의 바이토닉 수열중에 가장 큰 값이다.
"""
n = int(input())
sequence = list(map(int,input().split()))
increase = [1 for _ in range(n)]
decrease = [1 for _ in range(n)]
for i in range(n):
    for j in range(i):
        if sequence[i] > sequence[j]:
            if increase[i] <= increase[j]:
                increase[i] = increase[j] + 1
        if sequence[i] < sequence[j]:
            x = max(increase[j],decrease[j])
            if decrease[i] <= x:
                decrease[i] = x + 1
print(max(max(increase),max(decrease)))
