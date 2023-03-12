# 메뉴 리뉴얼

# 문제 설명
# - 레스토랑을 운영하던 스카피는 코로나19로 인한 불경기를 극복하고자 메뉴를 새로 구성하려고 고민하고 있습니다.
# - 기존에는 단품으로만 제공하던 메뉴를 조합해서 코스요리 형태로 재구성해서 새로운 메뉴를 제공하기로 결정했습니다. 어떤 단품메뉴들을 조합해서 코스요리 메뉴로 구성하면 좋을 지 고민하던 "스카피"는 이전에 각 손님들이 주문할 때 가장 많이 함께 주문한 단품메뉴들을 코스요리 메뉴로 구성하기로 했습니다.
# - 단, 코스요리 메뉴는 최소 2가지 이상의 단품메뉴로 구성하려고 합니다. 또한, 최소 2명 이상의 손님으로부터 주문된 단품메뉴 조합에 대해서만 코스요리 메뉴 후보에 포함하기로 했습니다.
# - 예를 들어, 손님 6명이 주문한 단품메뉴들의 조합이 다음과 같다면,
# - (각 손님은 단품메뉴를 2개 이상 주문해야 하며, 각 단품메뉴는 A ~ Z의 알파벳 대문자로 표기합니다.)
#   손님 번호	주문한 단품메뉴 조합
#   1번 손님	A, B, C, F, G
#   2번 손님	A, C
#   3번 손님	C, D, E
#   4번 손님	A, C, D, E
#   5번 손님	B, C, F, G
#   6번 손님	A, C, D, E, H
# - 가장 많이 함께 주문된 단품메뉴 조합에 따라 "스카피"가 만들게 될 코스요리 메뉴 구성 후보는 다음과 같습니다.
#   코스 종류	메뉴 구성	설명
#   요리 2개 코스	A, C	1번, 2번, 4번, 6번 손님으로부터 총 4번 주문됐습니다.
#   요리 3개 코스	C, D, E	3번, 4번, 6번 손님으로부터 총 3번 주문됐습니다.
#   요리 4개 코스	B, C, F, G	1번, 5번 손님으로부터 총 2번 주문됐습니다.
#   요리 4개 코스	A, C, D, E	4번, 6번 손님으로부터 총 2번 주문됐습니다.
# 문제
# - 각 손님들이 주문한 단품메뉴들이 문자열 형식으로 담긴 배열 orders, "스카피"가 추가하고 싶어하는 코스요리를 구성하는 단품메뉴들의 갯수가 담긴 배열 course가 매개변수로 주어질 때, "스카피"가 새로 추가하게 될 코스요리의 메뉴 구성을 문자열 형태로 배열에 담아 return 하도록 solution 함수를 완성해 주세요.
# 제한사항
# - orders 배열의 크기는 2 이상 20 이하입니다.
# - orders 배열의 각 원소는 크기가 2 이상 10 이하인 문자열입니다.
# - 각 문자열은 알파벳 대문자로만 이루어져 있습니다.
# - 각 문자열에는 같은 알파벳이 중복해서 들어있지 않습니다.
# - course 배열의 크기는 1 이상 10 이하입니다.
# - course 배열의 각 원소는 2 이상 10 이하인 자연수가 오름차순으로 정렬되어 있습니다.
# - course 배열에는 같은 값이 중복해서 들어있지 않습니다.
# - 정답은 각 코스요리 메뉴의 구성을 문자열 형식으로 배열에 담아 사전 순으로 오름차순 정렬해서 return 해주세요.
# - 배열의 각 원소에 저장된 문자열 또한 알파벳 오름차순으로 정렬되어야 합니다.
# - 만약 가장 많이 함께 주문된 메뉴 구성이 여러 개라면, 모두 배열에 담아 return 하면 됩니다.
# - orders와 course 매개변수는 return 하는 배열의 길이가 1 이상이 되도록 주어집니다.
from itertools import combinations
from collections import Counter

def solution(orders, course):
    result = []
    for c in course :
        comb = []
        for order in orders:
            comb.extend((combinations(sorted(order), c)))                                       # 조건) 순서와 상관없에 조합을 뽑기 위해서 정렬하고 조합
        
        comb = dict(Counter(comb))                                                              # 각 중복 요소 갯수 구하기
        comb_max = max(comb.values()) if len(comb) else 0                                       # 조건) comb가 없으면 max구할수 없으므로 0으로 처리
        if comb_max > 1 :                                                                       # 조건) 최소 2번이상만 주문된 메뉴만 코스에 올릴 수 있음.
            comb_max_list = dict(filter(lambda x: x[1]==comb_max , comb.items())).keys()         # 최대 주문 갯수만 필터
            result.extend(list(map(lambda x: "".join(x), comb_max_list)))                        
    
    return sorted(result)

def solution_2(orders, course):
    '''
    max 사용하지 않고 Counter().most_common()를 사용해 최대 빈도값을 구한 경우

        테스트 1 〉	통과 (0.13ms, 10.2MB)
        테스트 2 〉	통과 (0.07ms, 10.3MB)
        테스트 3 〉	통과 (0.10ms, 10.4MB)
        테스트 4 〉	통과 (0.10ms, 10.2MB)
        테스트 5 〉	통과 (0.16ms, 10.4MB)
        테스트 6 〉	통과 (0.29ms, 10.2MB)
        테스트 7 〉	통과 (0.31ms, 10.3MB)
        테스트 8 〉	통과 (1.66ms, 10.6MB)
        테스트 9 〉	통과 (1.32ms, 10.7MB)
        테스트 10 〉	통과 (2.66ms, 10.6MB)
        테스트 11 〉	통과 (0.78ms, 10.5MB)
        테스트 12 〉	통과 (1.01ms, 10.6MB)
        테스트 13 〉	통과 (1.27ms, 10.6MB)
        테스트 14 〉	통과 (1.07ms, 10.6MB)
        테스트 15 〉	통과 (1.40ms, 10.7MB)
        테스트 16 〉	통과 (0.43ms, 10.3MB)
        테스트 17 〉	통과 (0.27ms, 10.2MB)
        테스트 18 〉	통과 (0.20ms, 10.3MB)
        테스트 19 〉	통과 (0.05ms, 10.3MB)
        테스트 20 〉	통과 (0.54ms, 10.3MB)
    '''
    result = []
    for c in course :
        comb = []
        for order in orders:
            comb.extend((combinations(sorted(order), c)))                                       
        
        comb = Counter(comb).most_common()
        if len(comb) and comb[0][1] > 1 :
            comb_max_list = filter(lambda x: x[1]==comb[0][1],comb)                                                    
            result.extend(list(map(lambda x: "".join(x[0]), comb_max_list)))
    return sorted(result)
