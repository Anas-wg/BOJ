hour, minute = map(int, input().split())
cooking_time = int(input())

# 몫만 가져오기
hour += cooking_time // 60 
# 분은 60으로 나는 값의 나머지
minute += cooking_time % 60

if(minute >= 60):
  minute -= 60
  hour += 1

if(hour >= 24):
  hour -= 24

print(hour,minute)



