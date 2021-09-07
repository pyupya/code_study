def solution(bridge_length, weight, truck_weights):

    Q = [0 for i in range(bridge_length)]                           # Queue를 다리 길이만큼 줘서 트럭들이 실제로 움직이는 것처럼 계속 당길예정
    answer = 0



    for ind, i in enumerate(truck_weights):
        if sum(Q)+i <= weight:                          # 다리에 트럭이 더 올라갈 수 있는 경우
            Q.pop()                                     # 다리 길이는 계속  유지시켜주기
            Q.insert(0, i)                              # 트럭이 다리에 올라감
            answer += 1
        else:                                           # 다리에 트럭이 더 올라갈 수 없는 경우. 트럭 i를 다리 위에 올리는게 목표
            while sum(Q)+i>weight:                      # pop과 push를 반복. 현재 다리에 트럭이 더 못올라가는 경우.
                if Q[bridge_length-1]==0:               # 아직 트럭이 다리를 다 못건넌 경우
                    Q.pop()
                    Q.insert(0, 0)
                    answer += 1                         # 시간 추가
                else:
                    Q.pop()                             # 트럭 한 대가 다리를 거의 다 건넌 경우
                    if sum(Q)+i<=weight:                # 트럭이 더 올라갈 수 있는가?
                        Q.insert(0, i)                  # 트럭 다리 진입 --> i가 이번 for문이 지나면 다시 돌아갈 수 없기때문에 다리에 올리고 끝내는 것.
                        answer += 1
                        break
                    else:                               # 트럭 i가 올라가지 못한 경우는 while을 다시 반복
                        Q.insert(0,0)
                        answer += 1

        if ind == len(truck_weights)-1:                 # 더 올릴 트럭이 없는 경우, 모든 트럭이 다리를 지날 때까지 반복문 돌리기.
            while sum(Q)!=0:
                Q.pop()
                Q.insert(0,0)
                answer+=1


    return answer