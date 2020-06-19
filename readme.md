0. Install Thonny Python IDE ```sudo apt-get install thonny```

1. Enable camera

2. install picamera library for Python 3 ```sudo apt-get install python3-picamera```

# Other notes

## Setting up remote desktop control (VNC)
1. Enable vnc on the RPi
2. Install tightvnc on the host RPi ```sudo apt-get install tightvncserver``` 
3. On host RPi, run command ```vncserver```, follow prompts to set up a password (6-8 characters)

## Controlling remotely
1. In Remmina, Create a new connection profile for type VNC
  - Enter the IP address of the RPi, along with the vnc instance number. e.g. ```192.168.0.143:1```
  - Enable SSH tunneling
2. Connect and enjoy!

## Code to stitch images to a video:
```ffmpeg -r 24 -s 1920x1080 -start_number 1 -i image_%d.jpg -vcodec libx264 -crf 25 lucy-lego.mp4```
