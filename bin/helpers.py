import arrow
import datetime as dt


def datetime_from_log(log: str):
  datetime_string = log.split(' ')[7].replace('[', '')
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
