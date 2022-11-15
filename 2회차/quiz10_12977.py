# 소수 만들기
#
# 문제 설명
# - 주어진 숫자 중 3개의 수를 더했을 때 소수가 되는 경우의 개수를 구하려고 합니다. 
# - 숫자들이 들어있는 배열 nums가 매개변수로 주어질 때, 
#   nums에 있는 숫자들 중 서로 다른 3개를 골라 더했을 때 소수가 되는 경우의 개수를 return 하도록 solution 함수를 완성해주세요.
# 제한사항
# - nums에 들어있는 숫자의 개수는 3개 이상 50개 이하입니다.
# - nums의 각 원소는 1 이상 1,000 이하의 자연수이며, 중복된 숫자가 들어있지 않습니다.

from itertools import *

def is_prime_number(num):
    if num==0 or num==1:
        return False
    else:
        for n in range(2, (num//2)+1):
            if num % n == 0:
                return False        
        return True
def solution(nums):
    answer =0

    for num_arr in list(combinations(nums, 3)):
        num = sum(num_arr)
        if is_prime_number(num): answer+=1
                
    return answer