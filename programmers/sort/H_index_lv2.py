def solution(citations):

    num = len(citations)                                        # h는 최대값이 citations 갯수보다 작을수밖에 없음
    citations.sort()                                            # 최댓값을 원하므로 citations의 갯수부터 하나씩 빼면서 계산

    while True:
        for i, v in enumerate(citations):
            if v >= num and len(citations[i:]) >= num:          # v가 num과 같거나 크다 --> h번 인용된 논문, len(citations[i:]) >= num은 h편 이상
                return num
        num -= 1