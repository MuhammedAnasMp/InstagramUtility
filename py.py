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
def tm(time):
    return datetime.fromtimestamp(time).strftime('%Y-%m-%d %H:%M:%S')

# Login to Instagram
cl = Client()
cl.login('kaattu_kozhi_', '15036*Kk')

# Get the media ID from the reel URL
media_id = cl.media_id(cl.media_pk_from_url('https://www.instagram.com/p/C_BC2ckSqNL/'))
print("Taking meadia" ,tm)

# Post a comment on the reel
for i in range(1,500):
    for k in range(1,10):
        comment = cl.media_comment(media_id, f"testing{i}")
        time.sleep(10)
        print("POST Comment" ,tm)
        # print(comment.dict())
    print("Sleeping")
    time.sleep(100)
