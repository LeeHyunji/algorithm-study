![header](https://capsule-render.vercel.app/api?type=waving&color=gradient&height=300&section=header&text=Python%20%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98%20%EC%8A%A4%ED%84%B0%EB%94%94%201%ED%9A%8C%EC%B0%A8&fontSize=51)


## 1. 평균 구하기 [🔗](https://school.programmers.co.kr/learn/courses/30/lessons/12944)
### 결과
    테스트 성능
        - 0.01ms, 10.1MB

    채점 결과
        - 정확성: 100.0
        - 합계: 100.0 / 100.0
### 풀이
    1. 입력받은 배열(arr)의 값을 반복문을 통해서 합산.
    2. 합산 값을 arr의 len로 나눠서 평균값 계산.

<br>

## 2. 짝수와 홀수 [🔗](https://school.programmers.co.kr/learn/courses/30/lessons/12937)
### 결과
    테스트 성능
        - 0.00ms, 10.1MB

    채점 결과
        - 정확성: 100.0
        - 합계: 100.0 / 100.0
### 풀이
    1. 입력받은 정수(n)를 2로 나눴을 때 나머지가 0이면 짝수 1이면 홀수

<br>

## 3. 자릿수 더하기 [🔗](https://school.programmers.co.kr/learn/courses/30/lessons/12931)
### 결과
    테스트 성능
        - 0.02ms, 10.3MB

    채점 결과
        - 정확성: 100.0
        - 합계: 100.0 / 100.0
### 풀이
    1. 입력받은 자연수(n)을 배열로 바꾸기 위해서 문자열로 변환
    2. map을 통해 각 자리 숫자를 int타입으로 배열로 저장
    3. sum()으로 배열의 모든 값 더하기

<br>

## 4. 자연수 뒤집어 배열로 만들기 [🔗](https://school.programmers.co.kr/learn/courses/30/lessons/12932)
### 결과
    테스트 성능
        - 0.03ms, 10.4MB

    채점 결과
        - 정확성: 100.0
        - 합계: 100.0 / 100.0
### 풀이
    1. 입력받은 자연수(n)을 배열로 바꾸기 위해서 문자열로 변환
    2. map을 통해 각각 숫자로 변환해서 배열로 저장
    3. .reverse()를 통해서 배열의 순서를 반전시켜준다.

<br>

## 5. 숫자 문자열과 영단어 - 2021 카카오 채용연계형 인턴십 [🔗](https://school.programmers.co.kr/learn/courses/30/lessons/81301)
### 결과
    테스트 성능
        - 0.03ms, 10.4MB

    채점 결과
        - 정확성: 100.0
        - 합계: 100.0 / 100.0
### 퓰이
    1. 지칭하는 숫자에 맞는 index에 영단어를 넣은 배열을 생성
    2. 반복문을 통해서 입력받은 문자열(s)에 있는 영단어가 배열에 있으면 해당 index 번호로 변경
        - 이때, 인덱스 번호는 Number 타입이므로 String타입으로 변환해서 replace  

<br>

## 6. 체육복 탐욕법(Greedy) [🔗](https://school.programmers.co.kr/learn/courses/30/lessons/42862)
### 결과
    테스트 성능
        - 0.02ms, 10.3MB

    채점 결과
        - 정확성: 100.0
        - 합계: 100.0 / 100.0
### 풀이
    1. 도난당한 학생(lost)가 본인 여벌 옷(reserve)이 있는지 확인
        - 여벌옷이 있으면 lost에서 삭제
    2. 여벌의 체육복 빌릴 때는 앞번호나 뒷번호 학색만 가능하기 때문에 lost, reserve 배열을 번호순으로 정렬
    3. 순차적으로 앞번호에게 먼저 빌리고, 앞번호가 없을 경우 뒷번호 학생한테 빌리도록 처리
    4. error : 7번 결과만 미통과
        -  1번 과정에서 lost로 반복문을 돌면서 여벌옷있는지를 체크할때 바로 lost에서 빼버렸더니 lost가 제대로 반복되지 않는 현상 발견
        - tmp_lost로 초기 lost 데이터를 복사해서 반복문 실행하여 처리

<br>

## 7. 비밀지도 - 2018 KAKAO BLIND RECRUITMENT [🔗](https://school.programmers.co.kr/learn/courses/30/lessons/17681)

## 8. 약수의개수와덧셈-월간코드챌린지시즌2 [🔗](https://school.programmers.co.kr/learn/courses/30/lessons/77884)

## 9. 없는숫자더하기-월간코드챌린지시즌3 [🔗](https://school.programmers.co.kr/learn/courses/30/lessons/86051)

## 10. 완주하지 못한 선수 – 해시 [🔗](https://school.programmers.co.kr/learn/courses/30/lessons/42576)