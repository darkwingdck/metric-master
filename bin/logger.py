#!/usr/bin/python3
import config
import helpers

from json import dumps
import arrow
import datetime as dt


def deserialize_line(log):
  # TODO: custom lighttpd configs require custom deserialization
  splitted_log = log.split(' ')
  return {
      'user_ip': splitted_log[0],
      'host': splitted_log[1],
      'method': splitted_log[3],
      'status': splitted_log[4],
      'path': splitted_log[5],
      'body_length': splitted_log[6],
      'timestamp': helpers.datetime_from_log(log).strftime("%H:%M:%S"),
      'time_used_in_ms': splitted_log[9].replace('\n', '')
  }


def process_logline(line):
  if line == '\n':
    return
  return deserialize_line(line)


def read_last_and_first_line(filename: str):
  first_line = ''
  last_line = ''
  index = 0
  with open(filename) as f:
    for line in f:
      if line != '\n':
        if index == 0:
          first_line = line
        index += 1
        last_line = line
  return [first_line, last_line]


def new_logs_appeared(filename: str):
  [first_line, last_line] = read_last_and_first_line(filename)
  first_datetime = helpers.datetime_from_log(first_line)
  last_datetime = helpers.datetime_from_log(last_line)
  diff = last_datetime - first_datetime
  return diff.seconds > config.cooldown_time_in_seconds


def main():
  result_logs = []
  logfile = open(config.accesslog_filename)
  
  current_interval_array = []
  current_interval_end = dt.datetime.now()
  for i, log in enumerate(reversed(list(logfile))):
    current_log_datetime = helpers.datetime_from_log(log)
    if len(current_interval_array) == 0:
      current_interval_array.append(process_logline(log))
      current_interval_end = current_log_datetime
    elif i != 0 and (current_interval_end - current_log_datetime).seconds > config.cooldown_time_in_seconds:
      current_interval_array.append(process_logline(log))
      result_logs.append(list(reversed(current_interval_array)))
      current_interval_array = []
    else:
      current_interval_array.append(process_logline(log))
      if len(result_logs) > 10:
        break

  result = {'logs': list(reversed(result_logs))}
  print("Content-type: application/json")
  print()
  print(dumps(result))


if __name__ == '__main__':
  try:
    main()
  except Exception as e:
    print(e)
