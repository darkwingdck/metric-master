import arrow
import datetime as dt
import sys


def datetime_from_log(log: str):
  datetime_string = log.replace('[', '')
  date_string = datetime_string.split(':')[0]
  time_string = datetime_string.split(f'{dt.date.today().year}:')[1]

  arrow_date = arrow.get(date_string, 'D/MMM/YYYY').format('YYYY M DD')

  date = dt.datetime(int(arrow_date.split(' ')[0]), int(
      arrow_date.split(' ')[1]), int(arrow_date.split(' ')[2]))

  hours = int(time_string.split(':')[0])
  minutes = int(time_string.split(':')[1])
  seconds = int(time_string.split(':')[2])
  time = dt.time(hours, minutes, seconds)
  return dt.datetime.combine(date, time)


def log(data):
  original_stdout = sys.stdout
  with open('data_log.txt', 'a') as f:
    sys.stdout = f
    print('\n')
    print(dt.datetime.now().strftime("%m.%d.%Y, %H:%M:%S"))
    print(data)
    sys.stdout = original_stdout
