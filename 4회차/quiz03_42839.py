# 소수 찾기
# 
# 문제 설명
# - 한자리 숫자가 적힌 종이 조각이 흩어져있습니다. 흩어진 종이 조각을 붙여 소수를 몇 개 만들 수 있는지 알아내려 합니다.
# - 각 종이 조각에 적힌 숫자가 적힌 문자열 numbers가 주어졌을 때, 종이 조각으로 만들 수 있는 소수가 몇 개인지 return 하도록 solution 함수를 완성해주세요.
# 제한사항
# - numbers는 길이 1 이상 7 이하인 문자열입니다.
# - numbers는 0~9까지 숫자만으로 이루어져 있습니다.
# - "013"은 0, 1, 3 숫자가 적힌 종이 조각이 흩어져있다는 의미입니다.

from itertools import *

def primenumber(x):
    if x==0 or x== 1:
        return False
    for i in range(2, x):	# 2부터 x-1까지의 모든 숫자 나눠떨어지는게 하나라도 있으면 False
        if x % i == 0:		
            return False
    return True	

def solution(numbers):
    answer = set()
    for i in range(len(numbers)):                                                 # 순열로 n자리수 경우의 수 계산 
        answer |= set(map(lambda x : int("".join(x)),permutations(numbers, i+1))) 
    return len(list(filter(primenumber,answer)))                                  # 모든 경우의 수에 해당되는 숫자가 소수인지 찾기