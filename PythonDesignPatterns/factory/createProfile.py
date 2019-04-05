from profile import *

if __name__== '__main__':
	profile_type = input("Which Profile you'l like to create? [Linkedin or Facebook]")

	#v3.5
	#profile = eval(profile_type)()

	#v2.6
	# in python 2.x the input() already executes eval internally
	# according to this post https://stackoverflow.com/questions/17210057/must-eval-be-a-string-or-code-object
	profile = profile_type()


	print("Creating Profile..",type(profile).__name__)
	print("Profile has sections -- %",profile.getSections())
