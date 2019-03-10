#!/usr/bin/env python
# play a sound at random intervals

import time
import random
import os
import shutil
# when debug is set to true we speed up the wait and get some
# additional helpful output
debug = False
d = "/home/pi/sounds/sneaze/"
t = "/home/pi/sounds/temp/"
i = "/home/pi/sounds/interim/"

while True:
    # pick a random number and wait
	N = random.randrange(60, 5400) # at least once in 1.5 hrs
    # if debug is set we just wait 5 seconds
	if debug:
		N = 5
    # we wait
	time.sleep(N)
    # if either of the following files exist no sound is played
	m = os.path.exists("/home/pi/muted")
	r = os.path.exists("/home/pi/radio_is_on")
	if m == False and r == False:
        # we pick a random file from directory d
		f = random.choice(os.listdir(d))
        # we add the path
		s = d + f
        # if debug is set we print path and file name
		if debug:
			print("s: " + s)
        # constructing the shell command
		cmd = "aplay -q " + s
        # executing the shell command
		os.system(cmd)
        # debug output
		if debug:
		   	print("Played " + f + " after " + str(N) + " seconds.")
        # since we do not want hear the same sound twice in a row
        # we move the file out of the directory and into the temp directory
		shutil.move(s, t + f)
        # if the original directory is empty ...
		if os.listdir(d) == []:
            # the interim directory gets deleted if it exist
			shutil.rmtree(i,ignore_errors=True)
            # the temp directory gets renamed to interim
			shutil.move(t, i)
            # the (empty) original directory gets renamed to temp
			shutil.move(d, t)
            # the interim directory becomes the original
			shutil.move(i, d)
	else:   # if a stop files exist, we skip 
		if debug:
			print("Didn't get to sneaze after " + str(N) + " seconds.")
	pass # we start over with a random wait time

