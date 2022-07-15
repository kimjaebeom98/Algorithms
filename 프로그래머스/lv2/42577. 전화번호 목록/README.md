# [level 2] 전화번호 목록 - 42577 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/42577) 

### 성능 요약

메모리: 44.5 MB, 시간: 293.83 ms

### 구분

코딩테스트 연습 > 해시

### 채점결과

<br/>정확성: 83.3<br/>효율성: 16.7<br/>합계: 100.0 / 100.0

### 문제 설명

<p>전화번호부에 적힌 전화번호 중, 한 번호가 다른 번호의 접두어인 경우가 있는지 확인하려 합니다.<br>
전화번호가 다음과 같을 경우, 구조대 전화번호는 영석이의 전화번호의 접두사입니다.</p>

<ul>
<li>구조대 : 119</li>
<li>박준영 : 97 674 223</li>
<li>지영석 : 11 9552 4421</li>
</ul>

<p>전화번호부에 적힌 전화번호를 담은 배열 phone_book 이 solution 함수의 매개변수로 주어질 때, 어떤 번호가 다른 번호의 접두어인 경우가 있으면 false를 그렇지 않으면 true를 return 하도록 solution 함수를 작성해주세요.</p>

<h5>제한 사항</h5>

<ul>
<li>phone_book의 길이는 1 이상 1,000,000 이하입니다.

<ul>
<li>각 전화번호의 길이는 1 이상 20 이하입니다.</li>
<li>같은 전화번호가 중복해서 들어있지 않습니다.</li>
</ul></li>
</ul>

<h5>입출력 예제</h5>
<table class="table">
        <thead><tr>
<th>phone_book</th>
<th>return</th>
</tr>
</thead>
        <tbody><tr>
<td>["119", "97674223", "1195524421"]</td>
<td>false</td>
</tr>
<tr>
<td>["123","456","789"]</td>
<td>true</td>
</tr>
<tr>
<td>["12","123","1235","567","88"]</td>
<td>false</td>
</tr>
</tbody>
      </table>
<h5>입출력 예 설명</h5>

<p>입출력 예 #1<br>
앞에서 설명한 예와 같습니다.</p>

<p>입출력 예 #2<br>
한 번호가 다른 번호의 접두사인 경우가 없으므로, 답은 true입니다.</p>

<p>입출력 예 #3<br>
첫 번째 전화번호, “12”가 두 번째 전화번호 “123”의 접두사입니다. 따라서 답은 false입니다.</p>

<hr>

<p><strong>알림</strong></p>

<p>2021년 3월 4일, 테스트 케이스가 변경되었습니다. 이로 인해 이전에 통과하던 코드가 더 이상 통과하지 않을 수 있습니다.</p>

<p><a href="https://ncpc.idi.ntnu.no/ncpc2007/ncpc2007problems.pdf" target="_blank" rel="noopener">출처</a></p>


> 출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges

### 풀이(나) 🤣

1. 모든 번호에 대하여 딕셔너리를 만든다
2. phone_book에 들어 있는 번호를 하나씩 꺼내고 번호의 앞에서 부터 차례대로 
덧붙여 번호 문자열로 만들어 이 번호 문자열을 가지는게 딕셔너리에 있는지 체크 
- 예를 들어 꺼낸 번호가 '1234666'이면 '1' -> '12' -> '123' -> ... 가 딕셔너리에있는지 체크
- 마지막으로 만들어진 번호 문자열 '1234666'은 1에서 만든 딕셔너리에 당연히 있기 때문에 마지막으로
만들어진 번호 문자열을 체크하는건 생략한다.

### 코드(나) 📃

```python

def solution(phone_book):
    chk = {}
    for i in phone_book:
      if i not in chk:
        chk[i] = 1

    for i in range(len(phone_book)):
      s = ''
      for j in range(len(phone_book[i])):
        s += phone_book[i][j]
        if s == phone_book[i]:
          break
        if s in chk:
          return False

      chk[i] = 1
    
    return True
```

### 풀이(다른사람) & 코드(다른사람) 🔓

**놀랍다 너무 깔끔해서..**

1. phoneBook을 정렬하는 이유는 다른 제약을 안 줬을 때의 스트링은 오름차순 정렬
- 예를 들어 ['14561', '11145', '1234', '12', '145']가 있으면 정렬 후 ['11145', '12', '1234', '145', '14561'] 임

2. zip을 사용하여 ['11145', '12', '1234', '145', '14561'], ['12', '1234', '145', '14561']의 원소를 하나씩 꺼내서 비교
- startswith를 사용하여 '1234'의 접두어 '12'를 찾을 수 있는 것이다.



```python
def solution(phoneBook):
    phoneBook = sorted(phoneBook)

    for p1, p2 in zip(phoneBook, phoneBook[1:]):
        if p2.startswith(p1):
            return False
    return True
    
```

