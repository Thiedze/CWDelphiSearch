#!/usr/bin/python

import os

from CWDelphiSearchSave import CWDelphiSearchSave
from CWDelphiSearchParse import CWDelphiSearchParse
from CWDelphiSearchModel import CWDelphi

documentation = []

for dirInfo in os.walk('.'):
	directory = dirInfo[0]
	for file in os.listdir(directory):
		if file.endswith(".pas"):
			delphi = CWDelphi()
			delphi.unit = file
			delphi.directory = directory
			delphi.classes = CWDelphiSearchParse().ParseFile(delphi.directory+"/"+delphi.unit)
			documentation.append(delphi)

delphiSearchSave = CWDelphiSearchSave(documentation)
delphiSearchSave.Save()
