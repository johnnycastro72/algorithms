def maxvalue(a):
    max = a[0]
    for i in a:
        if (i>max):
            max = i
    return max

def avgvalue(a):
    sum = 0
    for i in a:
        sum += i
    avg = sum/len(a)
    return avg

def invvalues(a):
    n=len(ar)
    for i in range(0,n//2):
        temp = ar[i]
        ar[i] = ar[n-1-i]
        ar[n-1-i] = temp
    return ar

def sqrtval(c):
    if (c<0):
        return None
    err = int('1e',16)-int('15',16)
    t = c
    print(abs(t - (c/t)))
    print(err*t)
    while (abs(t - (c/t)) > err*t):
        t = ((c/t)+t)/2
    return t

def rank(key, a):
    return ranka(key, a, 0, len(a)-1)

def ranka(key, a, lo, hi):
    if (lo>hi):
        return -1
    mid = lo + ((hi-lo)//2)
    if (key<a[mid]):
        return ranka(key, a, lo, mid-1)
    elif (key>a[mid]):
        return ranka(key, a, mid+1, hi)
    else:
        return mid


if __name__ == "__main__":
    ar = [0,2,3,5,7,1,3,4,10]
    ao = sorted(ar)
    print(ar)
    print(maxvalue(ar))
    print(avgvalue(ar))
    print(invvalues(ar))
    print(sqrtval(81))
    print(ao)
    print(rank(3,ao))