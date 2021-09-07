def solution(progresses, speeds):

    answer = []

    days = 1
    while progresses != []:                                                         

        if progresses[0]+(days*speeds[0])<100:                              # progress의 맨 앞의 것이 끝나야 되기때문에 일단 끝날때까지 날짜 세기
            days += 1
            continue

        count = 0
        while progresses != [] and progresses[0]+(days*speeds[0])>=100:     # 끝난 process들을 pop하면서 그 개수 세기
            progresses.pop(0)
            speeds.pop(0)
            count += 1
        answer.append(count)

    return answer