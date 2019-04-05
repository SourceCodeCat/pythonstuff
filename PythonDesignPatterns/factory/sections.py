
from abc import ABCMeta, abstractmethod

#v3.5
#class Section(metaclass=ABCMeta):
#v2.x
class Section:
	__metaclass__ = ABCMeta
	@abstractmethod
	def describe(self):
		pass

class PersonalSection(Section):
	def describe(self):
		print ("personal section!")

class AlbumSection(Section):
	def describe(self):
		print("album section!")


class PatentSection(Section):
	def describe(self):
		print("patent section!")

class PublicationSection(Section):
	def describe(self):
		print("publication section!")


















