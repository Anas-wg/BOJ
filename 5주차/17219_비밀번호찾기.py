import sys

# N -> 저장된 사이트 개수
# M -> 비번 찾으려는 페이지 개수
N, M = map(int,sys.stdin.readline().strip().split())

## dict 형식으로 받고,
## 뒤에서 M번째 줄부터 일치하는 비번 찾아주기
box = {}
page_list = []
pw_list = []

for i in range(N):
  id, pw = sys.stdin.readline().strip().split()
  box[id] = pw

for j in range(-M, 0):
  page = sys.stdin.readline().strip()
  page_list.append(page)

for k in range(len(page_list)):
  pw = box.get(page_list[k])
  pw_list.append(pw)


for l in range(len(pw_list)):
  print(pw_list[l])
