from Compiler import *
class iOSCOmpiler(Compiler):

	def collectSource(self):
		print("Collection Swift Source Code")
	def compileToObject(self):
		print("Compiling Swift code to LLVM bitcode")
	def run(self):
		print("Program running on runtime environment")

iOS = iOSCOmpiler()
iOS.compileAndRun()
