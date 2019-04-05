from Subscriber import *

class EMAILSubscriber(Subscriber):

	def __init__(self,publisher):
		self.publisher = publisher
		self.publisher.attach(self)
	def  update(self):
		print(type(self).__name__,self.publisher.getNews())


