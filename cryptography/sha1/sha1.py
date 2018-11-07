#DONE
# To call method tall shaone(String) will return a binay string


#  set up vars
import textwrap

h0 = bin(0x67452301)[2:]
h1 = bin(0xEFCDAB89)[2:]
h2 = bin(0x98BADCFE)[2:]
h3 = bin(0x10325476)[2:]
h4 = bin(0xC3D2E1F0)[2:]
#input need to be bite wise already
def shaone(input):
    h0 = bin(0x67452301)[2:]
    h1 = bin(0xEFCDAB89)[2:]
    h2 = bin(0x98BADCFE)[2:]
    h3 = bin(0x10325476)[2:]
    h4 = bin(0xC3D2E1F0)[2:]
    if(len(h0)<32):
        h0=(len(h0)-32)*'0'+h0
    if(len(h1)<32):
        h1=(len(h1)-32)*'0'+h1
    if(len(h0)<32):
        h2=(len(h2)-32)*'0'+h2
    if(len(h0)<32):
        h3=(len(h3)-32)*'0'+h3
    if(len(h4)<32):
        h4=(len(h0)-32)*'0'+h4
    msg=''.join('{0:08b}'.format(ord(x),'b') for x in input)
    print("MSG")
    print(msg)
    if(len(msg)==0 or len(msg)%512!=0):
           msg= preprovessing(msg)
    sub=textwrap.wrap(msg,512)
    print("SUB")
    print(sub)
    #divide in to 512 subcunk
    for a in sub:
        wordsList=textwrap.wrap(a,32)
        i=16
        while i<=79:
            wordsList.append(leftrotate(xor(xor(xor(wordsList[i-3],wordsList[i-8]),wordsList[i-14]),wordsList[i-16]),1))
            i=i+1


        a1=h0
        a2=h1
        a3=h2
        a4=h3
        a5=h4
        for i in range(80):
            if i>=0 and i<=19:
                f= f1(a2,a3,a4)
                k=bin(0x5A827999)[2:]
            if i>=20 and i<=39:
                f=f2(a2,a3,a4)
                k = bin(0x6ED9EBA1)[2:]
            if i>=40 and i<=59:
                f=f3(a2,a3,a4)
                k= bin(0x8F1BBCDC)[2:]
            if i >= 60 and i <= 79:
                f=f4(a2,a3,a4)
                k = bin(0xCA62C1D6)[2:]
            if(len(k)<32):
                k=(len(k)-32)*'0'+k
            temp=gettemp(k,f,a5,wordsList[i],leftrotate(a1,5))
            if(len(temp)<32):
                temp=(len(temp)-32)*'0'+temp

            a5=ensure32(a4)
            a4=ensure32(a3)
            a3=ensure32(leftrotate(a2,30))
            a2=ensure32(a1)
            a1=ensure32(temp)
            print(i)
            print(int(a1,2))
            print(int(a2,2))
            print(int(a3,2))
            print(int(a4,2))
            print(int(a5,2))

        h0=add(h0,a1)
        h1=add(h1,a2)
        h2=add(h2,a3)
        h3=add(h3,a4)
        h4=add(h4,a5)

    hh=OR(OR(OR(leftshift(h0,128),leftshift(h1,96)),OR(leftshift(h2,64),leftshift(h3,32))),h4)
    return hex(int(hh,2))


def gettemp(k,f,e,w,aleft):
    y= int(k,2)+int(f,2)+int(e,2)+int(w,2)+ int(aleft,2)
    result='{0:0{1}b}'.format(y, 32)
    if(len(result)<32):
        result=len(result-32)*'0'+result
    return result[-32:]

def add(a,b):
    y = int(a, 2) + int(b, 2)
    result='{0:0{1}b}'.format(y, 32)
    if len(result)>=32:
        return result[len(result)-32:]
    else:
        return '0'*(32-len(result))+result
def OR(a,b):
    y=int(a,2)| int(b,2)
    return '{0:0{1}b}'.format(y, len(a))

def nd(a,b):
    y = int(a,2)& int(b,2)
    return  '{0:0{1}b}'.format(y,len(a))


def no(a):
    leng=len(a)
    max='1'*leng
    y= int(max,2)-int(a,2)
    return '{0:0{1}b}'.format(y,len(a))
def xor(a,b):
    y = int(a, 2) ^ int(b, 2)
    return '{0:0{1}b}'.format(y,len(a))
def preprovessing(msg):
    length=len(msg)
    if(length%512>=448):
        result=msg+'1'+(447+512-length%521)*'0'
    else:
        if(length%512==447):
            result=msg+'1'
        else:
            result=msg+'1'+(447-length%512)*'0'



    result =result+twobitlen(msg)
    return result

def twobitlen(msg):
    length=len(msg)
    result = "{0:b}".format(length)
    bitlen=len(result)
    if(bitlen<64):
        result='0'*(64-bitlen)+result

    return result

#take string of 2bits
def leftrotate(bit, n):
    result=bit
    if(len(bit)<32):
        result='0'*(32-len(bit))+result

    return result[n%len(bit):]+result[:n%len(bit)]

def ensure32(input):
    if len(input)<32:
        return '0'*(32-len(input))+ input
    else:
        return input[-32:]

#take string of 2 bit
def leftshift(bit,n):
    return bit+n*"0"
def f1(b,c,d):
    one = nd(b,c)
    nb=no(b)
    nbnd=nd(nb,d)
    result=OR(one,nbnd)
    return result
def f2(b,c,d):
    one =xor(b,c)
    result =xor(one,d)
    return  result
def f3(b,c,d):
    bnc=nd(b,c)
    bnd=nd(b,d)
    cnd=nd(c,d)
    return OR(OR(bnc,bnd),cnd)

def f4(b,c,d):
    return f2(b,c,d)


print(OR("101",'10'))
print("RESULT: "+ shaone("lalala"))
print(leftrotate('1100111010001010010001100000001',30))
#print("RESULT: "+ hex(int(shaone("The quick brown fox jumps over the lazy cog"),2)))
print("RESULT: "+ shaone("The quick brown fox jumps over the lazy cog"))