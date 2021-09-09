def solution(array, commands):
    answer = []

    for c in commands:
        li = sorted(array[c[0]-1:c[1]])                     # i번째에서 j번째까지의 수를 슬라이싱
        answer.append(li[c[2]-1])                           # 슬라이싱한 리스트에서 k번째 수를 가져옴

    return answer