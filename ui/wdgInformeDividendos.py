from PyQt4.QtCore import *
from PyQt4.QtGui import *
import datetime
from core import *
from Ui_wdgInformeDividendos import *
from frmInversionesEstudio import *
from frmDividendoEstimacionIBM import *

class wdgInformeDividendos(QWidget, Ui_wdgInformeDividendos):
    def __init__(self, cfg,  parent=None):
        QWidget.__init__(self, parent)
        self.setupUi(self)
        self.cfg=cfg
        self.inversiones=[]

        self.tblInversiones.settings("wdgInformeDividendos",  self.cfg.inifile)
        
        self.on_chkInactivas_stateChanged(Qt.Unchecked)

    @QtCore.pyqtSlot()  
    def on_actionModificarDPA_activated(self):
        d=frmDividendoEstimacionIBM(self.cfg, self.selInversion)
        d.exec_()
        self.selInversion.mq.estimaciones[d.txtYear.text()].dpa=d.txtDPA.text()
        self.on_chkInactivas_stateChanged(self.chkInactivas.checkState())
        self.tblInversiones.clearSelection()

    def on_chkInactivas_stateChanged(self,  state):               
        if state==Qt.Checked:
            self.inversiones=self.cfg.inversiones_activas(False)
        else:
            self.inversiones=self.cfg.inversiones_activas(True)
        self.load_inversiones()
        
    def load_inversiones(self):    
        self.inversiones=sorted(self.inversiones, key=lambda inv: inv.mq.estimaciones[str(datetime.date.today().year)].tpc_dpa(),  reverse=True) 

        self.tblInversiones.clearContents()
        self.tblInversiones.setRowCount(len(self.inversiones));
        sumdiv=Decimal(0)
        for i, inv in enumerate(self.inversiones):
            estimacion=inv.mq.estimaciones[str(datetime.date.today().year)]
            self.tblInversiones.setItem(i, 0,QTableWidgetItem(inv.name))
            self.tblInversiones.setItem(i, 1, QTableWidgetItem(inv.cuenta.eb.name))
            self.tblInversiones.setItem(i, 2, inv.mq.currency.qtablewidgetitem(inv.mq.quotes.last.quote))
            self.tblInversiones.setItem(i, 3, inv.mq.currency.qtablewidgetitem(estimacion.dpa))    
            self.tblInversiones.setItem(i, 4, qright(str(inv.acciones())))
            divestimado=inv.dividendo_bruto_estimado()
            sumdiv=sumdiv+divestimado
            self.tblInversiones.setItem(i, 5, inv.mq.currency.qtablewidgetitem(divestimado))
            self.tblInversiones.setItem(i, 6, qtpc(estimacion.tpc_dpa()))
                
            #Colorea si está desactualizado
            try:
                diassinactualizar=(datetime.date.today()-estimacion.fechaestimacion).days
            except:
                diassinactualizar=0
            if diassinactualizar>self.spin.value() or estimacion.fechaestimacion==None:
                self.tblInversiones.item(i, 3).setBackgroundColor(QColor(255, 146, 148))
        self.lblTotal.setText(self.trUtf8("Si mantuviera la inversión un año obtendría {0} €".format(sumdiv) ))
            
        
    @QtCore.pyqtSlot() 
    def on_actionInversionEstudio_activated(self):
        w=frmInversionesEstudio(self.cfg, self.selInversion)
        w.exec_()
        
    def on_cmd_pressed(self):
            self.on_chkInactivas_stateChanged(self.chkInactivas.checkState())

    def on_tblInversiones_customContextMenuRequested(self,  pos):        
        menu=QMenu()
        menu.addAction(self.actionModificarDPA)
        menu.addAction(self.actionInversionEstudio)    
        menu.exec_(self.tblInversiones.mapToGlobal(pos))

    def on_tblInversiones_itemSelectionChanged(self):
        self.selInversion=None
        for i in self.tblInversiones.selectedItems():#itera por cada item no row.
            self.selInversion=self.inversiones[i.row()]
        print ("Seleccionado: " +  str(self.selInversion))
