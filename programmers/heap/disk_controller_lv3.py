# 가장 작업량이 작은걸 먼저 끝내는게 가장 빠름
# 다른 작업의 대기시간을 줄일 수 있기 때문
import heapq

def solution(jobs):
    answer, now = 0, 0                                  # answer은 요청부터 종료까지 걸린 시간 총 합, now는 작업을 진행하는 현재 시점
    heap = []
    jobs_len = len(jobs)
    jobs = sorted(jobs, key=lambda x: x[0])             # 일 요청이 들어온 시점 순서대로 정렬

    while len(jobs) > 0:

        while len(jobs) > 0 and jobs[0][0] <= now:      # jobs가 있고, 현재 시점보다 앞선 시점에 요청이 들어온 작업들을 heap에 추가
            tmp = jobs.pop(0)
            heapq.heappush(heap, [tmp[1],tmp[0]])       # heap에 추가할 때는 걸리는 시간 순서대로 정렬(최소 힙)
        if len(heap) > 0:                               # 힙에 정보가 있는 경우 해당 task를 수행
            tmp = heapq.heappop(heap)
            answer += now - tmp[1] + tmp[0]
            now += tmp[0]
        else:                                           # 힙에 정보가 없는 경우, 현재 할 일이 없고, 요청도 없으므로 시간 1 증가
            now += 1
    while len(heap) > 0:                                # 위의 while문이 끝난 경우는 모든 job들이 heap에 추가된 경우.
        tmp = heapq.heappop(heap)                       # heap 순서대로 task를 수행해주면 됨.
        answer += now - tmp[1] + tmp[0]
        now += tmp[0]

    return int(answer/jobs_len)




