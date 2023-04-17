#!/usr/bin/python3
import sqlite3 as sl
import time
import os
import config

def get_log_lines(the_file):
    the_file.seek(0, os.SEEK_END)
    while 1:
        line = the_file.readline()
        if not line:
            time.sleep(0.1)
            continue
        yield line

def deserialize_log(log):
    # TODO: custom lighttpd configs require custom deserialization
    splitted_log = log.split(' ')
    return {
        'user_ip': splitted_log[0],
        'host': splitted_log[1],
        'method': splitted_log[3],
        'status': splitted_log[4],
        'path': splitted_log[5],
        'body_length': splitted_log[6],
        'timestamp': splitted_log[7],
        'time': splitted_log[9]
    }

def write_log_in_database(log):
    if log == '\n':
        return
    deserialized_log = deserialize_log(log)
    print(deserialized_log)


if __name__ == '__main__':
    logfile = open(config.accesslog_filename, 'r')
    loglines = get_log_lines(logfile)
    for line in loglines:
        write_log_in_database(line)
