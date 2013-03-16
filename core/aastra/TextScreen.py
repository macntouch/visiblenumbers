from xml.etree.ElementTree import SubElement
from core.aastra.Base import BaseFormat

__author__ = 'amucci'

class AastraIPPhoneTextScreen(BaseFormat):

    element_name = "AastraIPPhoneTextScreen"

    def setTitle(self,text):
        title = SubElement(self.root, "Title")
        title.text = text

    def setBody(self,text):
        body = SubElement(self.root, "Text")
        body.text = text