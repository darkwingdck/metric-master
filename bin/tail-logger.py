#!/usr/bin/python3
import time
import os

def follow(the_file):
    the_file.seek(0, os.SEEK_END)
    while 1:
        line = the_file.readline()

        if not line:
            time.sleep(0.1)
            continue
        yield line

if __name__ == '__main__':
    logfile = open('/var/log/lighttpd/access.log', 'r')
    loglines = follow(logfile)
    for line in loglines:
        print(line)
