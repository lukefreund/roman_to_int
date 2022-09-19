def roman_to_int(roman_numeral: str):
    """
    This function will convert a roman_numeral to an integer

    :param roman_numeral: M,D,C,l,X,V,I to form a roman numeral
    :return: The equivalent integer in base 10
    """
    number = []
    substract = []
    for index, char in enumerate(roman_numeral):
        if char == "M":
            number.append(1000)
        elif char == "D":
            number.append(500)
        elif char == "C":
            number.append(100)
        elif char == "L":
            number.append(50)
        elif char == "X":
            number.append(10)
        elif char == "V":
            number.append(5)
        elif char == "I":
            number.append(1)
        if number != sorted(number, reverse=True):
            exception_value = -2*(number[index - 1])
            substract.append(exception_value)
            number.sort(reverse=True)
    return sum(number) + sum(substract)
