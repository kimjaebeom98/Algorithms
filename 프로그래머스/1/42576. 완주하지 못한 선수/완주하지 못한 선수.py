"""
완주하지 못한 선수의 이름을 return
해쉬로 품 
선수의 이름을 key, value는 동명이인의 갯수
completion을 돌아보면서 key값에 해당하는 선수를 -1 해줌
"""
def solution(participant, completion):
    participant.sort()
    completion.sort()
    for i in range(len(completion)):
        if participant[i] != completion[i]:
            return participant[i]
        
    return participant[-1]

    