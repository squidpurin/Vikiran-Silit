class InvalidArgument(Exception): pass
class InvalidIdx(Exception): pass
class NotFound(Exception): pass

def binsearch(dataList, key):
    try:
        dataList += 1
    except:
        raise InvalidArgument("Not list")
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
    try:
        if len(dataList) < first:
            first /= 0
    except:
        raise InvalidIdx("Index Out of Range")
    try:
        first += 1
    except:
        raise NotFound("Not Found")
    return first
