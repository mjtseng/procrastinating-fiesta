
# Procrastinating Fiesta:
# are you procrastinating?

# call functions here

# some function definitions
# u sure you want to use bools?
# o crap I can't remember the syntax to define functions. lol this is pathetic, guess I don't know Python after all
def notworking:
	notworking_var = input("Are you procrastinating? Type your answer: 'True' or 'False' ")
	if (str(notworking_var) == "True"):
		print ("Shame on you. You have things to do. Sad!")
	elif (str(notworking_var) == "False"):
		print ("gfy... Are you lying? Because you (very likely) have work.")
	# :)
	elif(str(notworking_var) == "42"):
		print ("I pity the fool that procrastinates... but good answer")
	elif(str(notworking_var) == "Geico could save you 15% or more on car insurance"):
		print ("Can't argue with that.")
	else:
		print ("Sorry, I didn't get that. (You're procrastinating right now, aren't you?)")
		# and/or, you can make a temporary variable to store the answer in, and then you can put it in the log later!

'''
LOG CODE:

# create log here: list or something else mutable.
log

# create function to add an entry to the log

def add_entry:
	wannalog = input("Do you want to log your answer for the future? (y/n)")
	if (wannalog == "y"):
		print("Logging...")
		# put result into records
		print("Logged!")
	else:
		print ("Response discarded.")
	print ("Press space to go again or x to exit! To clear your log, press c.")
# pseudocode, idk the syntax - hopefully this exists, and does this go in the function add_entry ?
if (space == pressed):
	# call notworking function again
	notworking()
elif (c == pressed):
	# clear entire log (will need another function for this?)
elif (x == pressed):
	# exit whole program

'''

# TODOS and NOTES:
# try to optimize code - there has to be a better way to do this

# to be implemented:
# it would be cool if there was a log of some sort, of how often you were/weren't procrastinating.
# maybe have an array to keep track of dates as well? (the day and a list of that day's results?) idk really
	# ok so having days sounds hard and I'm going to focus on a list of results for now (as of 5/9/18)
# this will be far in the future but what about a GUI? A command-line thing is very meh in terms of aesthetics

'''
MASTER LIST OF ALL FUNCTIONS because I can't keep track of them and what they do:

- notworking() is used to take the user's initial input of whether they are procrastinating at the moment.
- add_entry() is used to put the user's entry into the log if they opt to do so.
- clear_log() is used to delete all entries from the log and allow the user to put their new input into a newly blank log.
	- should it be clearlog and add entry, or just clear log without adding an entry? Maybe I can put an option here.

'''