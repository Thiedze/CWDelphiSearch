#!/usr/bin/python

import os

from CWDelphiSearchSave import CWDelphiSearchSave
from CWDelphiSearchParse import CWDelphiSearchParse
from CWDelphiSearchModel import CWDelphi
from CWDelphiSearchGraph import CWGraph

documentation = []

print("Search and parse delphi files.")
for dirInfo in os.walk('.'):
	directory = dirInfo[0]
	for file in os.listdir(directory):
		if file.endswith(".pas"):
			delphi = CWDelphi()
			delphi.unit = file
			delphi.directory = directory
			delphi.classes = CWDelphiSearchParse().ParseFile(delphi.directory+"/"+delphi.unit)
			documentation.append(delphi)

print("Search dependencies.")
CWDelphiSearchParse().searchForDependencies(documentation)

print("Draw and save classdiagram.")
graph = CWGraph(documentation)
graph.CreateClassDiagram()

print("Save.")
delphiSearchSave = CWDelphiSearchSave(documentation)
delphiSearchSave.Save()
