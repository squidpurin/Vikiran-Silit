'''
def binsearch(dataList, key):
    first = 0
    count = len(dataList)
    while 0 < count:
        step = count // 2
        mid = first + step

        if dataList[mid] > key:
            mid += 1
            first = mid
            count -= step + 1
        else:
            count = step
'''


class InvalidArgument(Exception): pass


def binsearch(dataList, key):
    if not isinstance(dataList, list):
        raise InvalidArgument()

    ai = 0
    bi = len(dataList) - 1

    while bi != ai:
        av = dataList[ai]
        bv = dataList[bi]

        step = (bi - ai) // 2
        mi = ai + step
        mv = dataList[mi]

        if ai == mi or bi == mi:
            if key != av and key != bv:
                return None
        if mv == key:
            return mi
        elif key == dataList[ai]:
            return ai
        elif key == dataList[bi]:
            return bi

        elif mv < key:
            ai = mi
        else:
            bi = mi

    return ai
