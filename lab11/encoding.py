import math
from random import randint
from types import coroutine
import numpy 

def setKey():
    a = 0
    while a == 0:
        t1 = open('text.txt', 'r', encoding="utf-8")

        s1 = t1.read()

        size = 4

        keyValue = [[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]


        key = [keyValue.pop(randint(0,len(keyValue)-1)) for i in range(size)]

        #print(key)

        kID = str(size)

        temp = ''
        for i in key:
            temp = temp + str(i.index(1))

        kID = kID + temp

        kID = kID + str(math.ceil(len(s1)/16))

        with open('key.txt', 'w') as k:
            k.write(kID)
    #3021
    #2301
    #3102
    #2130
    #1032
    #0231
    #1203
    #0123
    #2031
    #2013
    #1302    
        if temp == '3021' or temp == '2301' or temp == '3102' or temp == '2130' or temp == '1032' or temp[:2] == '02' or temp == '1203' or temp == '0123' or temp[:2] == '20' or temp[:2] == '13' or temp == '3120' or temp == '3210' or temp == '0312':
            a = 0
        else:
            a = 1



def getKey():
    kr = ''
    with open('key.txt','r') as k:
        kr = k.read()

    #print(kr)

    size = int(kr[0])

    key = numpy.zeros((size,size), dtype=int)
    for i in range(1,size+1):
        key[i-1][int(kr[i])] = 1

    blocks = int(kr[5:])

    #print(size, key, blocks, sep = '\t')

    return [size, key, blocks]



def encrypt():

    k = getKey()

    size = k[0]   
    key = k[1]
    blocks = k[2]

    t1 = open('text.txt', 'r', encoding="utf-8")

    s1 = t1.read()

    print('text =', s1)
    s2 = ''

    l = [[['*' for i in range(size)] for x in range(size)] for y in range(blocks)]

    count = 0
    for x in range(len(l)):
        for y in range(size):
            for z in range(size):
                if(count>len(s1)-1):
                    break
                l[x][y][z] = s1[count]
                count = count + 1       

    #2310
    #0321
    #3012
    #1023
    #3201
    #1230
    #3201
    #

    #3021
    #2301
    #3102
    #2130
    #1032
    #0231
    #1203
    #0123
    #2031
    #2013

    for x in range(len(l)):
    # 0 градусов
        for y in range(size):
            for z in range(size):
                if(key[y][z]== 1):            
                    s2 = s2 + l[x][y][z]

    # 90 градусов
        for y in range(size):
            for z in range(size):
                if(key[size-z-1][y]== 1):            
                    s2 = s2 + l[x][y][z]

    # 180 градусов
        for y in range(size):
            for z in range(size):
                if(key[size-y-1][size-z-1]== 1):            
                    s2 = s2 + l[x][y][z]

    # 270 градусов
        for y in range(size):
            for z in range(size):
                if(key[z][size-y-1]== 1):            
                    s2 = s2 + l[x][y][z]

    print('зашифрованное сообщение:',s2)

    t2 = open('encrypt_file.txt','w', encoding="utf-8")

    for s in s2:
        t2.write(s)

    t1.close()
    t2.close()

def decrypt():
    k = getKey()

    size = k[0]   
    key = k[1]
    blocks = k[2]

    t1 = open('encrypt_file.txt','r', encoding="utf-8")

    s2 = t1.read()

    s1 = ''

    l = [[['' for i in range(size)] for x in range(size)] for y in range(blocks)]

    count = 0

    for x in range(len(l)):
    # 0 градусов
        for y in range(size):
            for z in range(size):           
                if(key[y][z]== 1) & (len(s2)>count):     
                    if s2[count] == '*':
                        l[x][y][z] = ''
                    else:
                        l[x][y][z] = s2[count]
                    count = count + 1

    # 90 градусов
        for y in range(size):
            for z in range(size):
                if(key[size-z-1][y]== 1) & (len(s2)>count):            
                    if s2[count] == '*':
                        l[x][y][z] = ''
                    else:
                        l[x][y][z] = s2[count]
                    count = count + 1

    # 180 градусов
        for y in range(size):
            for z in range(size):
                if(key[size-y-1][size-z-1]== 1) & (len(s2)>count):            
                    if s2[count] == '*':
                        l[x][y][z] = ''
                    else:
                        l[x][y][z] = s2[count]
                    count = count + 1

    # 270 градусов
        for y in range(size):
            for z in range(size):
                if(key[z][size-y-1]== 1) & (len(s2)>count):            
                    if s2[count] == '*':
                        l[x][y][z] = ''
                    else:
                        l[x][y][z] = s2[count]
                    count = count + 1

    t2 = open('decrypt_file.txt','w', encoding="utf-8")

    for x in range(len(l)):
        for y in range(size):
            for z in range(size):           
                s1 = s1 + l[x][y][z]

    print('Расшифрованное сообщение:',s1)

    for s in s1:
        t2.write(s)

    t1.close()
    t2.close()

t = 0
while t == 0:
    print('''
    1)Сгенерировать ключ
    2)Зашифровать
    3)Расшифровать
    
    0)Выйти''')
    a = input("Выберите действие:")


    if a == '0':
        t = 10
    if a == '1':
        setKey()        
    if a == '2':
        encrypt()        
    if a == '3':
        decrypt()
        
    
    
    