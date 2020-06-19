from picamera import PiCamera
from time import sleep

camera = PiCamera()

camera.resolution = (1920, 1080)
camera.start_preview()

for i in range(1,40000):
    sleep(10)    
    camera.capture('/home/pi/Pictures/lego-timelapse/image_%s.jpg' % i)
camera.stop_preview()
