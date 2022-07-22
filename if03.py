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
            return c-b
        else:
            if c>b:
                return a-b
            else:
                return a-c
    else:
        if b<c:
            return c-a
        else:
            if c>a:
                return b-a
            else:
                return b-c