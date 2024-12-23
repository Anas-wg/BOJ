N = int(input())
arr = []

for i in range(N):
  name , score = input().split()
  arr.append([name, int(score)])

arr.sort(key=lambda x:x[1])

for student in arr:
  print(student[0])
  
