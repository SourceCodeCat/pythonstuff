from abc import ABCMeta,abstractmethod

class Compiler(metaclass=ABCMeta):

	@abstractmethod
	def collectSource(self):
		pass
	@abstractmethod
	def compileToObject(self):
		pass
	@abstractmethod
	def run(self):
		pass

	def compileAndRun(self):
		self.collectSource()
		self.compileToObject()
		self.run()


