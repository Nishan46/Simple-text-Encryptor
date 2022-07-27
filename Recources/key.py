from this import d
from time import sleep
import random
from styles import *

def My(txt):
    fst = '[CRIPTOR >'
    print(f'{fst} {txt}')

def Begin():
    sleep(1)
    symbols = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
    '`','~','@','#','$','%','^','&','*','(',')','-','_','+','=','{','[','}',']',':',';','|','/','<',',','>','.','?',' ','!']
    for i in range(0,len(symbols)):
        symbols.append(symbols[i].upper())
        if(i<10):
            symbols.append(str(i))
    return(symbols)

def GetIndex(first,symbs):  
    return symbs.index(first)

def Encript(tobe,symbs,first):
    index_ = GetIndex(first,symbs)
    symbscount = (len(symbs) - 1)
    st = symbscount - index_
    criping = ''
    for items in tobe:
        cc = symbs.index(items) + st
        if cc >= (len(symbs)-1):
            gues = cc - (len(symbs)-1)
            criping += symbs[gues]
            print(f' gues --> {gues} and cc --->{cc} ')
        else:
            criping += symbs[cc]
    cripted = criping

    St.pans("blue","----- KEY GENARATED ! --- ","green",cripted)


def Testing(txt,symb,key):
    index_ = GetIndex(txt[0],symb)
    symbscount = (len(symb) - 1)
    st = symbscount - index_
    criping = ''
    for items in txt:
        cc = symb.index(items) + st
        if cc >= (len(symb)-1):
            gues = cc - (len(symb)-1)
            criping += symb[gues]
            print(f' gues --> {gues} and cc --->{cc} ')
        else:
            criping += symb[cc]
    cripted = criping
    if(cripted == key):
        St.pans("blue","--- CORRECT PASSWORD ---","green",f"--- [+]{txt}[+] ---" )
    else:
        St.pansError("red","--- INCORRECT PASSWORD ---")






            

        

        
    




