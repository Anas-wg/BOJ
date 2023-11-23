import sys
sys.stdin = open("input.txt","r")

N = int(sys.stdin.readline())
list = list(map(int,sys.stdin.readline().split()))
# list.sort()
# print(list[0], list[len(list)-1], end=" ")

# 더 빠른 해결책
print(min(list),max(list))