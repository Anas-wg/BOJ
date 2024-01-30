import sys
input = sys.stdin.readline

paper = [[0]*101 for i in range(101)]

for _ in range(int(input())):
    a,b = map(int,input().split())
    for i in range(10):
        for j in range(10):
            paper[a+i][b+j] = 1

size = 0
for i in paper:
    size += sum(i)
print(size)
