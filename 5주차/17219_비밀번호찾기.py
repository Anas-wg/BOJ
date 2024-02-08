import sys

# N -> 저장된 사이트 개수
# M -> 비번 찾으려는 페이지 개수
N, M = map(int,sys.stdin.readline().strip().split())

## dict 형식으로 받고,
# box = {}
# page_list = []
# pw_list = []

# for i in range(N):
#   id, pw = sys.stdin.readline().strip().split()
#   box[id] = pw

# for j in range(-M, 0):
#   page = sys.stdin.readline().strip()
#   page_list.append(page)

# for k in range(len(page_list)):
#   pw = box.get(page_list[k])
#   pw_list.append(pw)


# for l in range(len(pw_list)):
#   print(pw_list[l])

m, n = map(int, input().split())

find ={}
for i in range(m):
    site, pw = input().split()
    find[site] = pw

for j in range(n):
    f_site = input()
    print(find[f_site])