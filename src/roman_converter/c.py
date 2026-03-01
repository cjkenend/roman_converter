def to_roman(arabic: int) -> str:
    roman_map = [(1000,"M"),(500,"D"),(100,"C"),(50,"L"),(10,"X"),(5,"V"),(1,"I")]
    conversion = ""
    for num, roman in roman_map:
        count = arabic // num
        if count >= 1:
            conversion += roman * count # repeats roman count times
            arabic -= num * count
    return conversion

def from_roman(roman: str) -> int:
    return 0
