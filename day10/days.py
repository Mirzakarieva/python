def second_month(year):
    if year % 400 == 0:
        result = True
    elif year % 100 == 0:
        result = False
    elif year % 4 == 0:
        result = True
    else:
        result = False

    return result



def days_in_month(year, month):
    month_days = [31 , 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if second_month(year) == True:
        month_days[1] = 29
        days_num = month_days[month-1]
        return days_num



year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)