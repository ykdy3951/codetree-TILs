def is_leap_year(y : int) -> str:
    if y % 4:
        return 'false'
    else:
        if not y % 100 and y % 400:
            return 'false'
        else:
            return 'true'
print(is_leap_year(int(input())))