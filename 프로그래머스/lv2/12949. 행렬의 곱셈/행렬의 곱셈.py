def solution(arr1, arr2):
    # 새로만들어지는 행, 열
    # arr1의 행 갯수 x arr2의 열 갯수
    answer = [[0] * len(arr2[0]) for _ in range(len(arr1))]
    
    # 2행 1열은
    # arr1의 2행과 arr2의 1열 원소들의 곱의 합
    for i in range(len(arr1)):
        for j in range(len(arr2[0])):
            for k in range(len(arr1[i])):
                answer[i][j] += arr1[i][k] * arr2[k][j]
    
    return answer