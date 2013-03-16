from xml.etree.ElementTree import SubElement
from core.aastra.Base import BaseFormat

__author__ = 'amucci'


class AastraIPPhoneImageScreen(BaseFormat):

    element_name = "AastraIPPhoneImageScreen"

    def add_image(self,height, width, url, verticalAlign=None,horizontalAlign=None):
        line_subelement = SubElement(self.root, "Image")
        line_subelement.set("height", height)
        line_subelement.set("width",width)
        if verticalAlign is not None:
            line_subelement.set("verticalAlign", verticalAlign)
        if horizontalAlign is not None:
            line_subelement.set("horizontalAlign", horizontalAlign)
        line_subelement.text = url