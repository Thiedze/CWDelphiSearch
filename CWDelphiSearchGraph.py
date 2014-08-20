#!/usr/bin/python

# Import graphviz
import sys
import gv

# Import pygraph
from pygraph.classes.graph import graph
from pygraph.readwrite.dot import write

class CWGraph:
	
	def __init__(self, documentation):
		self.gr = graph()
		self.documentation = documentation


	def CreateClassDiagram(self):		
		for delphi in self.documentation:
			for delphiClass in delphi.classes:
				self.gr.add_nodes([delphiClass.name])

		for delphi in self.documentation:
			for delphiClass in delphi.classes:
				try:
					self.gr.add_edge((delphiClass.name, delphiClass.superClass))
				except:
					print("Edge already exist")
		dot = write(self.gr)
		gvv = gv.readstring(dot)
		gv.layout(gvv,'dot')
		gv.render(gvv,'svg','Delphi-Classdiagram.svg')
