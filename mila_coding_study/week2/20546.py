# 입력 받기
CASH = int(input())
stock_prices = list(map(int, input().split()))

# 준현이 (BNP) 초기 자산
jh_cash = CASH
jh_stocks = 0

# 성민이 (TIMING) 초기 자산
sm_cash = CASH
sm_stocks = 0

# 주가 변화 추이를 저장할 리스트
price_changes = []

# 주가 변화 추이 계산
for i in range(1, len(stock_prices)):
    if stock_prices[i] > stock_prices[i - 1]:
        price_changes.append(1)  # 상승
    elif stock_prices[i] < stock_prices[i - 1]:
        price_changes.append(-1)  # 하락
    else:
        price_changes.append(0)  # 변동 없음

# BNP 전략 실행
for price in stock_prices:
    if jh_cash >= price:
        jh_stocks += jh_cash // price
        jh_cash %= price

# TIMING 전략 실행
for i in range(12):  # 총 14일 중 마지막 날은 매매하지 않으므로 12일까지 반복
    # 3일 연속 상승 시, 다음 날 매도
    if i >= 2 and price_changes[i - 2:i + 1] == [1, 1, 1]:
        sm_cash += sm_stocks * stock_prices[i + 1]
        sm_stocks = 0
    # 3일 연속 하락 시, 다음 날 매수
    elif i >= 2 and price_changes[i - 2:i + 1] == [-1, -1, -1]:
        if sm_cash >= stock_prices[i + 1]:
            sm_stocks += sm_cash // stock_prices[i + 1]
            sm_cash %= stock_prices[i + 1]

# 최종 자산 계산
jh_total = jh_cash + jh_stocks * stock_prices[-1]
sm_total = sm_cash + sm_stocks * stock_prices[-1]

# 결과 출력
if jh_total > sm_total:
    print("BNP")
elif jh_total < sm_total:
    print("TIMING")
else:
    print("SAMESAME")
