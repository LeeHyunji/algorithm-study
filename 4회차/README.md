![header](https://capsule-render.vercel.app/api?type=waving&color=gradient&height=300&section=header&text=Python%20%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98%20%EC%8A%A4%ED%84%B0%EB%94%94%204%ED%9A%8C%EC%B0%A8&fontSize=51)


# 그래프 탐색

## 깊이 우선 탐색(DFS, Depth-First Search)
> 루트 노드에서 시작해서 다음 분기(branch)로 넘어가기 전에 해당 분기를 완벽하게 탐색하는 방법

<br>

#### 재귀를 통한 dfs 구현하기 👉 [dfs_recursive.py](https://github.com/LeeHyunji/python-algorithm/blob/main/4%ED%9A%8C%EC%B0%A8/dfs_recursive.py) :
    1. 시작 'A' 노드(루트 노드)를 방문한다.
        - 방문한 노드는 visited 배열에 표시한다.
    2. 시작 노드와 인접한 노드들을 차례로 순회한다.
    3. 이웃한 노드 'B'를 방문했다면, 시작노드와 인접한 또 다른 노드를 방문하기 전에 'B'와 인접한 노드들을 전부 방문해야 한다.
    4. 인접 노드에 대해서 재귀적으로 함수를 호출하며 탐색을 진행한다.
    5. 아직 방문이 안 된 노드이 없으면 종료한다.

#### 스택을 통한 dfs 구현하기 👉 [dfs_stack.py](https://github.com/LeeHyunji/python-algorithm/blob/main/4%ED%9A%8C%EC%B0%A8/dfs_stack.py) :
    1. 시작 'A' 노드(루트 노드)를 방문한다.
        - 방문한 노드는 visited 배열에 표시한다.
    2. 시작 노드와 인접한 노드들을 차례로 스택에 추가한다.
    3. 스택에 추가된 노드를 꺼내면서 이웃한 노드에 방문한다.
    4. 이웃 노드 'B'를 방문했다면, 시작노드와 인접한 또 다른 노드를 방문하기 전에 'B'와 인접한 노드들을 전부 스택에 추가한다.
    5. 인접 노드에 대해서 스택의 FILO 구조를 통해서 탐색을 진행한다. 
    5. 스택에 담긴 노드가 없을 때 종료한다.
<br>

## 너비 우선 탐색(BFS,Breadth-First Search)
>루트 노드에서 시작해서 인접한 노드들을 먼저 탐색하는 방법

<br>

#### 큐를 통한 bfs 구현하기 👉 [bfs_queue.py](https://github.com/LeeHyunji/python-algorithm/blob/main/4%ED%9A%8C%EC%B0%A8/bfs_queue.py) :
    1. 시작 'A' 노드(루트 노드)를 방문한다.
        - 방문한 노드는 visited 배열에 표시한다.
    2. 시작 노드와 인접한 노드들을 차례로 큐에 추가한다.
    3. 큐에서 추가된 노드를 꺼내면서 이웃한 노드 a 노드의 이웃 노드를 모두 방문한 다음에 이웃의 이웃들을 방문한다.
    4. 인접 노드에 대해서 큐의 FIFO 구조를 통해서 탐색을 진행한다.
    5. 큐에 담긴 노드가 없을 때 종료한다.

<br>
<hr>
<br>

# 완전 탐색 알고리즘
## 1. 최소직사각형 [🔗](https://school.programmers.co.kr/learn/courses/30/lessons/86491)
### 작성한 코드 👉 [#86491](https://github.com/LeeHyunji/python-algorithm/blob/main/4%ED%9A%8C%EC%B0%A8/quiz01_86491.py)

### 결과
    테스트 성능
        - 0.00ms, 0.0MB

    채점 결과
        - 정확성: 100.0
        - 합계: 100.0 / 100.0
### 풀이
    1. 명함의 크기가 가로, 세로가 나뉘어져 있지만 문제 설명에서 눕혀서 가로와 세로를 변경할 수 있다고 명시되어 있다.
    2. 전체 명함 크기에서 큰 부분을 x, 작은 부분을 y로 분리한다.
    3. 분리된 x,y 중에서 제일 큰 값을 곱해서 지갑의 크기를 계산한다.
<br>

## 2. 모의고사 [🔗](https://school.programmers.co.kr/learn/courses/30/lessons/42840)
### 작성한 코드 👉 [#42840](https://github.com/LeeHyunji/python-algorithm/blob/main/4%ED%9A%8C%EC%B0%A8/quiz02_42840.py)

### 결과
    테스트 성능
        - 0.00ms, 0.0MB

    채점 결과
        - 정확성: 100.0
        - 합계: 100.0 / 100.0
### 풀이
    1. 수포자1, 수포자2, 수포자3의 정답을 패턴화 한다.
    2. error ) 처음에는 찍는 패턴을 수식화 해서 문제를 풀었다가 문제를 잘 못읽어서 수포자2의 답 패턴을 잘못 계산해서 테스트 1,6,10,11,13에서 반복적으로 에러를 발생
    3. error 해결방법으로 수식화에서 패턴을 배열에 저장해서 인덱스를 계산하므로써 해당 수포자의 답을 계산하는 방법으로 변경했다.
    4. 수포자의 답과 정답을 비교해서 score를 계산한다.
    5. 계산 된 score 배열을 score의 max값과 비교해서 수포자 번호(index값)을 뽑아낸다.

<br>

## 3. 소수 찾기 [🔗](https://school.programmers.co.kr/learn/courses/30/lessons/42839)
### 작성한 코드 👉 [#42839](https://github.com/LeeHyunji/python-algorithm/blob/main/4%ED%9A%8C%EC%B0%A8/quiz03_42839.py)

### 결과
    테스트 성능
        - 0.00ms, 0.0MB

    채점 결과
        - 정확성: 100.0
        - 합계: 100.0 / 100.0
### 풀이
    1. 전달된 순자 배열 numbers를 가지고 모든 경우의 수를 찾은 다음 소수인지를 찾는다.
    2. 먼저 순열 permutations로 numbers의 length자리수까지의 경우의 수를 게산해준다.
    3. primenumber()를 통해서 소수인 숫자를 찾는다.
<br>

## 4. 카펫 [🔗](https://school.programmers.co.kr/learn/courses/30/lessons/42842)
### 작성한 코드 👉 [#42842](https://github.com/LeeHyunji/python-algorithm/blob/main/4%ED%9A%8C%EC%B0%A8/quiz04_42842.py)

### 결과
    테스트 성능
        - 0.00ms, 0.0MB

    채점 결과
        - 정확성: 100.0
        - 합계: 100.0 / 100.0
### 풀이
    1. 카펫의 사이즈를 계산 후 가능한 w,h 리스트 중에서 brown과 yellow 갯수와 맡은 값을 구하도록 한다.
    2. brown+yellow 격자의 갯수의 합을 통해서 전체 카펫의 크기를 계산한다.
    3. 가로나 세로는 내부 yellow블럭때문에 무조건 3부터 최대 brown 테두리의 반까지 시작한다.
    4. 내부 yellow의 갯수를 만족시키는 w를 카펫 size와 세로 h로 구해준다.
<br>

## 5. 피로도 [🔗](https://school.programmers.co.kr/learn/courses/30/lessons/87946)
### 작성한 코드 👉 [#87946](https://github.com/LeeHyunji/python-algorithm/blob/main/4%ED%9A%8C%EC%B0%A8/quiz05_87946.py)

### 결과
    테스트 성능

    채점 결과

### 풀이
    1. 
    
<br>

## 6. 전력망을 둘로 나누기 [🔗](https://school.programmers.co.kr/learn/courses/30/lessons/86971)
### 작성한 코드 👉 [#86971](https://github.com/LeeHyunji/python-algorithm/blob/main/4%ED%9A%8C%EC%B0%A8/quiz06_86971.py)

### 결과
    테스트 성능

    채점 결과

### 풀이
    1. 
<br>

## 7. 모음사전 [🔗](https://school.programmers.co.kr/learn/courses/30/lessons/84512)
### 작성한 코드 👉 [#84512](https://github.com/LeeHyunji/python-algorithm/blob/main/4%ED%9A%8C%EC%B0%A8/quiz07_84512.py)

### 결과
    테스트 성능

    채점 결과

### 풀이
    1. 
    
<br>