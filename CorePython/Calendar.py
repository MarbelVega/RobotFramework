import calendar

c = calendar.TextCalendar(calendar.SUNDAY)
st = c.formatmonth(2021, 7, 0, 0)
print(st)

# team meeting on first friday of each month, give days back
for m in range(1, 13):
    cal = calendar.monthcalendar(2018, m)
    # zeros in week means days from earlier/next month
    print(cal[0])
    weekone = cal[0]
    weektwo = cal[1]

    if weekone[calendar.FRIDAY] != 0:
        meetday = weekone[calendar.FRIDAY]
    else:
        meetday = weektwo[calendar.FRIDAY]

    print(calendar.month_name[m],  meetday)
