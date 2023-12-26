roman_numerals = {
        1000: 'M',
        900: 'CM',
        500: 'D',
        400: 'CD',
        100: 'C',
        90: 'XC',
        50: 'L',
        40: 'XL',
        10: 'X',
        9: 'IX',
        5: 'V',
        4: 'IV',
        1: 'I'
    }


def convert_to_roman(n):
    roman_numeral = ''
    for value, numeral in roman_numerals.items():
        while n >= value:
            roman_numeral += numeral
            n -= value
    return roman_numeral


number = 111
roman_number = convert_to_roman(number)
print(roman_number)