# HackerRank preparation

def pangrams(s):
    x = []
    pangram = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    for letter in s:
        if letter == " ":
            continue
        elif letter in x:
            continue
        else:
            letter = letter.upper()
            x.append(letter)
               
    x = list(set(x))
    x = sorted(x)

    if x == pangram:
        return("pangram")
    else:
        return("not pangram")
    

