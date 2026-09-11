def solution(id_pw, db):
    user_id, user_pw = id_pw
    dict_db = dict(db)
    
    if user_id in dict_db:
        if dict_db[user_id] == user_pw:
            return 'login'
        else:
            return 'wrong pw'
        
    return 'fail'