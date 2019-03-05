from lxml import etree
import lxml.builder   
import os

def convert_types():

    myDir = os.path.dirname(os.path.realpath(__file__))
    namespaces = {'dc':'http://purl.org/dc/elements/1.1/'}
    
    

    for file in os.listdir(myDir):
        if file.endswith(".xml"):
           
           nsmap = {
               'xlink': "http://www.w3.org/1999/xlink",
               'xsi': "http://www.w3.org/2001/XMLSchema-instance",
               'xmlns': "http://www.loc.gov/mods/v3",
               'schemaLocation': "http://www.loc.gov/mods/v3",
               'schemaLocation': "http://www.loc.gov/standards/mods/v3/mods-3-3.xsd"
            }

       
           root = etree.parse(file)
           titles = root.xpath('//dc:title/text()', namespaces=namespaces)
           creators = root.xpath('//dc:creator/text()', namespaces=namespaces)
           subjects = root.xpath('//dc:subject/text()', namespaces=namespaces)
           descriptions = root.xpath('//dc:description/text()', namespaces=namespaces)
           publishers = root.xpath('//dc:publisher/text()', namespaces=namespaces)
           xml_dates = root.xpath('//dc:date/text()', namespaces=namespaces)
           formats = root.xpath('//dc:format/text()', namespaces=namespaces)
           rights = root.xpath('//dc:rights/text()', namespaces=namespaces)
           E = lxml.builder.ElementMaker()
           schemas=etree.Element('modsCollection', nsmap=nsmap)
           st=etree.SubElement(schemas, 'mods', version='3.5')
           co=etree.SubElement(st, 'titleInfo')
          
           
           for title in titles:
               hawk=etree.SubElement(co, 'title')
               hawk.text = title 
           
           for creator in creators:
               eag=etree.SubElement(st, 'name', type='personal')
               eagl=etree.SubElement(eag, 'namePart')
               eagle=etree.SubElement(eagl, 'role')
               eagle.text=creator
               
           for subject in subjects:
               cran=etree.SubElement(st, 'subject')
               crane=etree.SubElement(cran, 'topic')
               crane.text=subject
            
           for description in descriptions:
               robin=etree.SubElement(st, 'note')
               robin.text=description
               
           for publisher in publishers:
               grackl=etree.SubElement(st, 'originInfo')
               grackle=etree.SubElement(grackl, 'publisher')
               grackle.text=publisher
               
           for xml_date in xml_dates:
               crow=etree.SubElement(grackl, 'dateOther')
               crow.text=xml_date
               
           for format in formats:
               dov=etree.SubElement(st, 'physicalDescription')
               dove=etree.SubElement(dov, 'form')
               dove.text=format
           
           for right in rights:
               bluejay=etree.SubElement(st, 'accessCondition')
               bluejay.text=format
          
           print etree.tostring(schemas, pretty_print=True, xml_declaration = True, encoding='UTF-8')
           
           
           i = 0
           while os.path.exists("mods%s.xml" % i):
               i += 1

           fh = open("mods%s.xml" % i, "w")
           my_tree = etree.ElementTree(schemas)
           fh.write(etree.tostring(my_tree, pretty_print=True))
           
convert_types()
