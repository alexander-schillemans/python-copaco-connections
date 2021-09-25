from pathlib import Path
import xml.etree.ElementTree as ET

from .constants.errors import NotFoundError

class XMLHandler:

    def __init__(self):

        self.rootDir = Path(__file__).parent.absolute()
        self.tempDir = '{root}/temp'.format(root=self.rootDir)

    
    def getRoot(self, filePath):
        """ Takes the path to an XML file and returns an ElementTree object """

        path = '{root}/{filePath}'.format(root=self.rootDir, filePath=filePath)
        return ET.parse(path).getroot()
    

    def parseJSON(self, json):
        """ Takes the JSON representation of an object and converts it to XML, returns an ElementTree object """

        # We can only have one root element, which is the first key in the dictionary
        firstKey = next(iter(json))
        parentElement = ET.Element(firstKey)

        for k1, v1 in json[firstKey].items():

            if v1['type'] == 'ATTRIBUTE':
                parentElement.set(k1, v1['value'])
            elif v1['type'] == 'PROPERTY':
                ET.SubElement(parentElement, k1).text = v1['value']
            elif v1['type'] == 'ELEMENT':
                element = self.parseJSON(v1['values'])
                parentElement.append(element)
            elif v1['type'] == 'LIST':
                for v in v1['values']:
                    element = self.parseJSON(v)
                    parentElement.append(element)
            elif v1['type'] == 'TEXT':
                parentElement.text = v1['value']
        
        return parentElement

            


