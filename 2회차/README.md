![header](https://capsule-render.vercel.app/api?type=waving&color=gradient&height=300&section=header&text=Python%20%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98%20%EC%8A%A4%ED%84%B0%EB%94%94%202%ED%9A%8C%EC%B0%A8&fontSize=51)


## 1. 두 정수 사이의 합 [🔗](https://school.programmers.co.kr/learn/courses/30/lessons/12912)
### 결과
    테스트 성능
        - 0.01ms, 10.1MB

    채점 결과
        - 정확성: 100.0
        - 합계: 100.0 / 100.0
### 풀이
    1. 입력받은 두 정수 a,b의 크기를 비교해서 range()연산.
    2. 이때, max를 포함해야되기때문에 range(min,max+1)
    2. sum으로 ragne의 합을 구함.

## 2. 문자열을 정수로 바꾸기 [🔗](https://school.programmers.co.kr/learn/courses/30/lessons/12925)
### 결과
    테스트 성능
        - 0.02ms, 10.3MB

    채점 결과
        - 정확성: 100.0
        - 합계: 100.0 / 100.0
### 풀이
    1. 문자열 앞에 있는 부호를 먼저 판별하고 숫자로 변환할 계획.
    2. 일단 제일 숫자로 타입변경 int()가 어떻게 반응하는지 확인하기 위해서 사용.
    3. int()는 +,-와 같은 부호도 숫자로 인식하다고 한다.

## 3. 정수 내림차순으로 배치하기 [🔗](https://school.programmers.co.kr/learn/courses/30/lessons/12933)
### 결과
    테스트 성능
        - 0.02ms, 10.3MB

    채점 결과
        - 정확성: 100.0
        - 합계: 100.0 / 100.0
### 풀이
    1. 각 자리수를 내림차순으로 쉽게 정렬 하기위해서 배열이 필요하다고 판단.
    2. 각 자리수를 분리하기 위해서 입력받은 정수 n을 문자열로 변환
    3. sorted()에 reverse=True 옵션을 추가해서 내림차순으로 정렬
    4. sorted()로 나온 리스트를 .join으로 문자열로 변환 후 다시 정수로 변환 출력

## 4. 나머지가 1이 되는 수 찾기 - 월간 코드 챌린지 시즌3 [🔗](https://school.programmers.co.kr/learn/courses/30/lessons/87389)
### 결과
    테스트 성능
        - 0.02ms, 10.3MB

    채점 결과
        - 정확성: 100.0
        - 합계: 100.0 / 100.0
### 풀이
    1. 1은 나눠도 나머지가 없으므로 제외하고 범위는 2부터 n-1까지 반복문
    2. x로 나눈 값이 1인지를 판별 후 return

## 5. 음양 더하기 - 월간 코드 챌린지 시즌2 [🔗](https://school.programmers.co.kr/learn/courses/30/lessons/76501)
### 결과
    테스트 성능
        - 0.10ms, 10.2MB

    채점 결과
        - 정확성: 100.0
        - 합계: 100.0 / 100.0
### 풀이
    1. absolute와 signs의 크기는 동일하기때문에 아무 배열로 반복문 진행
    2. sings가 True이면 그대로 absolute. False이면 -absolute로 저장된 리스트 생성
    3. 2번의 리스트를 sum()으로 합. 

## 6. 예산 - Summer/Winter Coding(~2018) [🔗](https://school.programmers.co.kr/learn/courses/30/lessons/12982)
### 결과
    테스트 성능
        - 0.00ms, 10.3MB

    채점 결과
        - 정확성: 100.0
        - 합계: 100.0 / 100.0
### 풀이
    1. 정해진 예산내에서 최대한 많은 부서의 물품을 전달할려면 신청 금액이 적은 순으로 정렬 필요.
    2. 예산 신청금액이 적은 순으로 예산에서 빼고 예산이 0미만이 되면 총 카운트를 Return


## 7. K번째수 - 정렬 [🔗](https://school.programmers.co.kr/learn/courses/30/lessons/42748)
### 결과
    테스트 성능
        - 0.00ms, 10.3MB

    채점 결과
        - 정확성: 100.0
        - 합계: 100.0 / 100.0
### 풀이
    1. array의 index는 0부터 시작하므로 [i-1:j]까지 자른다.
    2. commend가 여러개 있어서 sorted로 리스트를 만들어 정렬
    3. k번째 요소 추출해서 answer 리스트에 추가. 최종적으로 answer 출력 

## 8. 같은 숫자는 싫어 - 스택/큐 [🔗](https://school.programmers.co.kr/learn/courses/30/lessons/12906)
### 결과
    테스트 성능
        - 0.00ms, 10.3MB

    채점 결과
        - 정확성: 71.9
        - 효율성: 28.1
        - 합계: 100.0 / 100.0
### 풀이
    1. 문제 타이틀이 스택/큐 문제라고 되어 있고, 원소의 순서를 유지해야된다고 해서 앞에서 부터 요소 빼는 Queue를 사용했다.
    2. Queue를 사용해서 결과 배열(answer)이 비어있거나, 결과 배열의 마지막 값이 Queue.pop 값과 같지 않을때 결과 배열에 추가하도로 했다.
    3. 테스트 정확성은 문제가 없었는데 효율성에서 Runtime 문제가 발생한것같다.
    4. Queue를 열심히 만지작 거렸는데도 반복해서 Runtime Error 발생
    5. Queue 사용없이 list 요소 비교로 재작성 했더니 효율성 통과 (60.28ms, 27.8MB)
    6. Error 원인 ) Queue.pop 사용시 배열의 길이가 길어지면 모든 요소가 한칸씩 앞으로 당겨져야 해서 매우 오래 걸린다고 한다.
        1,000,000 배열 크기면 pop 한번 하면 999,999 요소가 한번씩 앞으로 이동해야 되는 현상이 발생.
    7. Error 파악하고나니 뒤에서 꺼내는 Stack으로 한뒤 reverse하면 어땠을까 싶어서 시도했는데 통과 (141.59ms, 21.8MB)



## 9. 실패율 - 2019 KAKAO BLIND RECRUITMENT [🔗](https://school.programmers.co.kr/learn/courses/30/lessons/42889)
### 결과
    테스트 성능
        - 1733.37ms, 18.4MB

    채점 결과
        - 정확성: 100.0
        - 합계: 100.0 / 100.0
### 풀이
    1. 실패율은 스테이지별로 계산을 해야되므로 전체 스테이지의 개수 N으로 반복문
    2. 리스트.count()를 사용해서 유저별로 현재 멈춰있는 스테이지의 번호가 담긴 stages배열에서 해당 스테이지에 몇명이나 멈춰있는지를 추출
    3. curr_stage_fail/curr_stage_players(스테이지에 도달했으나 아직 클리어하지 못한 플레이어의 수 / 스테이지에 도달한 플레이어 수)로 실패율 계산
    3. 실패율을 기준으로 정렬하고 번호를 return값으로 추출해야되므로 두개의 값 모두 저장할 필요성이 있어서 딕셔너리 형태로 저장
    4. dict의 items(실패율) 기준으로 정렬하고 리스트 축약형을 사용해 dict의 key(스테이지번호)가 담긴 리스트 생성 하고 return
    5. Runtime Error 발생 ) 앞쪽에서 스테이지 도달이 막히면 뒤쪽에는 스테이지에 도달한 유저가 0이 되므로 ZeroDivisionError가 발생
        - 스테이지 도달 유저가 0이면 실패율 0으로 처리 후 통과

## 10. 소수 만들기 - Summer/Winter Coding(~2018) [🔗](https://school.programmers.co.kr/learn/courses/30/lessons/12977)
### 결과
    테스트 성능
        - 106.05ms, 11.3MB

    채점 결과
        - 정확성: 100.0
        - 합계: 100.0 / 100.0
### 풀이
    1. 주어진 숫자 배열 num에서 순서상관없이 중복되지 않는 숫자를 추출하는데 조합 개념을 사용
    2. itertools 모듈의 combinations(배열,추출개수)를 사용해서 3가지 숫자 추출
    3. 추출한 값의 합이 소수인지 판별