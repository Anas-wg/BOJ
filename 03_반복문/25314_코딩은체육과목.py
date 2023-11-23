import sys
# sys.stdin = open("input.txt", "r")

byte = int(sys.stdin.readline())
string = "long int"

amount = round(byte / 4)

for i in range(1, amount):
  string = "long " + string

print(string)