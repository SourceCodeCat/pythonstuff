import sys

def anagramCheck(s1,s2):
	s1_l = list(s1)
	s2_l = list(s2)
	
	s1_l.sort()
	s2_l.sort()

	
	if s1_l == s2_l:
		return True
	else:
		return False


print "Argument List: %s" % (sys.argv)
a1=sys.argv[1]
a2=sys.argv[2]
print a1
print a2
print "%s is an anagram of %s?...%s" % (a1,a2,anagramCheck(a1,a2))
