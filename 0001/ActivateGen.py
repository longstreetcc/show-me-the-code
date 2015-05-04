#6K2KY-BFH24-PJW6W-9GK29-TMPWP

import random
sum = 200

def getnum():
    return random.randint(0,9)

def getchar():
    return chr(random.randint(65,90))

def getwhat():
    return  str(getnum()) if getnum()%2==0 else getchar()

for n in range(sum):
    code=''
    for i in range(5):
        for j in range(5):
            code +=getwhat()
        if i != 4:    
            code+= '-'
    print code
