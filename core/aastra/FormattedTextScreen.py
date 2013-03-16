from core.aastra.Base import BaseFormat

__author__ = 'amucci'
from xml.etree.ElementTree import SubElement

class AastraIPPhoneFormattedTextScreen(BaseFormat):

    element_name = "AastraIPPhoneFormattedTextScreen"

    def add_line(self,text, size=None, align=None,color=None):
        line_subelement = SubElement(self.root, "Line")
        if size is not None:
            line_subelement.set("Size", size)
        if align is not None:
            line_subelement.set("Align", align)
        if color is not None:
            line_subelement.set("Color", color)
        line_subelement.text = text