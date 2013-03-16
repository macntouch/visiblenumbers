from core.aastra.Base import BaseFormat

__author__ = 'amucci'
from xml.etree.ElementTree import SubElement

class AastraIPPhoneMultipleInputScreen(BaseFormat):

    element_name = "AastraIPPhoneInputScreen"

    def addTitle(self,text):
        title = SubElement(self.root, "Title")
        title.text = text

    def addPrompt(self,text):
        prompt = SubElement(self.root, "Prompt")
        prompt.text = text

    def addUrl(self,text):
        url = SubElement(self.root, "URL")
        url.text = text

    def addParameter(self,text):
        parameter = SubElement(self.root, "Parameter")
        parameter.text = text

    def addDefault(self,text):
        parameter = SubElement(self.root, "Default")
        parameter.text = text

    def addInputfield(self,type,prompt,editable=None,parameter=None,default=None):
        inputField = SubElement(self.root, "InputField")
        inputField.set("type",type)
        prompt_field = SubElement(inputField,"Prompt")
        prompt_field.text=prompt
        if editable is not None:
            inputField.set("editable",editable)
        if parameter is not None:
            parameter_field = SubElement(inputField,"Parameter")
            parameter_field.text=parameter
        if default is not None:
            default_field = SubElement(inputField,"Default")
            default_field.text=default

