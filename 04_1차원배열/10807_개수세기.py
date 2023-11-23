import sys
sys.stdin = open("input.txt","r")
N = int(sys.stdin.readline())
list = []
answer = 0

for item in map(int,sys.stdin.readline().split()):
  list.append(item)

V = int(sys.stdin.readline())

for i in range(len(list)):
  if V == list[i]:
    answer +=1

print(answer)