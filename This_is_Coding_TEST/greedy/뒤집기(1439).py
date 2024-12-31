S = input()

count0 = 0
count1 = 1

if S[0] == "1":
  count0 += 1
else:
  count1 += 1

for i in range(1, len(S)-1):
  if S[i] != S[i + 1]:
    if S[i + 1] == "1":
      count0 += 1
    else:
      count1 += 1

print(min(count0,count1))