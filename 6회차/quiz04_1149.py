# RGB거리
#
# 문제
# - RGB거리에는 집이 N개 있다. 거리는 선분으로 나타낼 수 있고, 1번 집부터 N번 집이 순서대로 있다.
# - 집은 빨강, 초록, 파랑 중 하나의 색으로 칠해야 한다. 각각의 집을 빨강, 초록, 파랑으로 칠하는 비용이 주어졌을 때, 아래 규칙을 만족하면서 모든 집을 칠하는 비용의 최솟값을 구해보자.
# - 1번 집의 색은 2번 집의 색과 같지 않아야 한다.
# - N번 집의 색은 N-1번 집의 색과 같지 않아야 한다.
# - i(2 ≤ i ≤ N-1)번 집의 색은 i-1번, i+1번 집의 색과 같지 않아야 한다.
# 입력
# - 첫째 줄에 집의 수 N(2 ≤ N ≤ 1,000)이 주어진다. 둘째 줄부터 N개의 줄에는 각 집을 빨강, 초록, 파랑으로 칠하는 비용이 1번 집부터 한 줄에 하나씩 주어진다. 집을 칠하는 비용은 1,000보다 작거나 같은 자연수이다.
# 출력
# - 첫째 줄에 모든 집을 칠하는 비용의 최솟값을 출력한다.

def solution(n, houses):
    dp = [[0,0,0] for _ in range(n)]                                    # RGB 해당한 색상으로 칠한 cost의 최소값 / 0:R, 1:G, 2:B

    for i in range(n):          
        if i==0:                                                        # 첫번째 집은 RGB별로 칠한 cost의 값
            dp[i] = houses[i]
        else :                                                          # 두번째 집은 현재 cost + 이전 집의 다른 색상cost의 합
            dp[i][0] = houses[i][0] + min(dp[i-1][1],dp[i-1][2])
            dp[i][1] = houses[i][1] + min(dp[i-1][0],dp[i-1][2])
            dp[i][2] = houses[i][2] + min(dp[i-1][0],dp[i-1][1])
    return min(dp[-1])
     
n = int(input())
houses = [list(map(int, input().split(" "))) for _ in range(n)]
print(solution(n,houses))
