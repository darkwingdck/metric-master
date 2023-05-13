#!/usr/bin/python3
import sqlite3 as sl
import config
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
        'timestamp': splitted_log[7].replace('[', ''),
        'time_used_in_ms': splitted_log[9].replace('\n', '')
    }


def process_logline(line):
    if line == '\n':
        return
    deserialized_line = deserialize_line(line)
    return deserialized_line

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

def datetime_from_log(log: str):
    datetime_string = log.split(' ')[7].replace('[', '')
    date_string = datetime_string.split(':')[0]
    time_string = datetime_string.split(f'{dt.date.today().year}:')[1]

    arrow_date = arrow.get(date_string, 'D/MMM/YYYY').format('YYYY M DD')

    date = dt.datetime(int(arrow_date.split(' ')[0]), int(arrow_date.split(' ')[1]), int(arrow_date.split(' ')[2]))


    hours = int(time_string.split(':')[0])
    minutes = int(time_string.split(':')[1])
    seconds = int(time_string.split(':')[2])
    time = dt.time(hours, minutes, seconds)
    return dt.datetime.combine(date, time)

def new_logs_appeared(filename: str):
    [first_line, last_line] = read_last_and_first_line(filename)
    first_datetime = datetime_from_log(first_line)
    last_datetime = datetime_from_log(last_line)
    diff = last_datetime - first_datetime
    return diff.seconds > config.cooldown_in_seconds

def main():
    if not new_logs_appeared(config.accesslog_filename):
        print('200 OK')
        return

    result_logs = []
    logfile = open(config.accesslog_filename, 'r')
    processed_logs_file = open(config.processed_logs_filename, 'a')

    loglines = logfile.readlines()
    processed_logs_file.write('\n')
    for line in loglines:
        processed_logs_file.write(line)
        processed_logline = process_logline(line)
        result_logs.append(processed_logline)

    result = { 'logs': result_logs }
    print("Content-type: application/json")
    print()
    print(dumps(result))

    logfile = open(config.accesslog_filename, 'w')
    logfile.write('')


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(e)
