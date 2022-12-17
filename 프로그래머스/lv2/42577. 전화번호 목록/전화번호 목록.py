def solution(phone_book):
    answer = True
    phone_book.sort()
    for i in range(len(phone_book)-1):
        a, b = list(sorted(phone_book[i:i+2], key=lambda x : len(x)))
        if a == b[:len(a)] :
            return False
    return True