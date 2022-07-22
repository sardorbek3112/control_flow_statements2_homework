def mix(a,b,c):
    if a>b:
        if a>c:
            return a
        else:
            return c
    else:
        if b>c:
            return b
        else:
            return c
def max(a,b,c,n,m,o):
    if a>b:
        if a>c:
            return n
        else:
            return o
    else:
        if b>c:
            return m
        else:
            return o
def main(n):
    """
    Find the index of the largest digit of the five-digit number.
    Args:
        n: Five-digit number.
    Returns:
        int: return answer.
    """
    x1 = n%10
    x2 = n//10%10
    x3 = n//100%10
    x4 = n//1000%10
    x5 = n//10000%10
    mx = mix(x1,x2,x3)
    mi = max(x1,x2,x3,1,2,3)
    mi = max(mx,x4,x5,mi,4,5) 
    return mi

