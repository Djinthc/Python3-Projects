# HackerRank preparation

def matchingStrings(strings, queries):
    results =[]
    for i in queries:
        count = 0
        if i in strings:
            count +=1
        results.append(count)
    print(results)


matchingStrings(['aba','baba','caba','war','aba'], ['aba','zzz','baba'])
