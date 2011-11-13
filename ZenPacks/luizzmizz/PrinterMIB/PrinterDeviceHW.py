from Globals import InitializeClass
from Products.ZenModel.DeviceHW import DeviceHW
from Products.ZenModel.Hardware import Hardware
from Products.ZenRelations.RelSchema import ToManyCont, ToOne

class PrinterDeviceHW(DeviceHW):

    # Define new relationships
    _relations = Hardware._relations + (
        ("toner", ToManyCont(ToOne, "ZenPacks.luizzmizz.PrinterMIB.PrinterToner", "hw")),
    )

    def __init__(self):
        id = "hw"
        Hardware.__init__(self, id)

InitializeClass(PrinterDeviceHW)
