import urllib
import time
y=1
z=0

while True:
    x=1
    if z:
        w=18000
        while w > 0:
            print "waiting %s seconds" %w
            time.sleep(1000)
            w = w-1000
    while x <= 10:
        while True:
            try:
                urllib.urlretrieve("http://www.goes.noaa.gov/GSSLOOPS/ecir/"+str(x)+".jpg",str(y)+".jpg")
            except Exception:
                time.sleep(1)
                continue
            break
        x += 1
        y += 1
        z=1
