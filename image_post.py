
import time
import os
from PIL import Image
from datetime import datetime
from instagrapi import Client
from instagrapi.exceptions import LoginRequired
from instagrapi.types import Usertag, Location ,UserShort
cl = Client()

USERNAME = 'kerala_partner_finder_bot'
PASSWORD = '15036*Kk'
SESSION_FILE = os.path.join(os.getcwd(), 'session.json')
if os.path.exists(SESSION_FILE):
    cl.load_settings(SESSION_FILE)  # Load session from the file if it exists
    try:
        cl.get_timeline_feed()  # Verify if the session is still valid
        print("Session loaded successfully!")
    except Exception as e:
        print("Session invalid, logging in again.")
        cl.login(USERNAME, PASSWORD)
        cl.dump_settings(SESSION_FILE)  # Save new session data to the file
else:
    # Login and save session
    cl.login(USERNAME, PASSWORD)
    cl.dump_settings(SESSION_FILE)  # Create the session file in the current directory
    print("Logged in and session saved!")

user_full = cl.user_info_by_username('mr_jorthan')
user_short = UserShort(
    pk=user_full.pk,
    username=user_full.username,
    full_name=user_full.full_name,
    profile_pic_url=user_full.profile_pic_url,
)
image_path = './11.JPG'
rotated_image_path = "./11_rotated.JPG"

with Image.open(image_path) as img:
    rotated_img = img.rotate(270, expand=True)  # Rotate the image 90 degrees
    rotated_img.save(rotated_image_path)  # Save the rotated image



media = cl.photo_upload(
    rotated_image_path,  # Path to your image file
    "Test caption for photo with #hashtags and mention users such @mr_jorthan",  # Caption for the post
    usertags=[Usertag(user=user_short, x=0.5, y=0.5)],  # Tagging a user at the center of the image
    location=Location(name='Russia, Saint-Petersburg', lat=59.96, lng=30.29)  # Location details
)

# Output the details of the uploaded media
print(media.dict())