def solution(numbers):
    answer = ''

    numbers = list(map(str, numbers))                   # 숫자를 string으로 변환 --> 사전식 역순으로 정렬하기 위해서
    numbers.sort(key = lambda x: x*4, reverse=True)     # 문제에서 요구하는 제한사항 중, 원소가 0~ 1000의 수
                                                        # 1의 자리 수와 그 이상의 자리 수들을 비교하기 위함
                                                        # ex) 3, 30을 비교하면 330이 되어야하는데, 사전 역순 정렬시, 30이 더 앞으로 옴. --> 303이 됨
                                                        # 이를 위해 3->3333으로, 30 -> 30303030으로 변환 시, 사전식 역순 상 3333이 더 앞으로 옴

    return str(int(''.join(numbers)))