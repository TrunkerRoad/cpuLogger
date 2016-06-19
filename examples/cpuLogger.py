# coding=UTF-8
from time import localtime, strftime
# download from http://code.google.com/p/psutil/
import psutil
import time
from subprocess import PIPE, Popen

import thingspeak

channel_id = "123456" # Change to your Channel ID
write_key  = "TRUNKER_ROAD" # Change to your WRITE API KEY

def get_cpu_temperature():
    process = Popen(['vcgencmd', 'measure_temp'], stdout=PIPE)
    output, _error = process.communicate()
    return float(output[output.index('=') + 1:output.rindex("'")])

def doit(channel):

    cpuUsage = psutil.cpu_percent()
    cpuValue = get_cpu_temperature()

    try:
        response = channel.update({1: cpuUsage, 2: cpuValue})
        print cpuUsage
        print cpuValue
        print strftime("%a, %d %b %Y %H:%M:%S", localtime())
        print response
    except:
        print "connection failed"


#sleep for 16 seconds (api limit of 15 secs)
if __name__ == "__main__":
    channel = thingspeak.Channel(id=channel_id,write_key=write_key)
    while True:
        doit(channel)
        time.sleep(16)

