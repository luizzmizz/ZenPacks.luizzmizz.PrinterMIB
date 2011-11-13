from Products.Zuul.interfaces import IComponentInfo
from Products.Zuul.form import schema
from Products.Zuul.utils import ZuulMessageFactory as _t


class IPrinterTonerInfo(IComponentInfo):
    """
    Info adapter for Printer Toner component
    """
    tonerName = schema.Text(title=u"Toner name", readonly=True, group='Details')
    maxToner = schema.Text(title=u"Max toner", readonly=True, group='Details')
    currentToner = schema.Text(title=u"Current toner", readonly=True,group='Details')
    cartType = schema.Text(title=u"Cartridge type", readonly=True, group='Details')
    cartUnit = schema.Text(title=u"Cartridge unit", readonly=True, group='Details')
