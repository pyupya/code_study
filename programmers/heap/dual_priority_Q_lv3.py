def solution(operations):                   # 우선순위 큐를 이용하지 않고 단순 min, max로 문제를 해결한 경우
    answer = [0, 0]
    Q = []

    for ind, i in enumerate(operations):
        operate = i.split()
        if operate[0] == 'I':
            Q.append(int(operate[1]))
        elif len(Q) != 0 and operate[0] == 'D':
            if operate[1] =='1':
                Q.remove(max(Q))
            elif operate[1] =='-1':
                Q.remove(min(Q))
    if len(Q) > 0:
        answer[0] = max(Q)
        answer[1] = min(Q)
    return answer