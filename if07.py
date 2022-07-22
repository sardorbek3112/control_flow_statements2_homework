def main(t):
    """
    Display the message according to the following temperature conditions given to you in Celsius:
    Use the elif statments.
    Temp<0: "Freezing"
    Temp 1-10: "Very Cold"
    Temp 11-20: "Cold"
    Temp 21-30: "Normal"
    Temp 31-40: "Hot"
    Temp >40: "Very Hot"
    Args:
        temp: Temperature in Celsius.
    Returns:
        str: return answer.
    """
    if t<0:
        return "Freezing"
    elif t>0 and t<11:
        return "Very Cold"
    elif t>10 and t<21:
        return "Cold"
    elif t>20 and t<31:
        return "Normal"
    elif t>30 and t<41:
        return "Hot"
    elif t>40:
        return "Very Hot"