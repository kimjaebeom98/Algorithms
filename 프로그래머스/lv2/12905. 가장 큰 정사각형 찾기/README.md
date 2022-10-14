# [level 2] 가장 큰 정사각형 찾기 - 12905

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/12904) 


### 채점결과

<br/>정확성: 59.6<br/>효율성: 40.4<br/>합계: 100.0 / 100.0

### 문제 설명

<p>1와 0로 채워진 표(board)가 있습니다. 표 1칸은 1 x 1 의 정사각형으로 이루어져 있습니다. 표에서 1로 이루어진 가장 큰 정사각형을 찾아 넓이를 return 하는 solution 함수를 완성해 주세요. (단, 정사각형이란 축에 평행한 정사각형을 말합니다.)</p>

<p>예를 들어</p>
<table class="table">
        <thead><tr>
<th style="text-align: center">1</th>
<th style="text-align: center">2</th>
<th style="text-align: center">3</th>
<th style="text-align: center">4</th>
</tr>
</thead>
        <tbody><tr>
<td style="text-align: center">0</td>
<td style="text-align: center">1</td>
<td style="text-align: center">1</td>
<td style="text-align: center">1</td>
</tr>
<tr>
<td style="text-align: center">1</td>
<td style="text-align: center">1</td>
<td style="text-align: center">1</td>
<td style="text-align: center">1</td>
</tr>
<tr>
<td style="text-align: center">1</td>
<td style="text-align: center">1</td>
<td style="text-align: center">1</td>
<td style="text-align: center">1</td>
</tr>
<tr>
<td style="text-align: center">0</td>
<td style="text-align: center">0</td>
<td style="text-align: center">1</td>
<td style="text-align: center">0</td>
</tr>
</tbody>
      </table>
<p>가 있다면 가장 큰 정사각형은</p>
<table class="table">
        <thead><tr>
<th style="text-align: center">1</th>
<th style="text-align: center">2</th>
<th style="text-align: center">3</th>
<th style="text-align: center">4</th>
</tr>
</thead>
        <tbody><tr>
<td style="text-align: center">0</td>
<td style="text-align: center"><code>1</code></td>
<td style="text-align: center"><code>1</code></td>
<td style="text-align: center"><code>1</code></td>
</tr>
<tr>
<td style="text-align: center">1</td>
<td style="text-align: center"><code>1</code></td>
<td style="text-align: center"><code>1</code></td>
<td style="text-align: center"><code>1</code></td>
</tr>
<tr>
<td style="text-align: center">1</td>
<td style="text-align: center"><code>1</code></td>
<td style="text-align: center"><code>1</code></td>
<td style="text-align: center"><code>1</code></td>
</tr>
<tr>
<td style="text-align: center">0</td>
<td style="text-align: center">0</td>
<td style="text-align: center">1</td>
<td style="text-align: center">0</td>
</tr>
</tbody>
      </table>
<p>가 되며 넓이는 9가 되므로 9를 반환해 주면 됩니다.</p>
<h5>제한사항</h5>

<ul>
<li>표(board)는 2차원 배열로 주어집니다.</li>
<li>표(board)의 행(row)의 크기 : 1,000 이하의 자연수</li>
<li>표(board)의 열(column)의 크기 : 1,000 이하의 자연수</li>
<li>표(board)의 값은 1또는 0으로만 이루어져 있습니다.</li>
</ul>

<h5>입출력 예</h5>
<table class="table">
        <thead><tr>
<th>board</th>
<th>answer</th>
</tr>
</thead>
        <tbody><tr>
<td>[[0,1,1,1],[1,1,1,1],[1,1,1,1],[0,0,1,0]]</td>
<td>9</td>
</tr>
<tr>
<td>[[0,0,1,1],[1,1,1,1]]</td>
<td>4</td>
</tr>
</tbody>
      </table>
<h5>입출력 예 설명</h5>

<p> 입출력 예 #1
위의 예시와 같습니다. </p>

<p> 입출력 예 #2 </p>
<p>입출력 예 #2<br>
| 0 | 0 | <code>1</code> | <code>1</code> |<br>
| 1 | 1 | <code>1</code> | <code>1</code> | <br>
로 가장 큰 정사각형의 넓이는 4가 되므로 4를 return합니다.</p>

> 출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges

### 풀이 🚀
일단 DP인데, 
왼쪽 상단, 오른쪽 상단, 왼쪽 하단 중 가장 작은 값의 + 1이 오른쪽 하단의 값이 된다  
이유는 만약 왼쪽 상단(2), 오른쪽 상단(1), 왼쪽 하단(1) 이라면 이걸 가지고 만들 수 있는 정사각형의  
한 변의 길이는 2이기 때문.... 직접 표를 그리고 테이블을 채워 나가면 이해가 쉽다 !
주의 할 점은 초반에 max_len값을 설정하는데에 있다.  
board가 길이가 1x1 표로 주어지면 board[0][0]에 값이 있으면 1을 리턴하고, 아니면 0을 리턴하게 만든다.

### 코드 📃

```python

def solution(board):
    if board[0][0] == 1:
        _max = 1
    else:
        _max = 0
    # 행
    for i in range(1, len(board)):
        # 열
        for j in range(1, len(board[0])):
            if board[i][j] == 1:
                board[i][j] = min(board[i-1][j-1], board[i-1][j], board[i][j-1]) + 1
                _max = max(_max, board[i][j])
            
    return _max*_max

```
