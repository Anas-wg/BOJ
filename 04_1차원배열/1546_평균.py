import sys
sys.stdin = open("input.txt","r")
average_score = 0
sum_score = 0

N = int(sys.stdin.readline())
grade_list = list(map(int, sys.stdin.readline().split()))
grade_list.sort()
best_score = grade_list[-1]


for i in range(N):
  grade_list[i] = grade_list[i] / best_score * 100

for j in range(N):
  sum_score += float(grade_list[j])
print(sum_score / N)
