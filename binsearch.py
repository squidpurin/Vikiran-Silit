class InvalidArgument(Exception): pass

def binsearch(dataList, key):
    try:
        type(dataList)==list
    except:
        raise InvalidArgument("your description of the error")
    first = 0
    count = len(dataList)
    while 0 < count:
        step = count / 2
        mid = first + step

        if dataList[mid] > key:
            mid += 1
            first = mid
            count -= step + 1
        else:
            count = step


    return first
