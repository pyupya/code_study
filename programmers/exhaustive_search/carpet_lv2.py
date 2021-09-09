def solution(brown, yellow):
    answer = []

    full = brown + yellow                               # brown과 yellow의 합이 카펫의 넓이

    for i in range(3, int(full/3)+3):                   # 갈색 격자 수 > 8, 노란 격자 수 > 1은 카펫의 최소 크기가 3x3임을 의미
                                                        # 가로의 길이를 반복시키고, 세로의 길이를 찾는 과정
        if full%i == 0 and ((i*2)+(full/i*2))-4 == brown and (i-2)*(full/i-2) == yellow:    # 1. 넓이를 가로로 나누었을 때 나누어 떨어짐
            answer.append(i)                                                                # 2. 둘레의 길이(brown의 수)가 계산한 식과 일치하는가
            answer.append(full/i)                                                           # 3. brown을 뺀 나머지 노란색 수가 계산 식과 같은가
            answer.sort(reverse=True)                                                       # 가로 길이가 무조건 더 기므로, 역순으로 sorting
            break

    return answer