
# Procrastinating Fiesta:
# are you procrastinating?

# may want to make this into a function instead?
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

'''
LOG CODE:

# create log here: list or something else mutable.
wannalog = input("Do you want to log your answer for the future? (y/n)")
if (wannalog == "y"):
	print("Logging...")
	# put result into records
	print("Logged!")
else:
	print ("Response discarded.")
print ("Press space to go again or x to exit!")
# pseudocode, idk the syntax:
# if (space == pressed):
	# call notworking function again
# elif (x == pressed):
	# exit program

'''


#TODOS: 
# make this into something useful or at least more entertaining
# try to optimize code - there has to be a better way to do this

# it would be cool if there was a log of some sort, of how often you were/weren't procrastinating.
# maybe have an array to keep track of dates as well? (the day and a list of that day's results?) idk really