from core.aastra.Base import BaseFormat

__author__ = 'amucci'
from xml.etree.ElementTree import SubElement

class AastraIPPhoneTextMenu(BaseFormat):

    element_name = "AastraIPPhoneTextMenu"

    def add_title(self,text, wrap=None):
        title_subelement = SubElement(self.root, "Title")
        if wrap is not None:
            title_subelement.set("wrap", "yes")
        title_subelement.text = text

    def add_menu_item(self, prompt, uri, dial=None, selection=None):
        menu_item = SubElement(self.root, "MenuItem")
        prompt_item = SubElement(menu_item, "Prompt")
        prompt_item.text = prompt
        uri_item = SubElement(menu_item, "URI")
        uri_item.text = uri
        if dial is not None:
            dial_item = SubElement(menu_item, "Dial")
            dial_item.set("line", dial['line'])
            dial_item.text = dial['text']

