#!/usr/bin/python

class CWDelphiSearchSave:
	
	def __init__(self, documentation):
		self.documentation = documentation

	def Save(self):
		with open("Output.txt", "w") as textFile:
			for delphi in self.documentation:
				textFile.write("\n\nDirectory: {}\n".format(delphi.directory))
				textFile.write("	Unit: {}\n".format(delphi.unit))
			
				for delphiClass in delphi.classes:
					textFile.write("		Class: {0} ({1})\n".format(delphiClass.name, delphiClass.superClass))
					
					if len(delphiClass.dependencies) > 0:
						textFile.write("			Dependencies: \n")
						for dependency in delphiClass.dependencies:
							textFile.write("				{}\n".format(dependency))
					
					if len(delphiClass.nonFlagedFunctions) > 0:
						for nonFlaged in delphiClass.nonFlagedFunctions:
							textFile.write("				{}\n".format(nonFlaged))

					if len(delphiClass.privateFunctions) > 0:
						textFile.write("			Private: \n")
						for private in delphiClass.privateFunctions:
							textFile.write("				{}\n".format(private))

					if len(delphiClass.publicFunctions) > 0:
						textFile.write("			Public: \n")
						for public in delphiClass.publicFunctions:
							textFile.write("				{}\n".format(public))

					if len(delphiClass.protectedFunctions) > 0:
						textFile.write("			Protected: \n")
						for protected in delphiClass.protectedFunctions:
							textFile.write("				{}\n".format(protected))

					if len(delphiClass.publishedFunctions) > 0:
						textFile.write("			Published: \n")
						for published in delphiClass.publishedFunctions:
							textFile.write("				{}\n".format(published))
										
					if len(delphiClass.consts) > 0:
						textFile.write("			Constants: \n")
						for const in delphiClass.consts:
							textFile.write("				{}\n".format(const))


