import random
def check(password):
        flag = False
        for i in password:
            if i in "1234567890":
                for i in password:
                    if i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
                        for i in password:
                            if i in "+-/*!&$#?=@":
                                flag = True
        return flag


letters = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
while True:
    q1 = int(input('Что вы хотите сделать? 1 создать пароль:'))
    if q1 == 1:
        q2 = int(input('Какой длинны вы хотите пароль?'))
        flag = False
        while flag == False:
            password = ""
            for i in range(q2):
                password += random.choice(letters)
            print(password)
            flag = check(password)
        
        if flag:
            print(password, 'Ваш пароль надёжный!')
                
        print('Ваш пароль:', password)


    