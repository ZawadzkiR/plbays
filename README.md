Simple functions showing information about business days in Poland.

isBusinessDay () - Returns True or False if the day is a business day
Examples
Default: isBusinessDay () or isBusinessDay (today)
isBusinessDay ('2011-11-11')

lastBD () - Returns the last business day

Examples
Default: lastBD () or lastBD (today) - The last business day of today
lastBD ('2011-11-11')

BDays_list (start_date, end_date) - returns a list with True and False values for a given range of days
Examples
BDays_list ('2021-01-01', '2021-12-31')
