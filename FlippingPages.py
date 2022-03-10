# HackerRank preparation

def pageCount(n, p):
    if n % 2==0:
        n += 1
    arr = []
    for i in range(0,n,2):
        arr.append((i,(i+1)))
    x = 0
    for i in range(len(arr)):
        if p not in arr[i]:
            x +=1
            print(x)
            print(arr)
        else:
            break
    if x == 0 or x ==len(arr)-1:
        return 0
    elif x <= len(arr)/2:
        return x
    else:
        return len(arr)-1 - x
            
        


print(pageCount(5,4))
