from SingleLinkedList import *
from sys import *


def isPalindrome(node):

	reversedList = SingleLinkedList()
	current = node
	while current is not None:
		reversedList.appendNode(current.data,AppendMode.TOHEAD)
		current = current.next
	current = node
	currentReversed = reversedList.head
	isPalindrome_ = True
	reversedList.printLinkedList()
	while current is not None:
		if current.data != currentReversed.data:
			isPalindrome_ = False
		current = current.next
		currentReversed = currentReversed.next
	return isPalindrome_
	


if __name__ == "__main__":
	
	l = []

	if len(argv) > 1:
		l = [int(e) for e in argv[1].split(',')]
		#print l
	
	sll = SingleLinkedList(l)
	sll.printLinkedList()
	print "Is Palindrome!!" if isPalindrome(sll.head) else "Nope it is not.. :("

