from Products.DataCollector.plugins.CollectorPlugin import SnmpPlugin, GetTableMap
from Products.DataCollector.plugins.DataMaps import ObjectMap
import logging

logger = logging.getLogger('zen.ZenModeler')

class PrinterTonerMap(SnmpPlugin):
   
    maptype = "PrinterTonerMap"
    relname = "toner"
    compname = "hw"
    modname = "ZenPacks.luizzmizz.PrinterMIB.PrinterToner"
    classname = "PrinterToner"
    
    columns = {
         '.3': 'snmpindex',
         '.5': 'cartType',
         '.6': 'color',
         '.7': 'unit',
         '.8': 'Max',
         '.9': 'current',
         }

    cartType = {
         1: 'other(1)',
         2: 'unknown(2)',
         3: 'toner(3)',
         4: 'wasteToner(4)',
         5: 'ink(5)',
         6: 'inkCartridge(6)',
         7: 'inkRibbon(7)',
         8: 'wasteInk(8)',
         9: 'opc(9)',
         10: 'developer(10)',
         11: 'fuserOil(11)',
         12: 'solidWax(12)',
         13: 'ribbonWax(13)',
         14: 'wasteWax(14)',
         15: 'fuser(15)',
         16: 'coronaWire(16)',
         17: 'fuserOilWick(17)',
         18: 'cleanerUnit(18)',
         19: 'fuserCleaningPad(19)',
         20: 'transferUnit(20)',
         21: 'tonerCartridge(21)',
         22: 'fuserOiler(22)',
         }

    cartUnit = {
         3: 'tenThousandthsOfInches(3)',
         4: 'micrometers(4)',
         7: 'impressions(7)',
         8: 'sheets(8)',
         11: 'hours(11)',
         12: 'thousandthsOfOunces(12)',
         13: 'tenthsOfGrams(13)',
         14: 'hundrethsOfFluidOunces(14)',
         15: 'tenthsOfMilliliters(15)',
         16: 'feet(16)',
         17: 'meters(17)',
         19: 'unknown(19'),
         }

    snmpGetTableMaps = (
        GetTableMap('fsTableOid', '.1.3.6.1.2.1.43.11.1.1', columns),
    )

    def process(self, cartridge, results, log):
        getdata, tabledata = results
        snmptable = tabledata.get("fsTableOid")
	
        maps = []
	om = []
        rm = self.relMap()
        for idx,ct in snmptable.iteritems():
            snmpindex = idx.split(".")[1]
            res = {}
            color = ct['color'].replace("[","(")
            color = color.replace("]",")")
            color = color.replace("/","-")
            color = color.replace("\\","-")
            res['id'] = snmpindex
            res['snmpindex'] = snmpindex
            res['tonerName'] = unicode(color, "ISO-8859-1")
            if ct['Max']:
              res['maxToner'] = ct['Max']
            if ct['cartType']:
              res['cartType'] = self.cartType[ct['cartType']]
            if ct['unit']:
              res['cartUnit'] = self.cartUnit[ct['unit']]
            log.debug('RES: %s', res)
            om = self.objectMap(res)
            rm.append(om)
        log.debug("MAPS: %s", om)
        return rm


