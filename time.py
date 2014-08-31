import sys
import time

for i in range(10001):

    percent = 1.0 * i / 10000 * 100
    sys.stdout.write("\r")
    print 'complete percent:' + str(percent) + '%',
    time.sleep(0.01)
