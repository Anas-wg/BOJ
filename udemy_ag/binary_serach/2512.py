import sys

# Input reading
N = int(sys.stdin.readline().rstrip())

city = list(map(int, sys.stdin.readline().split()))

M = int(sys.stdin.readline().rstrip())

city.sort()

lo = 0
hi = max(city)
mid = (lo + hi) // 2
ans = 0

# 이분 탐색
def is_possible(mid):
    return sum (min(elem, mid) for elem in city) <= M
        

while lo <= hi:
    if is_possible(mid):
        # mid까지 확인했기 때문
        lo = mid + 1
        ans = mid
    else:
        hi = mid - 1

    mid = (lo + hi) // 2

print(ans)
