from DebitCard_Proxy import *
class You:
	def __init__(self):
		print("You :: Lets buy the Denim Shirt")
		self.debitCard = DebitCard()
		self.isPurchased = None
	def makePayment(self):
		self.isPurchased = self.debitCard.do_pay()

	def __del__(self):
		if self.isPurchased:
			print("You:: WowW Denim Shirt is Mine ")
		else:
			print("You:: I should earn more!")

you = You()
you.makePayment()

