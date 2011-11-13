(function(){

var ZC = Ext.ns('Zenoss.component');


function render_link(ob) {
    if (ob && ob.uid) {
        return Zenoss.render.link(ob.uid);
    } else {
        return ob;
    }
}

ZC.PrinterTonerPanel = Ext.extend(ZC.ComponentGridPanel, {
    constructor: function(config) {
        config = Ext.applyIf(config||{}, {
            componentType: 'PrinterToner',
            fields: [
                {name: 'uid'},
                {name: 'name'},
                {name: 'severity'},
                {name: 'status'},
                {name: 'hasMonitor'},
                {name: 'monitor'},
                {name: 'tonerName'},
                {name: 'currentToner'},
                {name: 'maxToner'},
                {name: 'cartType'},
                {name: 'cartUnit'}
            ],
            columns: [{
                id: 'severity',
                dataIndex: 'severity',
                header: _t('Events'),
                renderer: Zenoss.render.severity,
                width: 60
            },{
                id: 'name',
                dataIndex: 'name',
                header: _t('Name'),
                sortable: true,
                width:150
            },{
                id: 'tonerName',
                dataIndex: 'tonerName',
                header: _t('Toner Name'),
                sortable: true,
                width:150
            },{
                id: 'cartType',
                dataIndex: 'cartType',
                header: _t('Cartridge Type'),
                sortable: true,
                width: 200
            },{
                id: 'maxToner',
                dataIndex: 'maxToner',
                header: _t('Max Toner'),
                sortable: true,
                width: 100
            }
            ]
        });
        ZC.PrinterTonerPanel.superclass.constructor.call(this, config);
    }
});


Ext.reg('PrinterTonerPanel', ZC.PrinterTonerPanel);
ZC.registerName('PrinterToner', _t('Printer Toner'), _t('Printer Toners'));
})();


