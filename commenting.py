# from instagrapi import Client 
# cl = Client()
# #enter your username and password
# cl.login('eudusj372', '15036*Kk')
# #you can replace 10 with whatever amount of reels you want to fetch
# reel = cl.explore_reels(amount = 10)
# print(reel)


# log=cl.account_change_picture(path='aa.JPG')
# print(log)



import time
from datetime import datetime
from instagrapi import Client
from instagrapi.exceptions import LoginRequired
def tm(time):
    return datetime.fromtimestamp(time).strftime('%Y-%m-%d %H:%M:%S')

# Login to Instagram
cl = Client()
cl.login('kaattu_kozhi_', '15036*Kk')

# Get the media ID from the reel URL
media_id = cl.media_id(cl.media_pk_from_url('https://www.instagram.com/p/Cqm4MeRgHkI/'))
print("Taking meadia" ,tm)

# Post a comment on the reel
i = 0
while True:
    i += 1
    try:
        comment = cl.media_comment(media_id, f"POST Comment {i}")
        print(F"Posted Comment {i}")
        time.sleep(15)  # Wait for 14 seconds between comments
    except LoginRequired:
        print("Session expired. Logging in again...")
        cl.login('kaattu_kozhi_', '15036*Kk')

