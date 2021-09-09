from itertools import permutations                                          # 순서를 고려한 조합을 위한 라이브러리

def solution(numbers):
    answer = 0

    numb = []
    for i in numbers:                                                       # 숫자를 한자리씩 뗴어서 list에 추가
        numb.append(i)
    numb.sort()


    numbs = []
    num_count = 1
    lit = []
    while num_count != len(numb)+1:                                         # 조합에 이용할 숫자의 개수
        lit.append(list(map(''.join, permutations(numb, num_count))))       # 숫자를 permutation해서 join으로 이어붙이고(string이므로) list화 시킴
        num_count += 1

    lit = sum(lit,[])                                                       # 이차원 리스트를 하나의 리스트로 합침
    lit = map(convInt,lit)                                                  # string을 int화
    lit = set(lit)                                                          # 중복 숫자 제거

    for i in lit:
        if i== 0 or i == 1:                                                 # 소수찾기
            continue
        p = True
        for t in range(1,int(i/2)+1):                                       # 끝까지 갈거 없이 절반정도까지만 약수 돌아봐도 파악 가능
            if t != 1 and i%t == 0:
                p = False
                break
        if p is True:
            numbs.append(i)

    numbs = set(numbs)
    answer = len(numbs)
    return answer

def convInt(numb):                                                          # map에서 각 숫자들에 적용할 함수
    return int(numb)