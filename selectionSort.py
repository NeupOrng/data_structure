test = [99,55,4,66,28,31,36,52,38,12]

i = 0
print(test)
while not i == len(test)-1:
    tem = test[i]
    temi = i
    for x in range(i, len(test)):
        t = test[x]
        ti = x
        if t < tem:
            tem = t
            temi = ti
    t = test[i]
    test[i] = tem
    test[temi] = t
    i+=1
    print(test)