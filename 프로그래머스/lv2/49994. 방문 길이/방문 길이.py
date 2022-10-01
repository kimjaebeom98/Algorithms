"""
처음 개척한 루트의 길이를 구하는 거임
bfs로 풀면서 distance배열을 만들고 distance배열에 값이 없으면 방문을 안했다는거고
distance배열에 값이 있으면 무시해야함 명령어

"""

def solution(dirs):
    # 명령어에 따라 현재 위치에서 이동시켜줄 좌표들임
    tmp = set()
    x, y = 0, 0
    for di in dirs:
        if di == 'U' and y < 5:
            tmp.add(((x, y), (x, y+1)))
            y += 1
        elif di == 'D' and y > -5:
            tmp.add(((x, y-1), (x, y)))
            y -= 1
        elif di == 'L' and x > -5:
            tmp.add(((x-1, y), (x, y)))
            x -= 1
        elif di == 'R' and  x < 5:
            tmp.add(((x, y), (x+1, y)))
            x += 1
            
        
    return len(tmp)

            