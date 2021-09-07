import heapq                                            # heapq를 이용하기 위한 라이브러리

def solution(scoville, K):
    answer = 0


    heapq.heapify(scoville)                             # heapify : list를 힙으로 만들어줌
    while len(scoville) > 1:

        u1 = heapq.heappop(scoville)                    # 최소값 pop

        if u1 >= K:                                     # 최소값이 기준 K 이상이면 끝
            break

        u2 = heapq.heappop(scoville)                    # 두번째로 작은 값을 가져와서 섞음

        new_scov = u1+(u2*2)
        answer += 1

        heapq.heappush(scoville, new_scov)              # 섞은 스코빌을 추가

    if heapq.heappop(scoville) < K:                     # 위의 while문을 돌고나면 어쨌든 힙 안에는 스코빌이 둘 이상 존재(while 조건문도 그렇고, push로 값을 섞어서 하나 넣기 때문)
        answer = -1                                     # 더 섞을 수 없어서 기준 K 이상 될 수 없는 경우






    return answer