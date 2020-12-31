# Raspberry Camera
Author: Rob Lisy

I'd like to setup a Raspberry Pi with a high quality camera, have it take a series of pictures around sunrise/sunset, 
and have those pictures uploaded to my AWS account. Potentially I'd like to process them together into a video. 

We'll see.

## Setup:
I like to get the following pieces of software on a clean Raspberry Pi:

- Python 3.7.3
- [A static IP](https://www.ionos.com/digitalguide/server/configuration/provide-raspberry-pi-with-a-static-ip-address/#:~:text=To%20assign%20an%20IP%20address,with%20the%20IPv4%20address%20192.168.) makes it easier to SSH into multiple times

Then the usual:

```
sudo apt update
# Python and camera software
sudo apt install python3-picamera
sudo apt install python3-pip

# Project directory
git clone 

pip3 install awscli --upgrade --user
export PATH=/home/pi/.local/bin:$PATH
```

The not so usual:
- Setup AWS credentials 

Files:
- `.gitignore` <- ignore file for code versioning 
- `config.yml` <- configuration info
- `live_stream.py` <- broadcast video stream to http location. Used for focus/setup of the camera.
- `take_pictures.py` <- main script which takes pictures
- `util.py` <- helper functions for `take_pictures.py`

There's an `img` folder for storing the image files taken by `take_pictures.py`.