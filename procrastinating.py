# are you procrastinating?
notworking = input("Are you procrastinating? Type 'True' or 'False' ")
# likely answers
if (str(notworking) == "True"):
	print ("Shame on you. You have things to do. Sad!")
elif (str(notworking) == "False"):
	print ("gfy... Are you lying? Because you (very likely) have work.")
# easter eggs
elif(str(notworking) == "42"):
	print ("I pity the fool that procrastinates... but good answer")
elif(str(notworking) == "Geico could save you 15% or more on car insurance"):
	print ("Can't argue with that.")
else:
	print ("Sorry, I didn't get that. (You're procrastinating right now, aren't you?)")

#TODO: make this into something useful or at least more entertaining