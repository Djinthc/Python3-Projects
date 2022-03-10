# HackerRank preparation
def plusMinus(arr):
    positive = 0
    negative = 0
    zeros = 0
    for liczba in arr:
        if liczba > 0:
            positive +=1
        elif liczba == 0:
            zeros +=1
        else:
            negative +=1


    positratio = positive/len(arr)
    negatratio = negative/len(arr)
    zeroratio = zeros/len(arr)
    positratio = str(positratio)
    negatratio = str(negatratio)
    zeroratio = str(zeroratio)


    if len(positratio) < 8:
        for sign in range(len(positratio),8):
            positratio = positratio+"0"
        print(positratio)
    else:
        print(positratio)
    if len(negatratio) < 9:
        for sign in range(len(negatratio),8):
            negatratio = negatratio+"0"
        print(negatratio)
    else:
        print(negatratio)
    if len(zeroratio) < 8:
        for sign in range(len(zeroratio),8):
            zeroratio = zeroratio+"0"
        print(zeroratio)
    else:
        print(zeroratio)

plusMinus([1,2,3,-1,-2,-3,0,0])
