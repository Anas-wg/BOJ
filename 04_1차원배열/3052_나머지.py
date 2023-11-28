list = []
while True:
  try:
    a = int(input())
    list.append( a % 42)
  except:
    break

print(len(set(list)))