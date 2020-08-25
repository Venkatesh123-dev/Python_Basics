import random

def gen_pass(num=8):
    upper = chr(random.randint(65,90))
    lower = chr(random.randint(97,122))
    special_chars = ["!","@","#","$"]
    special = random.choice(special_chars)
    digits = random.randint(10000,99999)
    
    password = upper+lower+special+str(digits)
    
    l = random.sample(password,num)
    
    return ("").join(l)

result = gen_pass(6)
print(result)
