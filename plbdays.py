from datetime import timedelta, datetime, date

def isBussinesDay(date='today'):
  """
  Default: last business day of today

  Examples:

  isBussinesDay() or isBussinesDay('today')
  isBussinesDay('2021-11-12')

  """



  if date == 'today':
    date = datetime.today().strftime('%Y-%m-%d')

  year = int(datetime.strptime(date, '%Y-%m-%d').strftime("%Y"))
  easter_calc = (2*(year%4)+ 4*(year%7) + 6*((year%19*19+24)%30) +5)%7 + (year%19*19+24)%30

  easter = (datetime.strptime(str(year) + '-03-22', '%Y-%m-%d') + timedelta(easter_calc)).strftime("%d%m")
  wet = (datetime.strptime(str(year) + '-03-22', '%Y-%m-%d') + timedelta(easter_calc+1)).strftime("%d%m")
  cialo = (datetime.strptime(str(year) + '-03-22', '%Y-%m-%d') + timedelta(easter_calc+60)).strftime("%d%m")
  holidays =  ['0101','0601',easter,wet,'0105','0305',cialo,'1508','0111','1111','2512','2612']

  if datetime.strptime(date, '%Y-%m-%d').weekday() in (5,6) or datetime.strptime(date, '%Y-%m-%d').strftime("%d%m") in holidays:

    return(False)

  else: 

    return(True)


def lastBD(date='today'):
  if date == 'today':
    date = datetime.today().strftime('%Y-%m-%d')

  """
  Default: last business day of today

  Examples:

  lastBD() or lastBD('today') : print last business day of today
  lastBD('2021-11-12'): print 10th November, because 10th Novemver is a holiday


  """


  i=1
  bd=False
  while bd != True:
    if isBussinesDay((datetime.strptime(date, '%Y-%m-%d') - timedelta(i)).strftime("%Y-%m-%d")) == True:
      bd = True
      return((datetime.strptime(date, '%Y-%m-%d') - timedelta(i)).strftime("%Y-%m-%d"))

    else:
      i+=1

def BDays_list(start_date, end_date):

  """
  Example:
    start_date='2021-01-01'
    end_date='2021-12-31'
    
    BDays_list('2021-01-01', '2021-12-31')
    
  """

  def daterange(start_date, end_date):
    for n in range(int((end_date - start_date).days)):
      yield start_date + timedelta(n)

  list_=[]
  start_date = datetime.strptime(start_date, '%Y-%m-%d')
  end_date = datetime.strptime(end_date, '%Y-%m-%d')
  for single_date in daterange(start_date, end_date):
    df_list.append([single_date.strftime("%Y-%m-%d"), isBussinesDay(single_date.strftime("%Y-%m-%d"))])
  return list_
