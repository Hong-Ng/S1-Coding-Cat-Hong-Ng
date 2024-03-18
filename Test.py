TimePeriod = {
    'year': 365,
    'quarter': 91.25,
    'month': 30.4167,
    'week': 7.0192,
    'day': 1
}
i = 5
it = TimePeriod['year']
i = 5/(TimePeriod['year']/TimePeriod['quarter'])
kt = TimePeriod['quarter']
k = TimePeriod['month']/kt
t = 5
p = 100

A = 100*(1+(i/k)**kt*k)