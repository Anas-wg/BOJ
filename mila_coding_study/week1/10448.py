from itertools import combinations_with_replacement

tri_nums = []
i = 1
while (i * (i + 1)) // 2 <= 1000:
    tri_nums.append((i * (i + 1)) // 2)
    i += 1

def is_three_tri(num):
    for comb in combinations_with_replacement(tri_nums, 3):  
        if sum(comb) == num:
            return 1  
    return 0

# 입력 처리
T = int(input())
for _ in range(T):
    K = int(input())
    print(is_three_tri(K))
