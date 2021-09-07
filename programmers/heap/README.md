# Heap
힙 내용 요약

- 힙(Heap)
  - 완전 이진트리의 일종
  - 최댓값(혹은 최솟값)이 root에 위치
  - 부모 노드는 자식 노드보다 큼(최솟값이 root에 위치하는 힙의 경우는 부모가 자식보다 작음)

------------------------------------------------
- 힙큐(heapq)
  - 파이썬(python)에서 제공하는 라이브러리
  - priority Queue 알고리즘을 제공
  - 최소 힙의 형태
  - 최대 힙을 사용하고자 한다면, 음수로 값을 바꿔 이용하면 됨
------------------------------------------------
- heapq 제공 함수
  - heapq.heapify(list)
    - list를 최소 힙 형태로 변환
  - heapq.heappush(heap, value)
    - heap에 value를 삽입
  - heapq.heappop(heap)
    - heap 상의 최솟값을 pop 하면서 return
