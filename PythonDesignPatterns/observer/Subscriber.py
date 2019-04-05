from abc import ABCMeta, abstractmethod

class Subscriber(metaclass=ABCMeta):

	@abstractmethod
	def update(self):
		pass

