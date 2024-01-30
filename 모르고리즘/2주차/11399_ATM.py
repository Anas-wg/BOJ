user = int(input())
arr = list(map(int, input().split()))
time = 0

arr.sort()

for i in range(1, user):
  arr[i] += arr[i -1]

print(arr)
print(sum(arr))  



