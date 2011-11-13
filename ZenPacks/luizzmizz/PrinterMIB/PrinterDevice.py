from Globals import InitializeClass
from Products.ZenRelations.RelSchema import *
from Products.ZenModel.Device import Device
from Products.ZenModel.OperatingSystem import OperatingSystem
from Products.ZenModel.ZenossSecurity import ZEN_VIEW, ZEN_CHANGE_SETTINGS
from Products.ZenModel.ManagedEntity import ManagedEntity
from PrinterDeviceHW import PrinterDeviceHW
from copy import deepcopy

class PrinterDevice(Device):
    factory_type_information = deepcopy(Device.factory_type_information)
    def __init__(self, id, buildRelations=True):
        ManagedEntity.__init__(self, id, buildRelations=buildRelations)
        os = OperatingSystem()
        self._setObject(os.id, os)
        hw = PrinterDeviceHW()
        self._setObject(hw.id, hw)
        #self.commandStatus = "Not Tested"
#        self._lastPollSnmpUpTime = ZenStatus(0)
        self._snmpLastCollection = 0
        self._lastChange = 0

InitializeClass(PrinterDevice)
