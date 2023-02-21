![header](https://capsule-render.vercel.app/api?type=waving&color=gradient&height=300&section=header&text=Python%20%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98%20%EC%8A%A4%ED%84%B0%EB%94%94%207%ED%9A%8C%EC%B0%A8&fontSize=51)


## 1. 평범한 배낭 [🔗](https://www.acmicpc.net/problem/12865)
### 작성한 코드 👉 [#12865](https://github.com/LeeHyunji/python-algorithm/blob/main/7%ED%9A%8C%EC%B0%A8/quiz01_12865.py)

### 결과
    테스트 성능
        - 0.00ms, 0.0MB

    채점 결과
        - 정확성: 100.0
        - 합계: 100.0 / 100.0
### 풀이
    1. 
<br>

## 2. 크레인 인형뽑기 게임 [🔗](https://school.programmers.co.kr/learn/courses/30/lessons/64061)
### 작성한 코드 👉 [#64061](https://github.com/LeeHyunji/python-algorithm/blob/main/7%ED%9A%8C%EC%B0%A8/quiz02_64061.py)

### 결과
    테스트 성능
        - 0.02ms, 10.1MB

    채점 결과
        - 정확성: 100.0
        - 합계: 100.0 / 100.0
### 풀이
    1. moves는 크레인을 작동시킨 열 위치를 담은 배열이나 board는 문제의 이미지처럼 위에서 접근 가능한 형태로 되어 있있다. 사용해야되는 두 매개변수의 포멧이 다르기 때문에 열별로 stack구조로 인형이 담긴 new_board를 만들어준다. (이때 비어 있는 값 0도 지워준다.)
    2. new_board에서 move의 레일에 인형이 있으면 new_board에서 pop()한 다음 basket[-1](제일 위의 인형)과 비교한다.

<br>

## 3. 크레인 인형뽑기 게임 [🔗](https://school.programmers.co.kr/learn/courses/30/lessons/77484)
### 작성한 코드 👉 [#77484](https://github.com/LeeHyunji/python-algorithm/blob/main/7%ED%9A%8C%EC%B0%A8/quiz03_64061.py)

### 결과
    테스트 성능
        - 0.01ms, 10.2MB

    채점 결과
        - 정확성: 100.0
        - 합계: 100.0 / 100.0
### 풀이
    1. 로또의 최고 등수는 기존 숫자 + 지워진 숫자가 모두 맞출 때이고, 로또 최저 등수는 기존 숫자만 맞출때이다.
    2. 기존 숫자 중에서 당첨 여부를 확인하기 위해서 set()을 사용해서 교집합을 구했다.
    3. 지워진 숫자의 갯수는 0으로 표시했기 때문에 count(0)을 통해서 갯수를 구했다.

<br>

## 4. 행렬 테두리 회전하기 [🔗](https://school.programmers.co.kr/learn/courses/30/lessons/77485)
### 작성한 코드 👉 [#77485](https://github.com/LeeHyunji/python-algorithm/blob/main/7%ED%9A%8C%EC%B0%A8/quiz04_77485.py)

### 결과
    테스트 성능
        - 123.56ms, 11.5MB

    채점 결과
        - 정확성: 100.0
        - 합계: 100.0 / 100.0
### 풀이
    1. 행렬 테두리 영역을 찾는다 : 상단(x1,y1)-(x1,y2),오른쪽(x1,y2)-(x2,y2), 하단(x2,y2)-(x2,y1), 왼쪽(x2,y1)-(x1,y1)
    2. 행들 테두리는 시계방향으로 회전시켜야하므로 시계반대방향으로 이전값을 유지하면서 값을 회전시킨다.