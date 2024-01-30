N = int(input())

i_list = []
cnt = 0

for i in range(N) :
  str, end = map(int, input().split())
  i_list.append([str, end])


i_list.sort(key=lambda x: (x[1], x[0]))

end = -1

for i in range(len(i_list)):
  next_start = i_list[i][0]
  if end <= next_start:
    end = i_list[i][1]
    cnt +=1

print(cnt)