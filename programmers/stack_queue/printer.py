def solution(priorities, location):

    answer = 0
    Q = []
    order = []                                              # 실제 출력 순서를 저장할 list
    for ind, i in enumerate(priorities):                    # 원래 순서와 함께 우선순위를 저장
        Q.append((ind, i))



    while len(Q) > 0:
        ind, i = Q[0]                                       # 큐의 맨 앞 정보만 이용

        if len(Q) == 1:                                     # 큐에 데이터가 하나만 남은 경우 order에 저장 후 끝
            order.append(Q.pop(0))
            break

        if max(Q[1:], key=lambda x:x[1])[1] > i:            # 현재 맨 앞의 정보보다 우선순위가 높은 출력물이 있으면
            Q = Q[1:]
            Q.append((ind,i))                               # 현재 출력물의 출력 순위를 맨 뒤로 미룸
        else:
            order.append(Q.pop(0))                          # 현재 출력물의 우선 순위가 가장 높다면 출력물 순서 리스트에 저장

    for ind, i in enumerate(order):
        i0, i1 = i
        if i0 == location:                                  # 원하는 번호의 문서의 출력 순서를 answer로 출력
            answer = ind+1

    return answer