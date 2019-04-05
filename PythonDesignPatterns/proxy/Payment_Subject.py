from abc import ABCMeta, abstractmethod

# v3.5
class Payment(metaclass=ABCMeta):
#-------------------------------
#v2.x
#class Payment
#	__metaclass__ = ABCMeta

	@abstractmethod
	def do_pay():
		pass


