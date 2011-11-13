from zope.interface import implements
from Products.Zuul.infos import ProxyProperty
from Products.Zuul.infos.component import ComponentInfo
from Products.Zuul.decorators import info
from ZenPacks.luizzmizz.PrinterMIB import interfaces

class PrinterTonerInfo(ComponentInfo):
    implements(interfaces.IPrinterTonerInfo)

    tonerName = ProxyProperty("tonerName")
    maxToner = ProxyProperty("maxToner")
    currentToner = ProxyProperty("currentToner")
    cartType = ProxyProperty("cartType")
    cartUnit = ProxyProperty("cartUnit")


