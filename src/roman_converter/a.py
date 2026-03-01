def to_roman(arabic: int) -> str:
    roman_map = [ # pair numerals to letters
        (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
        (100, "C"), (90, "XC"), (50, "L"), (40, "XL"), (10, "X"),
        (9, "IX"), (5, "V"), (4, "IV"), (1, "I")
    ]
    conversion = ""
    for num, roman in roman_map:
        while arabic >= num: # input >= to current num
            conversion += roman # add mapped letter
            arabic -= num # take away recorded value
    return conversion

def from_roman(roman: str) -> int:
    return 0
