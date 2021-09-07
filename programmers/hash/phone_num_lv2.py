def solution(phone_book):
    phone_book = sorted(phone_book)                         #string을 sort --> 사전식 정렬

    for i in range(len(phone_book)-1):                      #앞의 번호가 뒤의 번호보다 짧으면서 포함될 수 밖에 없음(사전식 정렬)
        if phone_book[i+1].startswith(phone_book[i]):
            return False



    return True