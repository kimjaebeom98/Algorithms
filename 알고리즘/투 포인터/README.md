# 💡 투 포인터가 뭔데?
이름 그대로 포인터(인덱스) 두 개를 써서 배열이나 리스트를 효율적으로 탐색하는 기법. 완전 탐색(Brute Force)으로 풀면 시간 복잡도가 O(N 
2
 ) 이렇게 되는데, 투 포인터 쓰면 **O(N)** 으로 가능

보통 **'시작 포인터'** 랑 **'끝 포인터'** 를 두거나, 두 포인터가 같은 방향으로 움직이거나, 다른 방향으로 움직이면서 특정 조건을 만족하는 부분을 찾는 데 활용됨

<br/>

# 🧐 투 포인터는 언제 쓰면 좋을까?

1. 정렬된 배열/리스트에서 특정 조건을 만족하는 두 요소를 찾아야 할 때 (예: 합이 특정 값이 되는 두 수).
2. 배열이나 리스트에서 **부분 배열(Subarray)** 이나 **부분 문자열(Substring)** 중 특정 조건을 만족하는 구간을 찾아야 할 때 (이건 슬라이딩 윈도우랑 비슷하게 쓰일 때도 있음).
3. 배열의 양 끝에서부터 탐색해야 할 때.

<br/>

# 🛠️ 투 포인터 작동 방식 (핵심)

1. 포인터 초기화: 보통 두 포인터를 배열의 시작과 끝, 또는 둘 다 시작 지점에 둬.
2. 조건 확인: 두 포인터가 가리키는 값들을 가지고 문제의 조건을 확인해.
3. 포인터 이동: 조건에 따라 포인터 중 하나 또는 둘 다를 이동시켜.
보통 합이 작으면 왼쪽 포인터를 늘리고, 합이 크면 오른쪽 포인터를 줄이는 식.
같은 방향으로 움직일 때는 start 포인터와 end 포인터를 함께 이동시켜.
4. 반복: 포인터들이 서로 교차하거나, 특정 조건을 만족할 때까지 2~3번 과정을 반복해!

<br/>

# 👀 Example 

**두 수의 합 (Two Sum) - 정렬된 배열 (Java 버전)**

문제: 정렬된 정수 배열 nums와 목표값 target이 주어졌을 때, 합이 target이 되는 두 숫자의 인덱스를 찾아라.

```java

public class TwoSumSorted {

    public static int[] twoSumSorted(int[] nums, int target) {
        int left = 0;
        int right = nums.length - 1; // 배열의 마지막 인덱스

        while (left < right) {
            int currentSum = nums[left] + nums[right];

            if (currentSum == target) {
                return new int[]{left, right}; // 인덱스 배열 반환
            } else if (currentSum < target) {
                left++; // 합이 작으면 left 포인터 증가
            } else { // currentSum > target
                right--; // 합이 크면 right 포인터 감소
            }
        }
        
        return new int[]{}; // 못 찾았을 경우 빈 배열 반환
    }

    public static void main(String[] args) {
        // 예시 1
        int[] nums1 = {2, 7, 11, 15};
        int target1 = 9;
        int[] result1 = twoSumSorted(nums1, target1);
        System.out.println("정렬된 배열: " + java.util.Arrays.toString(nums1) + ", 목표 합: " + target1);
        System.out.println("결과 인덱스: " + java.util.Arrays.toString(result1)); // 출력: [0, 1] (2 + 7 = 9)

        System.out.println(); // 한 줄 띄우기

        // 예시 2
        int[] nums2 = {1, 3, 4, 8, 10};
        int target2 = 7;
        int[] result2 = twoSumSorted(nums2, target2);
        System.out.println("정렬된 배열: " + java.util.Arrays.toString(nums2) + ", 목표 합: " + target2);
        System.out.println("결과 인덱스: " + java.util.Arrays.toString(result2)); // 출력: [1, 2] (3 + 4 = 7)
    }
}

```

코드 설명:

1. left와 right 포인터를 각각 배열의 시작과 끝에 배치해.
2. while (left < right) 조건으로 두 포인터가 교차하지 않을 때까지 반복
3. currentSum을 계산하고, target과 비교해서 left 또는 right 포인터를 적절히 이동

<hr/>

<br/>

**특정 합을 가지는 부분 배열의 개수 (Java 버전)**

문제: 양의 정수로 이루어진 배열 nums와 목표값 target이 주어졌을 때, 합이 target이 되는 연속된 부분 배열의 개수를 찾아라.

```java


public class CountSubarraysWithSum {

    public static int countSubarraysWithSum(int[] nums, int target) {
        int count = 0;
        int start = 0;
        int currentSum = 0;

        // end 포인터를 배열 끝까지 이동시키면서 윈도우 확장
        for (int end = 0; end < nums.length; end++) {
            currentSum += nums[end]; // end 포인터가 가리키는 값을 현재 합에 더함

            // 현재 합이 target보다 크거나 같아지면, start 포인터를 이동시켜 윈도우 축소
            while (currentSum >= target) {
                if (currentSum == target) {
                    count++; // 합이 target과 같으면 개수 증가
                }
                
                currentSum -= nums[start]; // start 포인터가 가리키는 값을 현재 합에서 뺌
                start++; // start 포인터 이동
            }
        }
            
        return count;
    }

    public static void main(String[] args) {
        // 예시 1
        int[] nums1 = {1, 2, 3, 2, 5};
        int target1 = 5;
        int result1 = countSubarraysWithSum(nums1, target1);
        System.out.println("배열: " + java.util.Arrays.toString(nums1) + ", 목표 합: " + target1);
        System.out.println("합이 " + target1 + "인 부분 배열 개수: " + result1); // 출력: 2 ([2,3], [5])

        System.out.println(); // 한 줄 띄우기

        // 예시 2
        int[] nums2 = {1, 1, 1, 1, 1};
        int target2 = 3;
        int result2 = countSubarraysWithSum(nums2, target2);
        System.out.println("배열: " + java.util.Arrays.toString(nums2) + ", 목표 합: " + target2);
        System.out.println("합이 " + target2 + "인 부분 배열 개수: " + result2); // 출력: 3 ([1,1,1], [1,1,1], [1,1,1])
    }
}
```
코드 설명:

1. end 포인터는 for 루프를 통해 배열의 끝까지 한 칸씩 전진
2. currentSum이 target 이상이 되면, while 루프 안에서 start 포인터를 전진시키면서 currentSum을 줄여나감
3. currentSum이 target과 정확히 같아지는 순간 count를 증가.

