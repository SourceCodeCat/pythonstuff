from Payment_Subject import *
import random


class Bank(Payment):

	

	def __init__(self):
		self.card= None
		self.account = None
		self.fund_state = [True,False]

	def __getAccount(self):
		self.account = self.card
		return self.account

	def __hasFunds(self):
		print("Bank:: Checking if Account",self.__getAccount(),"Has enough funds")
		return random.choice(self.fund_state)

	def setCard(self,card):
		self.card = card

	def do_pay(self):
		if self.__hasFunds():
			print("Bank:: Paying the merchant")
			return True
		else:
			print("Bank:: Sorry, not enough funds!")
			return False

		
