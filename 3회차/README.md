![header](https://capsule-render.vercel.app/api?type=waving&color=gradient&height=300&section=header&text=Python%20%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98%20%EC%8A%A4%ED%84%B0%EB%94%94%203%ED%9A%8C%EC%B0%A8&fontSize=51)


## 1. 문자열 내 p와 y의 개수 [🔗](https://school.programmers.co.kr/learn/courses/30/lessons/12916)
### 작성한 코드 👉 [#12916](https://github.com/LeeHyunji/python-algorithm/blob/main/3%ED%9A%8C%EC%B0%A8/quiz01_12916.py)

### 결과
    테스트 성능
        - 0.01ms, 10.1MB

    채점 결과
        - 정확성: 100.0
        - 합계: 100.0 / 100.0
### 풀이
    1. 개수를 비교할 때 대문자와 소문자는 구별하지 않기때문에 'p'와 'y'의 개수를 구하기전에 문자열을 lower()를 통해서 소문자로 바꿔준다.
    2. p와 y의 갯수를 비교해준다.

<br>

## 2. 핸드폰 번호 가리기 [🔗](https://school.programmers.co.kr/learn/courses/30/lessons/12948)

### 작성한 코드 👉 [#12948](https://github.com/LeeHyunji/python-algorithm/blob/main/3%ED%9A%8C%EC%B0%A8/quiz02_12948.py)

### 결과
    테스트 성능
        - 0.00ms, 10.3MB

    채점 결과
        - 정확성: 100.0
        - 합계: 100.0 / 100.0
### 풀이
    1. 문자열 곱셈으로 phone_number의 갯수-4만큼 '*'표현해준다.
    2. phone_number의 뒤에서 4자리를 자른다음 문자열 덧셈으로 '*'과 더해준다.

<br>

## 3. 제일 작은 수 제거하기 [🔗](https://school.programmers.co.kr/learn/courses/30/lessons/12935)

### 작성한 코드 👉 [#12935](https://github.com/LeeHyunji/python-algorithm/blob/main/3%ED%9A%8C%EC%B0%A8/quiz03_12935.py)

### 결과
    테스트 성능
        - 1.08ms, 15.6MB

    채점 결과
        - 정확성: 100.0
        - 합계: 100.0 / 100.0
### 풀이
    1. min()을 통해서 가장 작은 값을 찾아준 다음 list에서 remove()로 제거해 반환한다.
    2. 해당 배열의 크기가 0이면 [-1]값으로 반환한다.

<br>

## 4. 콜라츠 추측 [🔗](https://school.programmers.co.kr/learn/courses/30/lessons/12943)

### 작성한 코드 👉 [#12943](https://github.com/LeeHyunji/python-algorithm/blob/main/3%ED%9A%8C%EC%B0%A8/quiz04_12943.py)

### 결과
    테스트 성능
        - 0.46ms, 10.4MB

    채점 결과
        - 정확성: 100.0
        - 합계: 100.0 / 100.0
### 풀이
    1. 반복문을 쓸까했다가 한번 계산하고 나온 값에 대해서 다시 계산해야되서 재귀함수를 사용했다.
    2. 재귀함수에서는 종료조건이 중요한데 cnt가 500회 이상일 경우와 num이 1일 경우로 지정했다.

<br>

## 5. 수박수박수박수박수박수? [🔗](https://school.programmers.co.kr/learn/courses/30/lessons/12922)

### 작성한 코드 👉 [#12922](https://github.com/LeeHyunji/python-algorithm/blob/main/3%ED%9A%8C%EC%B0%A8/quiz05_12922.py)

### 결과
    테스트 성능
        - 0.00ms, 10.3MB

    채점 결과
        - 정확성: 100.0
        - 합계: 100.0 / 100.0
### 풀이
    1. "수박" 두글자씩 반복되기 때문에 n의 절반만큼 "수박"을 만들어준다.
    2. n 홀수인경우에는 "수"를 더 추가해준다.

<br>


## 6. 가운데 글자 가져오기 [🔗](https://school.programmers.co.kr/learn/courses/30/lessons/12903)

### 작성한 코드 👉 [#12903](https://github.com/LeeHyunji/python-algorithm/blob/main/3%ED%9A%8C%EC%B0%A8/quiz06_12922.py)

### 결과
    테스트 성능
        - 0.00ms, 10.3MB

    채점 결과
        - 정확성: 100.0
        - 합계: 100.0 / 100.0
### 풀이
    1. 문자열의 중간을 맞추기 위해서 나누기 2를 통해서 중간의 위치를 대략 감지할려고 한다.
    2. 같은 센터 위치만큼 앞뒤로 슬라이스 헤서 가운데 글자가 뽑는다.
    3. 글자 수가 1이나 2이면 센터위치가 0으로 나오기 때문에 그대는 문자열 그대로 뽑아준다.

<br>

## 7. 올바른 괄호 - 스택/큐[🔗](https://school.programmers.co.kr/learn/courses/30/lessons/12909)

### 작성한 코드 👉 [#12909](https://github.com/LeeHyunji/python-algorithm/blob/main/3%ED%9A%8C%EC%B0%A8/quiz07_12909.py)

### 결과
    테스트 성능
        - 20.78ms, 11MB

    채점 결과
        - 정확성: 69.5
        - 효율성: 30.5
        - 합계: 100.0 / 100.0
### 풀이
    1. 스택/큐 문제인만큼 기본 리스트를 활용할 수 있지만 스택 개념을 활용해 보았다.
    2. 문자열을 리스트로 만든 후 마지막 글자부터 stack_arr에 추가한다.
    3. stack_arr에서 문자열에서 뽑은 값과 가장 마지막에 들어간 데이터를 합쳤는데 "()"가 되면 stack의 마지막 값을 뽑아준다.
    4. 만약 "()"가 정상적이지 않으면 문자열에서 뽑은 값을 stack에 추가 해준다.
    5. 문자열 길이만큼 반복했다 stack에 괄호 값이 하나라도 남아있으면 false를 반환해준다.

<br>


## 8. H-Index - 정렬 [🔗](https://school.programmers.co.kr/learn/courses/30/lessons/42747)

### 작성한 코드 👉 [#42747](https://github.com/LeeHyunji/python-algorithm/blob/main/3%ED%9A%8C%EC%B0%A8/quiz08_42747.py)

### 결과
    테스트 성능
        - 0.09ms, 9.99MB

    채점 결과
        - 정확성: 100.0
        - 합계: 100.0 / 100.0
### 풀이
    1. H-index의 정의는 위키백과에서 참고 한다.
    2. H-index의 값은 모든 논문 중 h회 이상 인용된 논문이 h개 이상일 때, 이 둘을 동시에 만족하는 h의 최대값을 구하는 것 이기때문에 내림차순으로 정렬한다.
    3. H-index의 최대 갯수는 발표한 논문의 갯수를 초과할 수 없기 때문에 최소값이 n(발표한 논문의 갯수)보다 작은지 확인한다.
    4. 반복문을 인용횟수 v와 인용횟수 초과된 논문의 갯수 h를 비교해서 h-index의 최대값을 찾아낸다.



## 9. 폰켓몬-해시 [🔗](https://school.programmers.co.kr/learn/courses/30/lessons/1845)

### 작성한 코드 👉 [#1845](https://github.com/LeeHyunji/python-algorithm/blob/main/3%ED%9A%8C%EC%B0%A8/quiz09_1845.py)

### 결과
    테스트 성능
        - 0.00ms, 10.3MB

    채점 결과
        - 정확성: 100.0
        - 합계: 100.0 / 100.0
### 풀이
    1. 최대 선택가능한 값의 갯수는 N/2개이다.
    2. 가장 많은 종류의 포켓몬을 선택하는 방법은 중복없는 폰켓몬의 갯수를 의미한다.
    3. 중복없는 폰켓몬 갯수가 최대선택값보다 크면 최대선택값, 작으면 중복없는 폰켓몬 갯수를 리턴해준다.
    
## 10. 다트 게임 2018 KAKAO BLIND RECRUITMENT [🔗](https://school.programmers.co.kr/learn/courses/30/lessons/17682)

### 작성한 코드 👉 [#17682](https://github.com/LeeHyunji/python-algorithm/blob/main/3%ED%9A%8C%EC%B0%A8/quiz10_17682.py)

### 결과
    테스트 성능
        - 0.00ms, 10.3MB

    채점 결과
        - 정확성: 100.0
        - 합계: 100.0 / 100.0

### 풀이
    1. 0-10까지 정수로 점수가 나오기 때문에 두글자인 10은 16진수 A로 표현한다.
    2. 딕셔너리의 Key 값을 통해서 보너스 유형을 판별해서 해당 유형의 제곱만큼 보너스를 계산해준다.
    3. 추가적인 Option '*'은 현재와 직전 점수의 2배를 계산해야되므로 리스트의 뒤에서 2번째까지의 값을 재게산 해준다. 
    4. 추가적인 Option '#'은 현재 점수의 마이너스를 계산해야하므로 리스트의 뒤에서 1번째의 값을 마이터스로 재계산해준다.
    5. 리스트에 저장한 3번의 기회에서 얻은 점수를 더해준다. 
 