import sys
from datetime import datetime  

N = int(input())
student_list = []
for i in range(N):
  [name, day, month, year] = sys.stdin.readline().rstrip().split(' ')
  birthday = datetime(int(year), int(month), int(day))
  student_list.append([name, birthday])

student_list.sort(key=lambda x: x[1])

print(student_list[-1][0])
print(student_list[0][0])


