#!/usr/bin/python3
import sqlite3 as sl
import config
from json import dumps


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

def main():
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
