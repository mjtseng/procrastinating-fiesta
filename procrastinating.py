
# Procrastinating Fiesta:
# are you procrastinating?


# -------- FUNCTION DEFINITIONS --------------------------------

# u sure you want to use bools for notworking() ? You can use some of Python's built-in functions to handle cases, etc.
def notworking():
	# should you take notworking_var out of the function and use it as an argument? ::thinking emoji::
	notworking_var = input("Are you procrastinating? Type your answer: 'True' or 'False' ")
	if (str(notworking_var) == "True"):
		return ("Shame on you. You have things to do. Sad!")
	elif (str(notworking_var) == "False"):
		return ("gfy... Are you lying? Because you (very likely) have work.")
	# :)
	elif(str(notworking_var) == "42"):
		return ("I pity the fool that procrastinates... but good answer") # actually idk what I was thinking here
	elif(str(notworking_var) == "Geico could save you 15% or more on car insurance"):
		return ("Can't argue with that.")
	else:
		return ("Sorry, I didn't get that. (You're procrastinating right now, aren't you?)")
		# and/or, you can make a temporary variable to store the answer in, and then you can put it in the log later!

def test_start():
	'''This is a test. Hopefully, this will be used to take *any* input from the user and return the correct thing.'''
	user_intent = input("\nWelcome to Procrastinating Fiesta! Currently running v 0.1.1\nType info for more info, license to see the license, or exit to quit.\nTo start, hit <space>, then <enter>.")
	if (user_intent == "info"):
		return "hello! here's a placeholder for info"
	elif (user_intent == "license"):
		return "hello! the license will be here shortly. Thanks for your patience! (planning to use the Mozilla copyleft thing)"
	elif (user_intent == "exit"):
		return "Sorry to see you go!"
	elif (user_intent == " "):
		return notworking()

# -------- THINGS START HAPPENING --------------------------------

print(test_start())

# -------- LOG CODE: --------------------------------

# create initial, empty log: list or something else mutable.
# question: Can I have persistent memory for something like this? Or will it disappear when ending the program?
	# Maybe I can make a file and access it; then you can export to a spreadsheet and stuff like that

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

# -------- TODOS and NOTES: --------------------------------
# try to optimize code - there has to be a better way to do this
# update titlestring and license things
# figure out how to version this (looks like there are multiple ways to do this... ugh)

# to be implemented:
# it would be cool if there was a log of some sort, of how often you were/weren't procrastinating.
# maybe have an array to keep track of dates as well? (the day and a list of that day's results?) idk really
	# ok so having days sounds hard and I'm going to focus on a list of results for now (as of 5/9/18)
# this will be far in the future but what about a GUI? A command-line thing is very meh in terms of aesthetics

# -------- MASTER LIST OF ALL FUNCTIONS because I can't keep track of them and what they do: --------------------------------
'''
- notworking() is used to take the user's initial input of whether they are procrastinating at the moment.
- add_entry() will be used to put the user's entry into the log if they opt to do so.
- clear_log() will be used to delete all entries from the log and allow the user to put their new input into a newly blank log.
	- should it be clearlog and add entry, or just clear log without adding an entry? Maybe I can put an option here.
- info() is used to display more info about the project: the author, last update (May 2018), etc.
- license() displays the license
- exit() is used to quit and close the program. (look to see if there's a built-in Python function for this)

'''