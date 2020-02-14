

def bubbleShort(list_of_element):
    times = len(list_of_element) - 1
    while not times == 0:
        for i in range(0, times):
            if list_of_element[i] > list_of_element[i+1]:
                t = list_of_element[i]
                list_of_element[i] = list_of_element[i+1]
                list_of_element[i+1] = t
        times -= 1
        print(list_of_element)


bubbleShort([45,78,56,12,92,2,44])