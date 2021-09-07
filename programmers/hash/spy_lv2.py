import math

def solution(clothes):

    clothes_dic = {}                                #옷의 종류(key: 얼굴, 상의, 하의, 겉옷), 옷들(Value)

    for name, c_type in clothes:                    #옷 종류별로 key, value dictionary 생성
        if c_type not in clothes_dic:
            clothes_dic[c_type] = [name]
        else: clothes_dic[c_type].append(name)

    comb = 1                                        
    for l in clothes_dic.values():                  #옷 입는 방법 전체 경우의 수 - 1(아무것도 안입는 경우의 수는 뺀 것)
        comb = comb*(len(l)+1)                      #옷들 중 하나라도 입으면 되기 때문에 아무것도 안입는 경우만 빼면 됨


    return comb-1