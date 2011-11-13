from xml.dom.minidom import parse
import urllib
import socket
from Products.DataCollector.plugins.CollectorPlugin import PythonPlugin
from Products.DataCollector.plugins.DataMaps import ObjectMap

socket.setdefaulttimeout(1)

class CiscoIPPhoneMap(PythonPlugin):
    maptype = "DeviceMap" 
    modname = "Products.ZenModel.Device"

    def collect(self, device, log):
        names = ['MACAddress','phoneDN','serialNumber','modelNumber','HostName']
        values = self.getCiscoIPPhoneVals(device.id,names,log)
	return values 

    def process(self, device, results, log):
        log.info('Collecting Cisco info for device %s' % device.id)
	om = self.objectMap({})
        log.info('Results: %s'%results)
        if results:
          om.setHWSerialNumber=results[2]
          om.setHWTag=results[1]
          om.setHWProduct=results[3]
          om.title=results[4]
          om.zLinks='http://%s/DeviceInformationX'%device.manageIp
        return om

    def getCiscoIPPhoneVals(self,deviceIP,valueList,log):
      ret=[]
      try:
        dom=parse(urllib.urlopen('http://%s/DeviceInformationX'%deviceIP))
      except Exception as e:
        log.error("Parse Cisco DeviceInformationX: %s"%e)
        return 0 
      for value in valueList:
        for node in dom.getElementsByTagName(value):
          if len(node.childNodes)>0:
            ret.append(node.childNodes[0].nodeValue)
          else:
            ret.append('-')
      return ret

