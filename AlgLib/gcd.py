def gcd(p, q):
    if (q==0): 
        return p
    r = p % q
    return gcd(q, r)

if __name__ == "__main__":
    a = gcd(84,24)
    print(a)