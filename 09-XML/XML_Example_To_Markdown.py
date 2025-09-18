"""
@author hakon.fjelstad@entur.org
"""

import xml.etree.ElementTree as ET
from xml.dom import minidom

# Function to remove namespace from tag
def strip_namespace(tag):
    return tag.split('}', 1)[-1] if '}' in tag else tag

# Recursively remove namespaces from all elements
def remove_namespaces(elem):
    elem.tag = strip_namespace(elem.tag)
    for child in elem:
        remove_namespaces(child)

def xmlToMarkdown(File, OutputPath, RemovePath): 
    tree = ET.parse(File)
    root = tree.getroot()
    remove_namespaces(root)
    #markdownPath = OutputPath
    markdownFileName = str(File).replace('.xml','.md').replace(RemovePath,'')
    print(markdownFileName)
    markdownFile = open(OutputPath + markdownFileName, "w")

    try:
        x = root.findall("Description")
        for y in x:
            markdownFile.write(y.text)
            markdownFile.write('\n')
    except:
        pass
    # Find all elements with attribute 'nameOfClass'
    elements_with_nameOfClass_attribute = root.findall(".//*[@nameOfClass]")

    # Generate markdown content
    markdown_lines = []
    for elem in elements_with_nameOfClass_attribute:
        # Extract and remove Description if present
        description_text = None
        for child in elem.findall('Description'):
            description_text = child.text.strip() if child.text else ''
            elem.remove(child)

        # Remove nameOfClass attribute
        del elem.attrib['nameOfClass']

        # Add description to markdown
        if description_text:
            markdown_lines.append(description_text)
            markdown_lines.append('\n\n')

        # Convert element to string and add as code block
        
        
        # Konverter til string og fjern tomme linjer
        rough_string = ET.tostring(elem, encoding='unicode')
        reparsed = minidom.parseString(rough_string)
        pretty_xml = reparsed.toprettyxml(indent="    ")

        # Fjern XML-deklarasjonen og tomme linjer
        lines = pretty_xml.split('\n')
        filtered_lines = [line for line in lines if line.strip() and not line.strip().startswith('<?xml')]
        cleaned_xml = '\n'.join(filtered_lines)

        markdown_lines.append('```xml\n' + cleaned_xml + "\n```\n") 

    for x in markdown_lines:
        markdownFile.write(x)

if __name__ == "__main__":
    xmlToMarkdown("09-XML\guides\Timetable_DatedServiceJourney.xml")