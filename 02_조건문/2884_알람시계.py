a, b = input().split()

hour = int(a)
if hour == 0:
  hour = 24
minute = int(b)


set_time = 45

if minute > set_time:    
  print(hour, minute - set_time)
else: 
  if set_time - minute == 0:
    print(hour, 00)
  else:
    print(hour - 1, 60 - (set_time - minute))