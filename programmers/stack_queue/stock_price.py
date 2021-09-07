def solution(prices):

    answer = [0] * len(prices)

    for i in range(len(prices)-1):                  # 마지막 주식은 뒤에 더이상 시간이 없으므로 무조건 0초
        for j in range(i+1, len(prices)):           # 현재 주식이 떨어지는 시점 계산
            answer[i] += 1
            if prices[i] > prices[j]:
                break

    return answer