def solution(N, stages):
  answer = []
  length = len(stages)

  # 스테이지 번호 1 부터 N 까지 증가
  for i in range(1, N + 1):
    # 해당 스테이지에 머물러 있는 사람수 count를 이용하여 계산
    count = stages.count(i)
    # 실패율 계산
    if length == 0 :
      fail = 0
    else:
      fail = count / length
    # 리스트에 (스테이지, 실패율) 삽입
    answer.append((i, fail))
    length -= count # 길이 갱신
  # 실패율 기준 내림차순
  answer = sorted(answer, key=lambda x : x[1], reverse= True)
  # 정렬된 스테이지 번호 출력
  answer = [i[0] for i in answer]
  return answer
