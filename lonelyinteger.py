# # HackerRank preparation

def lonelyinteger(a):
    for i in a:
        x = a.index(i)
        if i in a[x+1:]:
            continue
        else:
            return i
