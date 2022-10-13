# [level 3] 가장 긴 팰린드롬 - 12904 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/12904) 



### 채점결과

<br/>정확성: 69.3<br/>효율성: 30.7<br/>합계: 100.0 / 100.0

### 문제 설명

<p>앞뒤를 뒤집어도 똑같은 문자열을 팰린드롬(palindrome)이라고 합니다.
문자열 s가 주어질 때, s의 부분문자열(Substring)중 가장 긴 팰린드롬의 길이를 return 하는 solution 함수를 완성해 주세요.

예를들면, 문자열 s가 "abcdcba"이면 7을 return하고 "abacde"이면 3을 return합니다.</p>

<h5>제한사항</h5>

<ul>
<li>문자열 s의 길이 : 2,500 이하의 자연수</li>
<li>문자열 s는 알파벳 소문자로만 구성</li>
</ul>

<h5>입출력 예</h5>
<table class="table">
        <thead><tr>
<th>s</th>
<th>answer</th>
</tr>
</thead>
        <tbody><tr>
<td>"abcdcba"</td>
<td>7</td>
</tr>
          <tr>
<td>"abacde"</td>
<td>3</td>
</tr>
</tbody>
      </table>
<h5>입출력 예 설명</h5>

<p> 입출력 예 #1 </p>
<p> 4번째자리 'd'를 기준으로 문자열 s 전체가 팰린드롬이 되므로 7을 return합니다. </p>

<p> 입출력 예 #2 </p>
<p> 2번째자리 'b'를 기준으로 "aba"가 팰린드롬이 되므로 3을 return합니다. </p>

> 출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges

### 풀이 🚀
일단.. 감격적이다.. 예전에 코딜리티에서
k번 오른쪽 rotate를 하는 함수를 시간복잡도를 고려하여 구현하는 문제를 풀었는데  못 풀고, 답지를 참고했었다..   
근데 풀이가 너무 인상적이여서 머리로 기억했는데... 이걸 여기서 써먹다니.. 성장했구나.. ㅠㅠ  
일단 오른쪽 k번 rotate함수는 arr가 주어졌다하면 arr[-k:] + arr[:-k] 이렇게 O(1)만에 풀 수 있다.     
이 문제에 적용하는 방법은
O(N^2)만에 푸는 건데,   
s가 "abcdcba"로 주어졌다고 하자
ab, abc, abcd, ...  
bc, bcd, bcdc, ....  
이렇게 검사를 한다 그러면 이제 O(1)만에 풀어야하는데  
먼저 문자열 길이 // 2 를 k라고 구한다.
**현재 문자열의 길이가 홀수이면**
문자열[-1:k:-1] + 문자열[k] + 문자열[k-1::-1]로 구한다  
예를 들어 현재 문자열이 "abcdcba"이면 abc + d + cba를 구할 수 있다.  
**현재 문자열의 길이가 짝수이면**
문자열[-1:k-1:-1] + tmp[k-1::-1] 로 구할 수있다.

### 코드 📃

```python

# def solution(s):
#     max_len = 1
#     for idx, data in enumerate(list(s)):
#         tmp = data
#         for i in range(idx+1, len(s)):
#             tmp += s[i]
#             k = list(tmp)
#             k.reverse()
#             k = ''.join(k)
#             if k == tmp:
#                 max_len = max(len(k), max_len)

#     return max_len

def solution(s):
    max_len = 1
    for i in range(len(s)):
        tmp = s[i]
        cnt = 1
        for j in range(i+1, len(s)):
            tmp += s[j]
            cnt += 1
            k = cnt // 2
            if cnt % 2 == 1:
                if tmp[-1:k:-1] + tmp[k] + tmp[k-1::-1] == tmp:
                    max_len = max(cnt, max_len)
                    
            else:
                if tmp[-1:k-1:-1] + tmp[k-1::-1] == tmp:
                    max_len = max(cnt, max_len)
                
    return max_len      

```
