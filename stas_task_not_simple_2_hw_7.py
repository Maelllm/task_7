def season(month_number: int):
    if 3 <= month_number <= 5:
        return ('spring')
    if 6 <= month_number <= 8:
        return ('summer')
    if 9 <= month_number <= 11:
        return ('autumn')
    if month_number <= 2 or month_number == 12:
        return ('winter')


month = int(input('Enter montn number '))
print(season(month))
