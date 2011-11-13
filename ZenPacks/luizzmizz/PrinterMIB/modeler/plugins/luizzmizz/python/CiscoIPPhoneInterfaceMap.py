from xml.dom.minidom import parse
import urllib
import struct
from Products.DataCollector.plugins.CollectorPlugin import PythonPlugin
from Products.DataCollector.plugins.DataMaps import ObjectMap

class CiscoIPPhoneInterfaceMap(PythonPlugin):
    maptype = "InterfaceMap" 
    modname = "Products.ZenModel.IpInterface"
    relname = "interfaces"
    compname="os"

    def collect(self, device, log):
        names = ['MACAddress','HostName','IPAddress','SubNetMask']
        values=self.getCiscoIPPhoneInterface(device.id,names,log)
        log.debug('Collect.values:%s'%values)
        return values

    def process(self, device, results, log):
        log.info('Collecting Cisco interface info for device %s' % device.id)
	rm = self.relMap()
        log.info('Results: %s'%results)
        i=0
        if results:
	  om = self.objectMap({})
          om.id="eth0"
          om.interfaceName=om.id
	  om.setIpAddresses= results[2]
          om.macaddress= ':'.join(results[0][c:c+2] for c in range(0, 12, 2)).upper()
          om.monitor=False 
	  rm.append(om)
        else:
          return 0
        log.debug("MAPS: %s"%rm)
        return rm

    def getCiscoIPPhoneInterface(self,deviceIP,valueList,log):
      ret=[]
      try:
        dom=parse(urllib.urlopen('http://%s/NetworkConfigurationX'%deviceIP))
      except Exception as e:
        log.error("Parse Cisco Network Information: %s, "%e)
        return 0 
      for value in valueList:
        for node in dom.getElementsByTagName(value):
          try: 
            ret.append(node.childNodes[0].nodeValue)
          except Exception as e:
            ret.append("")
            log.error("Error retrieveng XML value %s: %s"%(value,e))
      return ret 
