"""
Given no of days convert to Year, Week, Months
Assume year is 365 days and months is 30 days
"""


def days_converter(n):
    year = n // 365
    n = n % 365

    month = n // 30
    n = n % 30

    week = n // 7
    n = n % 7

    print(f"{year} Years  {month}  Months  {week}  Weeks   {n}  Days")


days_converter(200)
days_converter(956)