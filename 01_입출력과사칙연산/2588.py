fisrt_input = input().split()
second_input = input().split()

second_temp  =  second_input[0]

second_list = list(map(int, second_temp))

print(int(fisrt_input[0]) * second_list[len(second_list) - 1])
print(int(fisrt_input[0]) * second_list[len(second_list) - 2])
print(int(fisrt_input[0]) * second_list[len(second_list) - 3])
print(int(fisrt_input[0]) * int(second_temp))