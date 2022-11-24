def solution(id_pw, db):
    return "login" if id_pw in db else "fail" if id_pw[0] not in sum(db,[]) else "wrong pw"