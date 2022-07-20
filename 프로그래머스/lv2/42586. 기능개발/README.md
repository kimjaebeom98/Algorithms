# [level 2] 기능개발 - 42586 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/42586) 

### 성능 요약

메모리: 10.2 MB, 시간: 0.01 ms

### 구분

코딩테스트 연습 > 스택／큐

### 채점결과

<br/>정확성: 100.0<br/>합계: 100.0 / 100.0

### 문제 설명

<p>프로그래머스 팀에서는 기능 개선 작업을 수행 중입니다. 각 기능은 진도가 100%일 때 서비스에 반영할 수 있습니다.</p>

<p>또, 각 기능의 개발속도는 모두 다르기 때문에 뒤에 있는 기능이 앞에 있는 기능보다 먼저 개발될 수 있고, 이때 뒤에 있는 기능은 앞에 있는 기능이 배포될 때 함께 배포됩니다.</p>

<p>먼저 배포되어야 하는 순서대로 작업의 진도가 적힌 정수 배열 progresses와 각 작업의 개발 속도가 적힌 정수 배열 speeds가 주어질 때 각 배포마다 몇 개의 기능이 배포되는지를 return 하도록 solution 함수를 완성하세요.</p>

<h5>제한 사항</h5>

<ul>
<li>작업의 개수(progresses, speeds배열의 길이)는 100개 이하입니다.</li>
<li>작업 진도는 100 미만의 자연수입니다.</li>
<li>작업 속도는 100 이하의 자연수입니다.</li>
<li>배포는 하루에 한 번만 할 수 있으며, 하루의 끝에 이루어진다고 가정합니다. 예를 들어 진도율이 95%인 작업의 개발 속도가 하루에 4%라면 배포는 2일 뒤에 이루어집니다.</li>
</ul>

<h5>입출력 예</h5>
<table class="table">
        <thead><tr>
<th>progresses</th>
<th>speeds</th>
<th>return</th>
</tr>
</thead>
        <tbody><tr>
<td>[93, 30, 55]</td>
<td>[1, 30, 5]</td>
<td>[2, 1]</td>
</tr>
<tr>
<td>[95, 90, 99, 99, 80, 99]</td>
<td>[1, 1, 1, 1, 1, 1]</td>
<td>[1, 3, 2]</td>
</tr>
</tbody>
      </table>
<h5>입출력 예 설명</h5>

<p>입출력 예 #1<br>
첫 번째 기능은 93% 완료되어 있고 하루에 1%씩 작업이 가능하므로 7일간 작업 후 배포가 가능합니다.<br>
두 번째 기능은 30%가 완료되어 있고 하루에 30%씩 작업이 가능하므로 3일간 작업 후 배포가 가능합니다. 하지만 이전 첫 번째 기능이 아직 완성된 상태가 아니기 때문에 첫 번째 기능이 배포되는 7일째 배포됩니다.<br>
세 번째 기능은 55%가 완료되어 있고 하루에 5%씩 작업이 가능하므로 9일간 작업 후 배포가 가능합니다. </p>

<p>따라서 7일째에 2개의 기능, 9일째에 1개의 기능이 배포됩니다.</p>

<p>입출력 예 #2<br>
모든 기능이 하루에 1%씩 작업이 가능하므로, 작업이 끝나기까지 남은 일수는 각각 5일, 10일, 1일, 1일, 20일, 1일입니다. 어떤 기능이 먼저 완성되었더라도 앞에 있는 모든 기능이 완성되지 않으면 배포가 불가능합니다.</p>

<p>따라서 5일째에 1개의 기능, 10일째에 3개의 기능, 20일째에 2개의 기능이 배포됩니다.</p>

<p>※ 공지 - 2020년 7월 14일 테스트케이스가 추가되었습니다.</p>


> 출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges


### 풀이(나) 🤣

1. 기능 개발을 완료할 때 까지 걸리는 기간을 작업마다 각각 계산한다.
2. 먼저 배포할 기능이 끝나기 전에 기능 개발을 완료한 작업들을 count한다

### 코드(나) 📃

```python
from collections import deque

progresses = [95, 90, 99, 99, 80, 99]
speeds = 	[1, 1, 1, 1, 1, 1]

new = deque()
out = []
for idx, data in enumerate(progresses):
  r = (100 - data) % speeds[idx]
  day = (100 - data) // speeds[idx]

  if r :
    day += 1
  new.append(day)

idx = 0
k = new.popleft()
cnt = 1
while new:

  if k >= new[0]:
    new.popleft()
    cnt+=1
  else:
    out.append(cnt)
    k = new.popleft()
    cnt=1

out.append(cnt)
print(out)

```

### 풀이(다른 사람)🎉

위와 같다 그러나 좀 더 파이썬의 라이브러리를 활용하여 파이썬의 강점인 코드 간결화에 신경 썻다.

차이점은 math 모듈을 이용하여 나 처럼 나머지가 잇으면 기간을 +1 하는게 아니라 어차피 나머지가 있으면 무조건 올림을 하는
ceil함수를 사용했다. 그리고 원소를 두 개를 한꺼번에 꺼내며 비교할 수 있는 zip을 썻다.

### 코드(다른 사람)📃

```python
import math

progresses1 = [95, 90, 99, 99, 80, 99]
speeds1 = 	[1, 1, 1, 1, 1, 1]

progresses = [93, 30, 55]
speeds = [1, 30, 5]

answer = []
new = [math.ceil((100-p)/s) for p, s in zip(progresses, speeds)]


idx = 0
for i in range(len(new)):
  if new[idx] < new[i]:
    answer.append(i - idx)
    idx = i
  
answer.append(len(new) - idx)
print(answer)
```
