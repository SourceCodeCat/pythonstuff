from abc import ABCMeta, abstractmethod
from sections import *
#v3.5
#class Profile(metaclass=ABCMeta):
#--------------------------------
#v2.x
class Profile:
#--------------------------------
	__metaclass__ = ABCMeta
	def __init__(self):
		self.sections = []
		self.createProfile()
	@abstractmethod
	def createProfile(self):
		pass
	def getSections(self):
		return self.sections
	def addSections(self,section):
		return self.sections.append(section)

class Linkedin(Profile):
	def createProfile(self):
		self.addSections(PersonalSection())
		self.addSections(PatentSection())
		self.addSections(PublicationSection())

class Facebook(Profile):
	def createProfile(self):
		self.addSections(PersonalSection())
		self.addSections(AlbumSection())


