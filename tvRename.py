#!/usr/local/bin/python3
import os
import sys

#also promt user for file extension ex .mkv, .mp4 etc.

if len(sys.argv) != 2:
	print("Usage:")
	print("	$ tvRename [Exact name of TV show inside /mnt/main/plexmediafiles/TvShows/]")
	#print("         Example: $ tvRename MrRobot .mkv\n")
	print("         Example: $ tvRename MrRobot")
	exit()

TVSHOWS_PATH="/mnt/main/plexmediafiles/TvShows/"
os.chdir(TVSHOWS_PATH)
TVSHOWS = os.listdir() # get list of all Tv Shows
SHOW = sys.argv[1] # Store in variable

if SHOW not in TVSHOWS:
	print("No tv show called "+SHOW)
	exit()

#EXT = sys.argv[2]
#assume that season 1 at index 1,2 ...  etc

# Change directory to SHOW
show_dir = TVSHOWS_PATH+SHOW
os.chdir(show_dir)


seasons = os.listdir()
seasons.sort()

"""
episodes = {}
for season in seasons:
	os.chdir(season)
	temp_eps = os.listdir()
	temp_eps.sort()
	episodes[season] = temp_eps
	os.chdir(show_dir)
"""


x = 1
for season in seasons:
	#y = int(os.listdir()[0][-1])
	os.chdir(season)
	eps_list = os.listdir()
	eps_list.sort()

	y = 1
	for eps in eps_list:
		if eps == "subtitles" or eps == "Subtitles":
			continue
		ext = eps[-3:]

		if x < 10 and y < 10:
			os.rename(eps, "S0"+str(x)+"E0"+str(y)+"."+ext)
		elif x < 10:
			os.rename(eps, "S0"+str(x)+"E"+str(y)+"."+ext)
		elif y < 10:
			os.rename(eps, "S"+str(x)+"E0"+str(y)+"."+ext)
		else:
			os.rename(eps, "S"+str(x)+"E"+str(y)+"."+ext)
		print("Renaming "+eps+" to "+"S"+str(x)+"E"+str(y)+"."+ext)
		y += 1
	os.chdir(show_dir)
	x += 1

"""
ep_name = "SxEy"
TODO clean the 10+ to appear in correct position in list
TODO account for other files in the directory such as subtitles folders or files
x = 1
y = 1
dont run this, for some reason it only renames 1 ep and removes the rest
accidentally deleted silicon valley
for season in seasons:
	s += 1
	os.chdir(show_dir + "/" + season) 
	for ep in episodes[season]:
		e += 1
		ep_name.replace("x",str(s))
		ep_name.replace("y", str(e))
		os.rename(ep, ep_name + ext)
	os.chdir(show_dir)
"""
