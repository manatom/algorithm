"""
백준 3273번 두  수의 합
수열을 정렬한 뒤 풀이한다.
정렬된 수열 seq에 대하여 seq[l] + seq[r] = x 인 l과 r을 찾을 때
 l을 1부터 잡고 비교한다. 이때 다른 수 r은 가장 큰 수에서 시작한다.
 1.만약 seq[l] + seq[r] > x이면 r을 줄여가며 l과 비교한다.
 그런데 자연수 n에 대해 seq[l+n] + seq[r] > seq[l] + seq[r] > x이므로 l보다 더 큰 수를 대입할 때 r이상의 값은 대입할 필요가 없다.
 2.만약 seq[l] + seq[r] < x이면 r보다 작은 수 k에 대하여 seq[l] +seq[k] < seq[l] +seq[r] < x이므로 l에 대해 더이상 비교할 필요가
없으므로 l에 다음 수를 대입한다.
 3.만약 seq[l]과 seq[r]이 같으면 정답 카운터를 늘리고 중복된 값이 업으므로 l과 r이하의 수를 비교할 필요가 없다.그래서 다음 l값을 대입한다.
 1과 마찬가지로 r이상의 값에서는 더이상 고려할 필요없다.
 계속해서 대입을 하다 l과 r이 교차하는 순간부터는 더이상 비교를 할 필요가 없다.
"""
n = int(input())
seq = list(map(int,input().split()))
x = int(input())
l,r = 0, n-1
seq.sort()
ans = 0
while l <r:
    if seq[l] + seq[r] < x:
        l += 1
    elif seq[l] + seq[r] > x:
        r -= 1
    else:
        ans += 1
        l += 1
        r -= 1
print(ans)