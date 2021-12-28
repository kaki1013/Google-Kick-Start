# 시작하는 날만 체크해도 충분
# sol1: 1. 각 (시작) 날짜에 대해서 갈 수 있는 attr을 탐색 2. happiness가 최대가 되도록 heapq에서 뽑아냄
import heapq
T = int(input())
for test in range(1, T+1):
    ans = 0
    D, N, K = map(int, input().split())
    attraction = sorted([tuple(map(int, input().split())) for _ in range(N)], key=lambda x:x[1])  # h s e
    for i in range(N):
        ss = attraction[i][1]
        temp = 0
        maximum = []  # go_able
        for n in range(i+1):
            h, s, e = attraction[n]
            if s <= ss <= e:
                heapq.heappush(maximum, -h)
        for k in range(K):
            if maximum:
                temp -= heapq.heappop(maximum)
        ans = max(ans, temp)
    print(f"Case #{test}: {ans}")

# sol2 : Mansurbek
# https://codingcompetitions.withgoogle.com/kickstart/submissions/0000000000435bae/TWFuc3VyYmVr
import bisect

T = int(input())
for test in range(1, T+1):
    d, n, k = map(int, input().split())
    arr = []
    brr = []
    for i in range(n):
        h, s, e = map(int, input().split())
        arr.append([s, h])
        brr.append([e, h])
    arr.sort()
    brr.sort()
    ans = 0
    s = 0
    arr_in = []
    arr_ex = []
    last = 0
    first = 0
    for i in range(1, d + 1):
        while first < n and arr[first][0] == i:
            if len(arr_in) < k or (len(arr_in) > 0 and arr_in[0] < arr[first][1]):
                pos = bisect.bisect_left(arr_in, arr[first][1])
                arr_in.insert(pos, arr[first][1])
                s += arr_in[pos]
            else:
                pos = bisect.bisect_left(arr_ex, arr[first][1])
                arr_ex.insert(pos, arr[first][1])
            first += 1
        while last < n and brr[last][0] == i - 1:
            if len(arr_ex) > 0 and arr_ex[-1] >= brr[last][1]:
                pos = bisect.bisect_left(arr_ex, brr[last][1])
                arr_ex.pop(pos)
            else:
                pos = bisect.bisect_left(arr_in, brr[last][1])
                s -= arr_in[pos]
                arr_in.pop(pos)
            last += 1

        while len(arr_in) < k and len(arr_ex) > 0:
            val = arr_ex[-1]
            arr_ex.pop(-1)
            pos = bisect.bisect_left(arr_in, val)
            arr_in.insert(pos, val)
            s += arr_in[pos]
        while len(arr_in) > k:
            val = arr_in[0]
            s -= arr_in[0]
            arr_in.pop(0)

            pos = bisect.bisect_left(arr_ex, val)
            arr_ex.insert(pos, val)
        ans = max(ans, s)
    print('Case #{}: {}'.format(test, ans))
