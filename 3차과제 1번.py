def stair_ways_dp(n):
    # 예외 처리
    if n < 0:
        return 0
    if n == 0:
        return 1  # "아무 것도 안 하고 0층에 있는 방법" 1가지로 보는 정의
    if n == 1:
        return 1  # (1)

    # DP 테이블 준비
    dp = [0] * (n + 1)
    dp[0] = 1
    dp[1] = 1

    # 테이블 채우기
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]


# 테스트
n = 7
print("7개의 계단을 오르는 방법의 수는", stair_ways_dp(n), "가지 입니다.")  # 13
print("=" * 100)