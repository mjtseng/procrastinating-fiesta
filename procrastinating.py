
# Procrastinating Fiesta:
# are you procrastinating?


# -------- FUNCTION DEFINITIONS --------------------------------

# the way all of these work actually makes no sense to me but it kinda works?? keeping it, will fix later
def get_start_info():
	''' this determines what happens at the beginning of the program '''
	first_input = input("Type info for more info, license to see the license, or exit to quit.")
	if (first_input == "info"):
		return "hello! here's a placeholder for info"
	elif (first_input == "license"):
		return "hello! the license will be here shortly. Thanks for your patience! (planning to use the Mozilla copyleft thing)"
	elif (first_input == "exit"):
		return "Sorry to see you go!"

def start():
	''' when the user presses <start> and <enter>, the program returns what is used as the start signal, "ready". '''
	# actually I don't know why you need to press <enter> too. TODO: research
	arewethereyet = input("To start, hit <space>, then <enter>.")
	if (arewethereyet == " "):
		return "ready"
	else:
		print(get_start_info())

# u sure you want to use bools for notworking() ? You can use some of Python's built-in functions to handle cases, etc.
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

# -------- THINGS START HAPPENING --------------------------------

# have the title string thing that will be printed when program starts in command line
	# u know the thing with stuff like license and year, version and stuff like that
print("\nWelcome to Procrastinating Fiesta! Currently running v 0.1.0")
	# running the command "ipython" gives this (I have Anaconda). Note that the results of these tell you to go to a website
	# "q" gives you a quick tutorial kinda thing
'''
		Python 3.6.5 |Anaconda custom (64-bit)| (default, Mar 29 2018, 13:32:41) [MSC v.1900 64 bit (AMD64)]
		Type 'copyright', 'credits' or 'license' for more information
		IPython 6.3.1 -- An enhanced Interactive Python. Type '?' for help.
'''

# if user wants to start, print current results
print(get_start_info())
if (start() == "ready"):
	print(notworking())

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
# understand functions; attempt to organize them so they make sense
	# explain EVERYTHING to a rubber duck
		# find a nice rubber duck
	# to be fixed: after typing in "info"/"license"/"exit" it works, then prompts you to press <start> and <enter>, but you can still type "info"/"license"/"exit".
		# after doing that, it prints "Type info for info, license for the license", etc. and it works
		# then, the program ends

# to be implemented:
# it would be cool if there was a log of some sort, of how often you were/weren't procrastinating.
# maybe have an array to keep track of dates as well? (the day and a list of that day's results?) idk really
	# ok so having days sounds hard and I'm going to focus on a list of results for now (as of 5/9/18)
# this will be far in the future but what about a GUI? A command-line thing is very meh in terms of aesthetics

# -------- MASTER LIST OF ALL FUNCTIONS because I can't keep track of them and what they do: --------------------------------
'''
- notworking() is used to take the user's initial input of whether they are procrastinating at the moment.
- add_entry() is used to put the user's entry into the log if they opt to do so.
- clear_log() is used to delete all entries from the log and allow the user to put their new input into a newly blank log.
	- should it be clearlog and add entry, or just clear log without adding an entry? Maybe I can put an option here.
- info() is used to display more info about the project: the author, last update (May 2018), etc.
- license() displays the license
- exit() is used to quit and close the program. (look to see if there's a built-in Python function for this)

'''