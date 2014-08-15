#!/usr/bin/python

import string
import copy

from CWDelphiSearchModel import CWDelphiClass

class CWDelphiSearchParse:
	
	def __init__(self):
		self.foundPrivate = False
		self.foundPublic = False
		self.foundProtected = False
		self.foundPublished = False
		self.foundClass = False
		self.foundConst = False

	def SetFlags(self, foundPrivate, foundPublic, foundProtected, foundPublished, foundConst, foundClass):
		self.foundPrivate = foundPrivate
		self.foundProtected = foundProtected
		self.foundPublic = foundPublic
		self.foundPublished = foundPublished
		self.foundClass = foundClass
		self.foundConst = foundConst


	def FoundClassTag(self, line):
		if "=class" in line.translate(None, string.whitespace).lower():
			return True
		else:
			return False

	def SaveFunctions(self, line):
		if self.delphiClass != None and len(line.translate(None, string.whitespace).lower()) > 0 and '//' not in line.translate(None, string.whitespace).lower():
			if self.foundConst == True:
				self.delphiClass.consts.append(line)
				return True			

			if self.foundClass == True:
				self.delphiClass.nonFlagedFunctions.append(line)
				return True

			if self.foundPrivate == True:
				self.delphiClass.privateFunctions.append(line)
				return True
			
			if self.foundPublic == True:
				self.delphiClass.publicFunctions.append(line)
				return True
		
			if self.foundProtected == True:
				self.delphiClass.protectedFunctions.append(line)
				return True

			if self.foundPublished == True:
				self.delphiClass.publishedFunctions.append(line)
				return True

		return False

	def SaveFlags(self, line):
		if "private" in line.lower():
			self.SetFlags(True, False, False, False, False, False)
			return True
			
		if "public" in line.lower():	
			self.SetFlags(False, True, False, False, False, False)
			return True
					
		if "protected" in line.lower():	
			self.SetFlags(False, False, True, False, False, False)
			return True
			
		if "published" in line.lower():
			self.SetFlags(False, False, False, True, False, False)
			return True

		if line.translate(None, string.whitespace).lower() == "const":
			self.SetFlags(False, False, False, False, True, False)
			return True

		if line.translate(None, string.whitespace).lower() == "type":
			self.SetFlags(False, False, False, False, False, False)
			return True
		
		if "record" in line.lower():
			self.SetFlags(False, False, False, False, False, False)
			return True

		if self.foundConst == True and ("function" in line.lower() or "procedure" in line.lower()):
			self.SetFlags(False, False, False, False, False, True)

		return False		

	def findBetween(self, s, first, last ):
		try:
			start = s.index( first ) + len( first )
			end = s.index( last, start )
			return s[start:end]
		except ValueError:
			return ""

	def searchForDependencies(self, foundDelphi):
		searchDelphi = list(foundDelphi)
		for found in foundDelphi:			
			for search in searchDelphi:
				for foundClass in found.classes:
					for searchClass in search.classes:
						if foundClass.name == searchClass.superClass:
							foundClass.dependencies.append(searchClass.name)

	def ParseFile(self, path):		
		classes = []
		self.delphiClass = None	

		f = open(path)
		lines = f.readlines()
		f.close()

		for line in lines:
	
			if self.FoundClassTag(line) == True:
				if self.delphiClass != None:
					classes.append(self.delphiClass)
				self.delphiClass = CWDelphiClass()
				self.delphiClass.name = line.split('=')[0].translate(None, string.whitespace)
				self.delphiClass.superClass = self.findBetween(line, "(", ")").translate(None, string.whitespace)
				self.SetFlags(False, False, False, False, False, True)
				continue
			
			if "end;" in line.lower():
				self.SetFlags(False, False, False, False, False, False)
				continue	
			
			if "implementation" in line.lower():
				break			
			
			if self.SaveFlags(line) == True:
				continue

			if self.SaveFunctions(line) == True:
				continue

		if self.delphiClass != None:
			classes.append(self.delphiClass)

		return classes

