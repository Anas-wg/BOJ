def solution(s):
  answer = len(s)
  # 1 부터 압축 단위를 늘려가면서 확인
  for step in range(1, len(s)// 2 + 1):
    compressed = ""
    prev = s[0:step] # 앞에서 step 만큼의 문자열 추출
    count = 1
    # step 크기 만큼 증가시키며 이전 문자열과 비교
    for j in range(step, len(s), step):
      if prev == s[j:j + step]:
        count += 1
      else:
        # 2보다 작으면 그냥 문자열만, 아니라면 문자열 처리
        compressed += str(count) + prev if count >= 2 else prev
        prev = s[j : j + step] # 다음 단위로 이동(상태 초기화)
        count = 1 # 역시나 상태 초기화
    compressed += str(count) + prev if count >= 2 else prev
    # 만들어지는 압축 문자열이 가장 짧은 것이 답
    answer = min(answer, len(compressed))
  return answer

