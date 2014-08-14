#!/usr/bin/python

class CWDelphiClass:
	
	def __init__(self):
		self.name = ''
		self.consts = []
		self.privateFunctions = []
		self.publicFunctions = []
		self.protectedFunctions = []
		self.publishedFunctions = []
		self.nonFlagedFunctions = []

class CWDelphi:

	def __init__(self):
		self.directory = ''
		self.unit = ''
		self.classes = []
