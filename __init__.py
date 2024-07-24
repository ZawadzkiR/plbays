from datetime import timedelta, datetime, date

def isBusinessDay(date='today'):
    """
    Check if a given date is a business day.

    A business day is defined as a weekday (Monday through Friday) that is not a public holiday.
    Public holidays are predefined and include New Year's Day, Epiphany, Easter, Whit Monday, 
    Labor Day, Constitution Day, Assumption Day, All Saints' Day, Independence Day, Christmas, and Boxing Day.

    Parameters:
    date (str or datetime): The date to check in 'YYYY-MM-DD' format or as a datetime object. Defaults to 'today'.

    Returns:
    bool: True if the date is a business day, False otherwise.
    """
    if date == 'today':
        date = datetime.today().strftime('%Y-%m-%d')

    year = int(datetime.strptime(date, '%Y-%m-%d').strftime("%Y"))
    easter_calc = (2*(year%4)+ 4*(year%7) + 6*((year%19*19+24)%30) +5)%7 + (year%19*19+24)%30

    easter = (datetime.strptime(str(year) + '-03-22', '%Y-%m-%d') + timedelta(easter_calc)).strftime("%Y-%m-%d")
    wet = (datetime.strptime(str(year) + '-03-22', '%Y-%m-%d') + timedelta(easter_calc+1)).strftime("%Y-%m-%d")
    cialo = (datetime.strptime(str(year) + '-03-22', '%Y-%m-%d') + timedelta(easter_calc+60)).strftime("%Y-%m-%d")
    holidays = [str(year)+'-01-01', str(year)+'-01-06', easter, wet, str(year)+'-05-01', str(year)+'-05-03', cialo,
                str(year)+'-08-15', str(year)+'-11-01', str(year)+'-11-11', str(year)+'-12-25', str(year)+'-12-26']

    if datetime.strptime(date, '%Y-%m-%d').weekday() in (5,6) or date in holidays:
        return False
    else:
        return True


def lastBD(date='today'):
    """
    Find the most recent business day before or on the given date.

    This function will iterate backward from the given date until it finds a business day.

    Parameters:
    date (str or datetime): The date to start from in 'YYYY-MM-DD' format or as a datetime object. Defaults to 'today'.

    Returns:
    str: The most recent business day in 'YYYY-MM-DD' format.
    """
    if date == 'today':
        date = datetime.today().strftime('%Y-%m-%d')

    i = 1
    bd = False
    while not bd:
        if isBusinessDay((datetime.strptime(date, '%Y-%m-%d') - timedelta(i)).strftime("%Y-%m-%d")):
            bd = True
            return (datetime.strptime(date, '%Y-%m-%d') - timedelta(i)).strftime("%Y-%m-%d")
        else:
            i += 1


def nextBD(date='today'):
    """
    Find the next business day after or on the given date.

    This function will iterate forward from the given date until it finds a business day.

    Parameters:
    date (str or datetime): The date to start from in 'YYYY-MM-DD' format or as a datetime object. Defaults to 'today'.

    Returns:
    str: The next business day in 'YYYY-MM-DD' format.
    """
    if date == 'today':
        date = datetime.today().strftime('%Y-%m-%d')

    i = 1
    bd = False
    while not bd:
        if isBusinessDay((datetime.strptime(date, '%Y-%m-%d') + timedelta(i)).strftime("%Y-%m-%d")):
            bd = True
            return (datetime.strptime(date, '%Y-%m-%d') + timedelta(i)).strftime("%Y-%m-%d")
        else:
            i += 1


def BDays_list(start_date, end_date):
    """
    Generate a list of business days between two dates.

    This function returns a list of dates between start_date and end_date, inclusive, with each date marked 
    as either a business day (True) or not (False).

    Parameters:
    start_date (str or datetime): The start date in 'YYYY-MM-DD' format or as a datetime object.
    end_date (str or datetime): The end date in 'YYYY-MM-DD' format or as a datetime object.

    Returns:
    list of lists: Each sublist contains a date in 'YYYY-MM-DD' format and a boolean indicating if it's a business day.
    """
    def daterange(start_date, end_date):
        for n in range(int((end_date - start_date).days) + 1):
            yield start_date + timedelta(n)

    list_ = []
    start_date = datetime.strptime(start_date, '%Y-%m-%d')
    end_date = datetime.strptime(end_date, '%Y-%m-%d')
    for single_date in daterange(start_date, end_date):
        list_.append([single_date.strftime("%Y-%m-%d"), isBusinessDay(single_date.strftime("%Y-%m-%d"))])
    return list_
