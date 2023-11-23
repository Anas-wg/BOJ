import sys
sys.stdin = open('input.txt', 'r')
N, X = map(int, sys.stdin.readline().split())

list = []
answer_list = []
for i in map(int, sys.stdin.readline().split()):
  list.append(i)


for j in range(len(list)):
  if list[j] < X:
    answer_list.append(list[j])
print(*answer_list)