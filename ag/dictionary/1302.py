import sys

N = int(sys.stdin.readline().rstrip())
d = dict()
for i in range(N):
  book = sys.stdin.readline().rstrip()
  # 이미 dict 안에 있다면
  if book in d:
    d[book] += 1
  else:
    #없다면 한권 팔렸다
    d[book] = 1

# 가장 많이 팔린 책의 value값
m = max(d.values())
candidates = []
for key, value in d.items():
  if value == m:
    candidates.append(key)

candidates.sort()
print(candidates[0])
