import random
def gen_pass(len_password):
    words=("+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890")
    password=""
    for i in range(len_password):
        password+=random.choice(words)
    return password

def coin(flip):
    flip = random.randint(0,1)
    if flip == 0:
        return "OREL"
    else:
        return "RESHKA"