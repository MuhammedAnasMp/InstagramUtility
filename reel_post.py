
import re
import os,time,json

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

media_id = cl.media_id(cl.media_pk_from_url('https://www.instagram.com/p/C_iAuYaJOO4/'))
media_info = cl.media_info(media_id).dict()
print(media_info)