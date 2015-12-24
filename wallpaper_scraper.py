#!/usr/bin/env python3
import os
import praw
import re
from math import gcd
import random
import requests

### SETTINGS ###
subreddit = "wallpapers"
allowed_resolutions = ["1920x1080"]
allowed_extentions = ["png", "jpg",]
filename="wallpaper"
directory=os.path.expanduser("~/.wallpapers/")
### END SETTINGS ###

version='1.1'

#Converts strings of type "WIDTHxHEIGHT" to ratios (eg 16:9)
def ratio_for(string):
    numbers = string.split("x")
    x = float(numbers[0])
    y = float(numbers[1])
    r = gcd(int(x),int(y))
    return str(int(x/r)) + ":" + str(int(y/r))

#Calculate allowed ratio's
allowed_ratios = [ratio_for(x) for x in allowed_resolutions]

r = praw.Reddit(user_agent='wallpaper/' + version + ' by tvgdb')
success = False
i = 0
matches = []
while not success:
    i += 100
    submissions = r.get_subreddit(subreddit).get_hot(limit=i)
    for s in submissions:
        m = re.search('\[[0-9]+x[0-9]+\]',s.title)
        if m:
            res = m.group(0).strip("[").strip("]")
            rat = ratio_for(res)
            extention = s.url[-3:]
            if rat in allowed_ratios and extention in allowed_extentions:
                matches.append(s)
                success = True

#Pick a random wallpaper from the matches
s = random.choice(matches)
extention = s.url[-3:]
with open(directory + filename + "." + extention,'wb') as f:
    r = requests.get(s.url)
    f.write(r.content)

print(directory + filename + "." + extention)
