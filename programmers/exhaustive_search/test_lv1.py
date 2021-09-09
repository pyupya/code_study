def solution(answers):
    answer = []

    first = [1,2,3,4,5]                     # 찍은 번호들 순서
    second = [2,1,2,3,2,4,2,5]
    third = [3,3,1,1,2,2,4,4,5,5]

    first_l = first*(len(answers)//len(first)) + first[:len(answers)%len(first)]                # 문제 수 만큼 찍을 번호들을 반복해서 저장
    second_l = second*(len(answers)//len(second)) + second[:len(answers)%len(second)]
    third_l = third*(len(answers)//len(third)) + third[:len(answers)%len(third)]

    count = [0,0,0]

    for ind, i in enumerate(answers):
        if i == first_l[ind]:                               # 정답을 맞춘 경우 count를 셈
            count[0] += 1
        if i == second_l[ind]:
            count[1] += 1
        if i == third_l[ind]:
            count[2] += 1

    m_ind = count.index(max(count))                         # 정답을 가장 많이 맞춘 사람의 index를 저장
    answer.append(m_ind+1)                                  # 이게 index가 아니라 사람 번호여서 1을 더해줌
    for ind, i in enumerate(count):
        if ind != m_ind and i == count[m_ind]:              # 만약 가장 많이 맞춘 동점자 수가 여럿이면 그만큼 사람 번호를 추가
            answer.append(ind+1)
    answer.sort()                                           # 오름차순으로 정렬해서 출력
    return answer