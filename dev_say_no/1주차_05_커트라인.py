import sys

N, K = sys.stdin.readline().split()
N = int(N)
K = int(K)

score_list = list(map(int, sys.stdin.readline().split()))
score_list.sort(reverse=True)
print(score_list[K-1])

