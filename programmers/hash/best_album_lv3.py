def solution(genres, plays):

    gen = {}
    gen_sum_dic = {}
    gen_sum = []

    for i, p in enumerate(zip(genres, plays)):                      # 장르별로 노래 모으기

        k, v = p

        if k not in gen:                                            # 장르에 해당하는 노래를 (고유번호, 재생횟수)로 저장
            gen[k] = [(i, v)]
            gen_sum_dic[k] = v                                      # 장르별 재생횟수 총합
        else:
            gen[k].append((i, v))
            gen_sum_dic[k] += v

    for i in genres:
        gen[i] = sorted(gen[i], key = lambda x: (-x[1], x[0]))      # 장르별 정렬(재생횟수 내림차순, 고유번호 오름차순)


    for i, v in list(gen_sum_dic.items()):
        gen_sum.append((i, v))                                      # 정렬을 위해 list에 장르별 재생횟수 정보 저장

    gen_sum = sorted(gen_sum, key=lambda x: x[1], reverse=True)     # 재생횟수 순으로 내림차순 정렬




    answer = []


    for k, v in gen_sum:
        if len(gen[k]) >= 2:
            answer.append(gen[k][0][0])                             # 장르에 노래가 2곡 이상인 경우 최대값 2개 저장
            answer.append(gen[k][1][0])
        else:
            answer.append(gen[k][0][0])                             # 장르가 key로 있다는건 일단 노래는 있다는거 --> 한곡 --> 저장

    return answer