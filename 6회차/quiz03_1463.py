# 1로 만들기

# 문제
# - 정수 X에 사용할 수 있는 연산은 다음과 같이 세 가지 이다.
# - X가 3으로 나누어 떨어지면, 3으로 나눈다.
# - X가 2로 나누어 떨어지면, 2로 나눈다.
# - 1을 뺀다.
# - 정수 N이 주어졌을 때, 위와 같은 연산 세 개를 적절히 사용해서 1을 만들려고 한다. 연산을 사용하는 횟수의 최솟값을 출력하시오.
# 입력
# - 첫째 줄에 1보다 크거나 같고, 10^6보다 작거나 같은 정수 N이 주어진다.
# 출력
# - 첫째 줄에 연산을 하는 횟수의 최솟값을 출력한다.


def solution(num):
    '''
        테스트 성능
            - 772ms, 219776KB
    '''
    dp=[[] for _ in range(num)]
    cnt =0
    dp[cnt]=[num]
    while min(dp[cnt])>1:                               # 계산이 1이 될때까지 연산
        cnt+=1
        for calc in  dp[cnt-1]:                         # 조건1,2,3에 해당되는 모든 연산의 경우의 수를 계산
            dp[cnt].append(calc-1)                      # - 조건 1 : 나눠떨어지지 않을 경우 : -1
            if calc%2 == 0:                             # - 조건 2 : 2으로 나눠떨어질 경우 : //2
                dp[cnt].append(calc//2)
            if calc%3 == 0:                             # - 조건 3 : 3으로 나눠떨어질 경우 : //3
                dp[cnt].append(calc//3)
    return cnt

def solution_bottomUp(num):
    '''
        테스트 성능
            - 368ms, 39068KB
    '''
    dp= [0]*(num+1)
    for i in range(2,num+1):                                # 2부터 num까지 반복
        dp[i]=dp[i-1]+1                                     # 1을 빼는 연산 -> 1회 진행
        if i%2==0:                                          # 2로 나누어 떨어질 때, 2로 나누는 연산
            dp[i]=min(dp[i],dp[i//2]+1)
        if i%3==0:                                          # 3으로 나누어 떨어질 때, 3으로 나누는 연산
            dp[i]=min(dp[i],dp[i//3]+1)
    return dp[num]
num = int(input())
print(solution(num))