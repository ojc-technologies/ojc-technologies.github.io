import time
import urllib.request
import re

def follow(thefile):
    thefile.seek(0,2)
    while True:
        line = thefile.readline()
        if not line:
            time.sleep(0.1)
            continue
        yield line


def process(line):
    if re.match( r'.+DHCPREQUEST.+ac:63:be:7f:29:47', line):
        print("Processed Dash button press")
        urllib.request.urlopen("http://192.168.1.100:1880/dash-button")


if __name__ == '__main__':
    logfile = open("/var/log/syslog","r")
    loglines = follow(logfile)
    for line in loglines:
        process(line)
