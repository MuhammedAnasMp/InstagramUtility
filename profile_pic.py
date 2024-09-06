from instagrapi import Client 
cl = Client()
#enter your username and password
cl.login('eudusj372', '15036*Kk')
#you can replace 10 with whatever amount of reels you want to fetch
reel = cl.explore_reels(amount = 10)
print(reel)


log=cl.account_change_picture(path='aa.JPG')
print(log)


