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
    if a >= b and a <= c:
        return a
    if b >= a and b <= c:
        return b
    return c
print(main(6,5,9))