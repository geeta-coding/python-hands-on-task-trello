import re
def password_strength(password):
    score = 0
    # len of password
    if len(password)>=8:
        score +=1
    # uppercase letter
    if re.search(r"[A-Z]",password):
        score += 1
    # lowercase letter
    if re.search(r"[a-z]",password):
        score += 1

    # numbers 
    if re.search(r"[0-9]",password):
        score += 1
    
    # special character
    if re.search(r"[!@#$%^&*()<>,.;':{}\[\]]", password):
        score += 1


    #determining a score
    if score <=2:
        stren = "weak"
    elif score <=3:
        stren = "medium"

    elif score <=4:
        stren = "strong"
    else :
        stren = "very strong"

    return score,stren
    
    
password = input("ENter the password for check the score :  ")
score,stren = password_strength(password)

print("password score : ",score)
print("password strength : ",stren)