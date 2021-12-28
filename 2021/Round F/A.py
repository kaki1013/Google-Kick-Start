def sum_1_to_n(n):
    return (n*(n+1))//2


T = int(input())
for test in range(1, T+1):
    ans = 0
    N = int(input())
    S = list(map(int, list(input())))
    have_list = [i for i in range(N) if S[i]]  # 0 start
    l = len(have_list)
    ans += sum_1_to_n(have_list[0])
    for i in range(l-1):
        diff = have_list[i+1] - have_list[i] - 1
        ans += sum_1_to_n(diff//2)
        ans += sum_1_to_n(diff - diff//2)
    ans += sum_1_to_n(N - have_list[-1] - 1)
    print(f"Case #{test}: {ans}")
