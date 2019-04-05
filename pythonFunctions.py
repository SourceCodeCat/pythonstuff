import sys
def greeting(language):
	if language == 'eng':
		return "Hello World"
	elif language == 'fr':
		return "Bonjour le mond"
	else:
		return "language not supported"


def greetingAgain(language):
	if language == 'eng':
		return "Hello World, my friend!"
	elif language == 'fr':
		return "Bonjour le mond, mon amie!!"
	else:
		return "language not supported, dude!"



def callf(f,param):
	return f(param)

print "passing as paramter the language and the name of function 'greeting': %s" % callf(greeting,sys.argv[1])
print "passing as paramter the language and the name of function 'greetingAgain': %s    " % callf(greetingAgain,sys.argv[1])
