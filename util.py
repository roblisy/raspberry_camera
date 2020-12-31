# Utility functions for taking pictures around sunrise / sunset
import astral
from astral.sun import sun
import datetime
import yaml
from picamera import PiCamera
from time import sleep

camera = PiCamera()

def load_config(yaml_file: str):
    """ Helper function to load config info.
    :param yaml_file: location of the configuration file.
    :return: config parameters
    """
    # load config options from yaml.
    with open(yaml_file) as f:
        config = yaml.safe_load(f)
    return config


def get_sunset_sunrise(loc: astral.LocationInfo,
                       dt: datetime):
    """
    Function to get the sunrise and sunset at a location
    :param loc: location to determine the sunrise / sunset
    :param dt: date to determine the sunrise / sunset for
    :return:
    """
    l = sun(loc.observer, date=dt, tzinfo=loc.timezone)
    return l["sunrise"], l["sunset"]


def take_picture(folder: str,
                 file_pattern: str,
                 sleep_sec: int,
                 x_resolution: int,
                 y_resolution: int):
    """
    Take a picture, store it using a given resolution in a folder and file.
    :param x_resolution: X resolution for the image
    :param y_resolution: Y resolution for the image
    :param folder: file system location for storing the picture.
    :param file_pattern: file name pattern for saving..
    :param sleep_sec: number of seconds to sleep before the next picture... should be at LEAST 2.
    :return:
    """

    camera.start_preview()
    camera.resolution = (x_resolution, y_resolution)
    camera.capture(f"""{folder}/{file_pattern}.jpg""")
    camera.stop_preview()
    sleep(sleep_sec)

