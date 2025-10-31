from datetime import timedelta, datetime, date as _date

def _to_ymd(d):
    """Zwraca string 'YYYY-MM-DD' dla wejścia: 'today' | str | datetime | date."""
    if d == 'today':
        return datetime.today().strftime('%Y-%m-%d')
    if isinstance(d, (datetime, _date)):
        return d.strftime('%Y-%m-%d')
    return d  # zakładamy format 'YYYY-MM-DD'

def isBusinessDay(d='today'):
    """
    Sprawdza czy dzień jest roboczy w PL.
    Dniem roboczym jest pon-pt bez świąt ustawowych.
    Od 2025-01-01 Wigilia (12-24) jest wolna.
    """
    d = _to_ymd(d)
    year = int(datetime.strptime(d, '%Y-%m-%d').strftime('%Y'))

    # obliczenie Wielkanocy (prosty computus jak w oryginale)
    easter_calc = (2*(year % 4) + 4*(year % 7) + 6*(((year % 19)*19 + 24) % 30) + 5) % 7 + (((year % 19)*19 + 24) % 30)
    easter_dt = datetime.strptime(f'{year}-03-22', '%Y-%m-%d') + timedelta(easter_calc)
    easter = easter_dt.strftime('%Y-%m-%d')
    wet = (easter_dt + timedelta(days=1)).strftime('%Y-%m-%d')           # Poniedziałek Wielkanocny
    cialo = (easter_dt + timedelta(days=60)).strftime('%Y-%m-%d')        # Boże Ciało

    holidays = {
        f'{year}-01-01',  # Nowy Rok
        f'{year}-01-06',  # Trzech Króli
        easter,           # Wielkanoc
        wet,              # Poniedziałek Wielkanocny
        f'{year}-05-01',  # Święto Pracy
        f'{year}-05-03',  # Święto Konstytucji 3 Maja
        cialo,            # Boże Ciało
        f'{year}-08-15',  # Wniebowzięcie NMP
        f'{year}-11-01',  # Wszystkich Świętych
        f'{year}-11-11',  # Narodowe Święto Niepodległości
        f'{year}-12-25',  # Boże Narodzenie (pierwszy dzień)
        f'{year}-12-26',  # drugi dzień BN
    }

    # Wigilia wolna od 2025
    if year >= 2025:
        holidays.add(f'{year}-12-24')

    weekday = datetime.strptime(d, '%Y-%m-%d').weekday()  # 0=pon, 6=nd
    if weekday in (5, 6):  # sob, nd
        return False
    return d not in holidays

def lastBD(d='today'):
    """
    Zwraca poprzedni dzień roboczy względem d.
    """
    d = _to_ymd(d)
    i = 1
    while True:
        prev = (datetime.strptime(d, '%Y-%m-%d') - timedelta(days=i)).strftime('%Y-%m-%d')
        if isBusinessDay(prev):
            return prev
        i += 1

def nextBD(d='today'):
    """
    Zwraca następny dzień roboczy względem d.
    """
    d = _to_ymd(d)
    i = 1
    while True:
        nxt = (datetime.strptime(d, '%Y-%m-%d') + timedelta(days=i)).strftime('%Y-%m-%d')
        if isBusinessDay(nxt):
            return nxt
        i += 1

def BDays_list(start_date, end_date):
    """
    Zwraca listę [data, bool] dla zakresu od start_date do end_date włącznie.
    """
    def daterange(a, b):
        for n in range(int((b - a).days) + 1):
            yield a + timedelta(n)

    out = []
    a = datetime.strptime(_to_ymd(start_date), '%Y-%m-%d')
    b = datetime.strptime(_to_ymd(end_date), '%Y-%m-%d')
    for day in daterange(a, b):
        ds = day.strftime('%Y-%m-%d')
        out.append([ds, isBusinessDay(ds)])
    return out
