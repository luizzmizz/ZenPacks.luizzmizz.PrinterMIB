from Globals import InitializeClass
from Products.ZenRelations.RelSchema import *
from Products.ZenModel.ManagedEntity import ManagedEntity
from Products.ZenModel.ZenossSecurity import *
from Products.ZenModel.DeviceComponent import DeviceComponent
from Products.ZenModel.HWComponent import HWComponent

class PrinterToner(DeviceComponent, ManagedEntity):

    portal_type = meta_type = 'PrinterToner'

    tonerName = ''
    maxToner = -1
    currentToner = -1
    cartType = ''
    cartUnit = ''

    _properties = HWComponent._properties + (
        {'id':'tonerName', 'type':'string', 'mode':''},
        {'id':'maxToner', 'type':'int', 'mode':''},
        {'id':'currentToner', 'type':'int', 'mode':''},
        {'id':'cartType', 'type':'string', 'mode':''},
        {'id':'cartUnit', 'type':'string', 'mode':''},
        )

    _relations = (
        ("hw", ToOne(ToManyCont, "ZenPacks.luizzmizz.PrinterMIB.PrinterDevice", "toner")),
        )

    factory_type_information = ( 
        { 
            'id'             : 'PrinterToner',
            'meta_type'      : 'PrinterToner',
            'description'    : """Printer Toner info""",
            'product'        : 'PrinterToner',
            'immediate_view' : 'viewPrinterToner',
            'actions'        :
            ( 
                { 'id'            : 'status'
                , 'name'          : 'Printer Toner Graphs'
                , 'action'        : 'viewPrinterToner'
                , 'permissions'   : (ZEN_VIEW, )
                },
                { 'id'            : 'perfConf'
                , 'name'          : 'Printer Toner Template'
                , 'action'        : 'objTemplates'
                , 'permissions'   : (ZEN_CHANGE_SETTINGS, )
                },                
                { 'id'            : 'viewHistory'
                , 'name'          : 'Modifications'
                , 'action'        : 'viewHistory'
                , 'permissions'   : (ZEN_VIEW, )
                },
            )
          },
        ) 

    def showToner(self):
       print ('TonerName=%s, maxToner=%s, currentToner=%s tonerType=%s unit=%s' % (self.tonerName, self.maxToner, self.currentToner, self.cartType, self.cartUnit))
    
    def viewName(self):
        return self.tonerName
        
    name = primarySortKey = viewName

    def device(self):
      return self.hw().device()
      
    def getId(self):
        return self.id

    def currentValue(self, default=None):
        """
        Return the current toner levels
        """
        currentVal = self.cacheRRDValue('toner_toner', default)
        if currentVal is None:
            return "no value"
        if currentVal is not None:
            return long(currentVal)
        return None
    currentvalue = currentValue

    def getPercent(self):
        currentVal = self.cacheRRDValue('toner_toner', default)


InitializeClass(PrinterToner)
