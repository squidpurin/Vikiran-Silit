class InvArg(Exception): pass

def toHex(n):
    try:
        format(n, 'X')
    except:
        raise InvArg("inv arg not int")
    try:
        if n < 0:
            v = n/0
    except:
        raise InvArg("inv arg neg")
    n = format(n, 'X')
    return n
