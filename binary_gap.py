def solution(N):
    # write your code in Python 3.6
    binary = bin(N)
    strBin = str(binary)[3:]
    maxZero = 0
    temp = 0
    index=0    
    nextIndex=0
    while index != -1 and nextIndex != -1:
        try:
            index = strBin.index('0')
        except:
            index = -1
            break
        try:
            nextIndex = strBin.index('1')
            temp = nextIndex-index
        except:
            temp = len(strBin)-index
            nextIndex = -1
            break
        strBin = strBin[nextIndex+1]
        if temp>maxZero:
            maxZero = temp
    return maxZero
