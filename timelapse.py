from picamera import PiCamera
from time import sleep

camera = PiCamera()

camera.resolution = (1920, 1080)
camera.start_preview()
i = 0

for i in range(40000):
    sleep(5)    
    camera.capture('/home/pi/Pictures/timelapse/image_%s.jpg' % i)
camera.stop_preview()