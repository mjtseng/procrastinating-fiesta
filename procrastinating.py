
# Procrastinating Fiesta:
# are you procrastinating?


# FUNCTION DEFINITIONS

def start():
	if(input("To start, hit <space>.") == " "):
		return "ready"

# u sure you want to use bools for notworking() ?
def notworking():
	# should you take notworking_var out of the function and use it as an argument? ::thinking emoji::
	notworking_var = input("Are you procrastinating? Type your answer: 'True' or 'False' ")
	if (str(notworking_var) == "True"):
		return ("Shame on you. You have things to do. Sad!")
	elif (str(notworking_var) == "False"):
		return ("gfy... Are you lying? Because you (very likely) have work.") # "gfy" this is so passive aggressive haha
	# :)
	elif(str(notworking_var) == "42"):
		return ("I pity the fool that procrastinates... but good answer") # actually idk what I was thinking here
	elif(str(notworking_var) == "Geico could save you 15% or more on car insurance"):
		return ("Can't argue with that.")
	else:
		return ("Sorry, I didn't get that. (You're procrastinating right now, aren't you?)")
		# and/or, you can make a temporary variable to store the answer in, and then you can put it in the log later!

# END FUNCTION DEFINITIONS


# have the title string thing that will be printed when program starts in command line
	# u know the thing with stuff like license and year, version and stuff like that
print("Welcome to Procrastinating Fiesta! Currently running v 0.1.\nType info() for more info, license() to see the license, or exit() to quit.")
	# neither info(), license(), nor exit() currently exist
	# running the command "ipython" gives this (I have Anaconda). Note that the results of these tell you to go to a website
	# "q" gives you a quick tutorial kinda thing
'''
		Python 3.6.5 |Anaconda custom (64-bit)| (default, Mar 29 2018, 13:32:41) [MSC v.1900 64 bit (AMD64)]
		Type 'copyright', 'credits' or 'license' for more information
		IPython 6.3.1 -- An enhanced Interactive Python. Type '?' for help.
'''

# CALL FUNCTIONS

# print current results
print(notworking())

# LOG CODE:

# create initial, empty log: list or something else mutable.
# question: Can I have persistent memory for something like this? Or will it disappear when ending the program?
	# If it can be kept indefinitely then maybe I can make a file and access it

'''
def add_entry():
	# function to add an entry to the log
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
	# exit whole program - use same quit function as titlestring will
	exit()

'''

# TODOS and NOTES:
# try to optimize code - there has to be a better way to do this
# create functions
# update titlestring and license things

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
- info() is used to display more info about the project: the author, last update (May 2018), etc.
- license() displays the license
- exit() is used to quit and close the program. (look to see if there's a built-in Python function for this)

'''