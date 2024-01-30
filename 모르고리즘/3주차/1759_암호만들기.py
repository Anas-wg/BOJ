from itertools import combinations
L, C = map(int, input().split())

pw_char = list(input().split())
vowel = ['a','e','i','o','u']
pw_list = []
result = list(combinations(pw_char, L))
for i in result:
    i = list(i)
    i.sort()
    count = 0
    for j in vowel:
        if j in i:
            count += 1
    if 1 <= count <= L-2:
        pw = ''.join(i)
        pw_list.append(pw)
pw_list.sort()
for i in pw_list:
    print(i)