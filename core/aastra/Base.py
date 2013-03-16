__author__ = 'amucci'
from xml.dom import minidom
from xml.etree.ElementTree import Element, tostring, SubElement

class BaseFormat:

    element_name = ""
    root = None

    def __init__(self,
                 type=None,
                 password = None,
                 editable = None,
                 displayMode= None,
                 defaultIndex = None,
                 style = None,
                 wrapList = None,
                 scrollConstrain= None,
                 unitScroll = None,
                 numberLaunch = None,
                 destroyOnExit=None,
                 cancelAction=None,
                 doneAction=None,
                 imageAction=None,
                 mode=None,
                 beep=None,
                 timeout=None,
                 allowAnswer=None,
                 allowDrop=None,
                 allowXFer=None,
                 allowConf=None,
                 lockIn=None,
                 allowDTMF=None,
                 scrollUp=None,
                 scrollDown=None,
                 scrollLeft=None,
                 scrollRight=None):

        #create root
        self.root = Element(self.element_name)

        if type is not None:
            self.root.set("type",type)
        if password is not None:
            self.root.set("password","yes")
        if editable is not None:
            self.root.set("editable","no")
        if displayMode is not None:
            self.root.set("displayMode","condensed")
        if style is not None:
            self.root.set("style", style)
        if defaultIndex is not None:
            self.root.set("defaultIndes",defaultIndex)
        if wrapList is not None:
            self.root.set("wrapList", "yes")
        if scrollConstrain is not None:
            self.root.set("scrollConstrain", "yes")
        if unitScroll is not None:
            self.root.set("unitScroll", "yes")
        if numberLaunch is not None:
            self.root.set("numberLaunch","yes")

        if destroyOnExit is not None:
            self.root.set("destroyOnExit", "yes")
        if cancelAction is not None:
            self.root.set("cancelAction", cancelAction)
        if doneAction is not None:
            self.root.set("doneAction", doneAction)
        if imageAction is not None:
            self.root.set("imageAction", imageAction)
        if mode is not None:
            self.root.set("mode", mode)
        if beep is not None:
            self.root.set("Beep", "yes")
        if timeout is not None:
            self.root.set("Timeout", timeout)
        if allowAnswer is not None:
            self.root.set("allowAnswer", "yes")
        if allowDrop is not None:
            self.root.set("allowDrop", "yes")
        if allowConf is not None:
            self.root.set("allowConf", "yes")
        if allowXFer is not None:
            self.root.set("allowXFer", "yes")
        if allowDTMF is not None:
            self.root.set("allowDTMF", "yes")
        if lockIn is not None:
            self.root.set("LockIn","yes")
        if scrollUp is not None:
            self.root.set("scrollUp", scrollUp)
        if scrollRight is not None:
            self.root.set("scrollRight", scrollRight)
        if scrollLeft is not None:
            self.root.set("scrollLeft", scrollLeft)
        if scrollDown is not None:
            self.root.set("scrollDown", scrollDown)

    def prettify(self, elem):
        """Return a pretty-printed XML string for the Element.
        """
        rough_string = tostring(elem, 'utf-8')
        reparsed = minidom.parseString(rough_string)
        return reparsed.toprettyxml(indent="  ")

    def addSoftKey(self,index,label,uri):
        softKey = SubElement(self.root, "SoftKey")
        softKey.set("index",index)
        label_key = SubElement(softKey,"Label")
        label_key.text = label
        uri_key = SubElement(softKey,"URI")
        uri_key.text = uri

    def getXML(self):
        return self.prettify(self.root)