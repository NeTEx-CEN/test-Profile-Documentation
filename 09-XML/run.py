"""
@author hakon.fjelstad@entur.org
"""

import os
from XML_Example_To_Markdown import xmlToMarkdown as XtM

xmlPath = '09-XML\\'
for example in os.listdir(xmlPath):
    if example == 'guides':
        for x in os.listdir(xmlPath + example):
            print(xmlPath + example + '\\' + x)
            XtM(xmlPath + example + '\\' + x, '04-Guides\\', xmlPath + example + '\\')
    elif example == 'usecases':
        for y in os.listdir(xmlPath + example):
            print(y)
            XtM(xmlPath + example + '\\' + y, '05-Use case\\', xmlPath + example + '\\')