# 가능한 구조물인지 확인하는 함수
def possible(answer):
  for x, y, stuff in answer:
    if stuff == 0: # 기둥일 경우
      if y == 0 or [x - 1, y, 1] in answer or [x, y, 1] in answer or [x, y - 1, 0] in answer:
        # 바닥 위, 보의 한쪽 끝 부분위 , 다른 기둥 위라면 정상
        continue
      return False # 아니면 False
    elif stuff == 1: # 설치된 것이 보인 경우
      # 한쪽 끝이 기둥 위 혹은 양쪽 끝부분이 다른 보와 동시 연결이라면 정상
      if[x, y -1, 0] in answer or [x + 1, y - 1 , 0] in answer or([x - 1, y, 1] in answer and [x + 1,y,1] in answer):
        continue
      return False
  return True
  
def solution(n, build_frame):
  answer = []
  for frame in build_frame:
    x, y, stuff, operate = frame 
    if operate == 0: # 삭제하는 경우
      answer.remove([x, y, stuff]) # 일단 삭제 부터
      if not possible(answer):
        answer.append([x, y, stuff])
    if operate == 1: # 설치하는 경우
      answer.append([x, y, stuff])
      if not possible(answer):
        answer.remove([x, y, stuff])
  return sorted(answer)