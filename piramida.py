# Bardzo ciekawe zadanie mające na celu zbudowanie piramidy z klocków.

c0 = int(input("Napisz liczbę: "))
count = 0

while c0 != 1:
    if c0 % 2 == 0:
        c0 = int(c0 * 0.5)
        print (c0)
        count += 1
    else:
        c0 = int(3* c0 + 1)
        count +=1
        print (c0)
print (c0, "przekształceń: ", count)
