from core.aastra.Base import BaseFormat
from xml.etree.ElementTree import SubElement
__author__ = 'amucci'

class AastraIPPhoneExecute(BaseFormat):

    element_name = "AastraIPPhoneExecute"

    def add_item(self,URI, interruptCall=None):
        line_subelement = SubElement(self.root, "ExecuteItem")
        line_subelement.set("URI", URI)
        if interruptCall is not None:
            line_subelement.set("interruptCall", "no")