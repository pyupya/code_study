def solution(participant, completion):

    part_dict = {}                          #참가자 dictionary

    for n, name in enumerate(participant):  #동명이인 검수
        if name not in part_dict:
            part_dict[name] = 1
        else:
            part_dict[name] += 1



    com_dict = {}                           #완주자 dictionary

    for n, name in enumerate(completion):   #동명이인 검수
        if name not in com_dict:
            com_dict[name] = 1
        else:
            com_dict[name] += 1

    answer = ''
    for name in list(com_dict.keys()):     #참가자 - 완주자
        part_dict[name] = part_dict[name] - com_dict[name]

    for k,v in list(part_dict.items()):     #완주하지 못한 사람은 한 명 --> value가 0보다 크면 그 이름을 return
        if v > 0:
            answer = k
            break

    return answer