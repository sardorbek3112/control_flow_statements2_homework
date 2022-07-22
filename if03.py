def main(a,b,c):
    """
    Determine the number between large and small.
    Args:
        a: First number.
        b: Second number.
        c: Third number.
    Returns:
        int: return answer.
    """
    if a>b:
        if a<c:
            return a
        else:
            if c>b:
                return c
            else:
                return b
    else:
        if b<c:
            return b
        else:
            if c>a:
                return c
            else:
                return a