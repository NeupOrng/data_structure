test = [99,55,4,66,28,31,36,52,38,12]

i = 0
print(f"list zin {test}")
while not i == len(test):
    tem = test[i]
    temi = i
    for x in range(i, len(test)):
        t = test[x]
        if tem < t:
            tem = t
            temi = x
    del test[temi]
    test[:0] = [tem]
    print(test)
    i+=1