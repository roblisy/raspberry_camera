# !/usr/bin/env python3
# Main script which
# - takes a picture


import time
import datetime
import yaml
import pytz
import astral
import boto3

# utility imports...
import util as u

# how long to sleep our loop for...
sleep_seconds: int = 30
# number of minutes before sunset to turn the lights on.

# turn off at this local time (11:30 pm)
off_at_hour_minute: datetime.time = datetime.time(21, 14)

# S3 connection
s3 = boto3.client('s3')

def main():
    # Load our configuration from yaml file...
    config = u.load_config(yaml_file='config.yml')
    # Create an astral location.
    location = astral.LocationInfo(
        name=config['astral_location']['name'],
        region=config['astral_location']['region'],
        timezone=config['astral_location']['tz'],
        latitude=float(config['astral_location']['latitude']),
        longitude=float(config['astral_location']['longitude']))

    while True:
        # what time is it now?
        now = pytz.timezone(config['astral_location']['tz']).localize(datetime.datetime.now())
        today = datetime.date.today()

        # get the sunrise...
        sunrise, sunset = u.get_sunset_sunrise(loc=location, dt=today)

        # make a string for saving any pictures...
        filestring = datetime.datetime.today().strftime('%Y_%m_%d_%H_%M_%S')

        print(f"now: {now}")
        print(f"sunset {sunset}")
        #
        # # if it's right before or after sunset, take a picture!
        # #if (now >= sunset - config['mins_before_sunset']) & (now <= sunset + config['mins_after_sunset']):
        if True:
            print('taking a picture')
            u.take_picture(folder=config['local_img_folder'],
                           file_pattern=filestring,
                           sleep_sec=5,
                           x_resolution=config['camera_res_x'],
                           y_resolution=config['camera_res_y'])

            # Save the file to an S3 location
            with open("FILE_NAME", "rb") as f:
                s3.upload_fileobj(f, "BUCKET_NAME", "OBJECT_NAME")

    # Example values...
    # now: 2020-10-30 04:26:02.658039 - 07: 00
    # sunset: 2020-10-30 17: 53:38.655055 - 07: 00

    # Things to do in a loop:
    # - check the time: is it close to sunrise/sunset?
    # - if it is, take a picture

    # print(config)
    # make a connection to our S3 bucket...
    # s3 = boto3.resource('s3')
    # s3.Bucket(config).upload_file('/local/file/here.txt', 'folder/sub/path/to/s3key')
    #


# Call the main function
if __name__ == "__main__":
    main()
