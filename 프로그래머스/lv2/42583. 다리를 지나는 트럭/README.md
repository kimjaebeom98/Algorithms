# [level 2] 다리를 지나는 트럭 - 42583 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/42583) 

### 성능 요약

메모리: 10.2 MB, 시간: 0.01 ms

### 구분

코딩테스트 연습 > 스택／큐

### 채점결과

<br/>정확성: 100.0<br/>합계: 100.0 / 100.0

### 문제 설명

<p>트럭 여러 대가 강을 가로지르는 일차선 다리를 정해진 순으로 건너려 합니다. 모든 트럭이 다리를 건너려면 최소 몇 초가 걸리는지 알아내야 합니다. 다리에는 트럭이 최대 bridge_length대 올라갈 수 있으며, 다리는 weight 이하까지의 무게를 견딜 수 있습니다. 단, 다리에 완전히 오르지 않은 트럭의 무게는 무시합니다.</p>

<p>예를 들어, 트럭 2대가 올라갈 수 있고 무게를 10kg까지 견디는 다리가 있습니다. 무게가 [7, 4, 5, 6]kg인 트럭이 순서대로 최단 시간 안에 다리를 건너려면 다음과 같이 건너야 합니다.</p>
<table class="table">
        <thead><tr>
<th>경과 시간</th>
<th>다리를 지난 트럭</th>
<th>다리를 건너는 트럭</th>
<th>대기 트럭</th>
</tr>
</thead>
        <tbody><tr>
<td>0</td>
<td>[]</td>
<td>[]</td>
<td>[7,4,5,6]</td>
</tr>
<tr>
<td>1~2</td>
<td>[]</td>
<td>[7]</td>
<td>[4,5,6]</td>
</tr>
<tr>
<td>3</td>
<td>[7]</td>
<td>[4]</td>
<td>[5,6]</td>
</tr>
<tr>
<td>4</td>
<td>[7]</td>
<td>[4,5]</td>
<td>[6]</td>
</tr>
<tr>
<td>5</td>
<td>[7,4]</td>
<td>[5]</td>
<td>[6]</td>
</tr>
<tr>
<td>6~7</td>
<td>[7,4,5]</td>
<td>[6]</td>
<td>[]</td>
</tr>
<tr>
<td>8</td>
<td>[7,4,5,6]</td>
<td>[]</td>
<td>[]</td>
</tr>
</tbody>
      </table>
<p>따라서, 모든 트럭이 다리를 지나려면 최소 8초가 걸립니다.</p>

<p>solution 함수의 매개변수로 다리에 올라갈 수 있는 트럭 수 bridge_length, 다리가 견딜 수 있는 무게 weight, 트럭 별 무게 truck_weights가 주어집니다. 이때 모든 트럭이 다리를 건너려면 최소 몇 초가 걸리는지 return 하도록 solution 함수를 완성하세요.</p>

<h5>제한 조건</h5>

<ul>
<li>bridge_length는 1 이상 10,000 이하입니다.</li>
<li>weight는 1 이상 10,000 이하입니다.</li>
<li>truck_weights의 길이는 1 이상 10,000 이하입니다.</li>
<li>모든 트럭의 무게는 1 이상 weight 이하입니다.</li>
</ul>

<h5>입출력 예</h5>
<table class="table">
        <thead><tr>
<th>bridge_length</th>
<th>weight</th>
<th>truck_weights</th>
<th>return</th>
</tr>
</thead>
        <tbody><tr>
<td>2</td>
<td>10</td>
<td>[7,4,5,6]</td>
<td>8</td>
</tr>
<tr>
<td>100</td>
<td>100</td>
<td>[10]</td>
<td>101</td>
</tr>
<tr>
<td>100</td>
<td>100</td>
<td>[10,10,10,10,10,10,10,10,10,10]</td>
<td>110</td>
</tr>
</tbody>
      </table>
<p><a href="http://icpckorea.org/2016/ONLINE/problem.pdf" target="_blank" rel="noopener">출처</a></p>

<p>※ 공지 - 2020년 4월 06일 테스트케이스가 추가되었습니다.</p>


> 출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges

### 풀이 1️⃣

0. 다리의 길이 만큼 0으로 초기화 해준다.
1. 일단 시간이 지날 때 마다 다리의 앞 부분을 pop 시켜준다
- 어차피 뒤에서 다리에 새로 들어 올 조건을 파악한 후에 조건이 만족하면 트럭을 넣어주거나 만족하지 않으면 0을 넣으면 되기 때문
2. 다리에 들어올 조건을 파악하는데, 조건을 만족하여 트럭이 들어오면 다리에 트럭 무게를 넣어주고 
아니면 0을 넣는다

### 코드 📃

```python

bridge_length = 100
weight = 100
truck_weights = [10]

bridge = [0 for _ in range(bridge_length)]


time = 0
while bridge:
  time += 1
  bridge.pop(0)

  if truck_weights:
    if sum(bridge) + truck_weights[0] <= weight:
      bridge.append(truck_weights.pop(0))
    else:
      bridge.append(0)

print(time)

```

### 🤣

맨 처음 pop(0) 대신 popleft()를 사용할려고 deque를 사용했는 데, 시간 초과가 났다.
그러나 그래도 pop(0)를 사용해도 시간이 너무 오래걸렸다... 그래서 어디가 문제일 까 생각을 했는데
아마 sum일 것 같다 그리고 while문에서 bridge에 의미없는 값이 잇어도 길이 계산을 하기 위해
계속 남아있으니깐 이것 또한 개선하면 시간이 줄어들 것이다.

### 코드(수정) 📃

```python

from collections import deque


bridge_length = 100
weight = 100
truck_weights = [10]

truck_weights = deque(truck_weights)
bridge = deque([0 for _ in range(bridge_length)])
total = 0
time = 0
while truck_weights:
  time += 1
  k = bridge.popleft()

  if k :
    total -= k

  if total + truck_weights[0] <= weight:
    bridge.append(truck_weights.popleft())
    total += bridge[-1]
  else:
    bridge.append(0)

time += len(bridge)
print(time)

```

### 😊
매 time마다 sum을 사용하여 요소들을 모두 더해서 조건을 비교하는 것은 엄청난 낭비이다.
( 파이썬 내장함수 sum의 시간복잡도를 찾진 못 했지만 아마..?)
그래서 total로 다리에 들어 오는 것들을 합하여 현재 다리의 트럭들의 무게를 추적하는 것이다
또 bridge에 의미없는 값을 다 pop 시킬 때 까지 기다리지말고 의미없으면 바로 반복문을 종료해서
남은 bridge의 길이를 더 해줬다! 재밌구만 아주!


