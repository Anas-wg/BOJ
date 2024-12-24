N , M , K = map(int, input().split())
nums = list(map(int, (input().split())))

nums.sort()

max_num = nums[-1]
second_num = nums[-2]

var1 = M//K
var2 = M % K
print(var1)

answer = max_num * K * (M // K) + second_num * (M % K)
print(answer)