from PyQt5.QtCore import Qt, pyqtSlot
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMenu, QWidget
from datetime import date
from xulpymoney.libxulpymoney import Money, Percentage
from xulpymoney.libxulpymoneyfunctions import qmessagebox
from xulpymoney.ui.Ui_wdgDividendsReport import Ui_wdgDividendsReport
from xulpymoney.ui.frmInvestmentReport import frmInvestmentReport
from xulpymoney.ui.frmProductReport import frmProductReport
from xulpymoney.ui.frmEstimationsAdd import frmEstimationsAdd

class wdgDividendsReport(QWidget, Ui_wdgDividendsReport):
    def __init__(self, mem,  parent=None):
        QWidget.__init__(self, parent)
        self.setupUi(self)
        self.mem=mem
        self.investmentes=[]

        self.tblInvestments.settings(self.mem, "wdgDividendsReport")
        
        self.on_chkInactivas_stateChanged(Qt.Unchecked)

    @pyqtSlot()  
    def on_actionEstimationDPSEdit_triggered(self):
        d=frmEstimationsAdd(self.mem, self.selInvestment.product, "dps")
        d.exec_()
        self.on_chkInactivas_stateChanged(self.chkInactivas.checkState())
        self.tblInvestments.clearSelection()

    def on_chkInactivas_stateChanged(self,  state):               
        if state==Qt.Checked:
             
            self.investmentes=self.mem.data.investments_inactive()
        else:
            self.investmentes=self.mem.data.investments_active()
        self.load_inversiones()
        
    def load_inversiones(self):    
        if self.investmentes.order_by_dividend()==False:
            qmessagebox(self.tr("I couldn't order data due to they have null values"))     
        
        self.tblInvestments.applySettings()
        self.tblInvestments.clearContents()
        self.tblInvestments.setRowCount(len(self.investmentes.arr));
        rows=[]
        for i, inv in enumerate(self.investmentes.arr):
            if inv.product.estimations_dps.find(date.today().year)==None:
                dpa=0
                tpc=Percentage()
                divestimado=Money(self.mem, 0, self.mem.localcurrency)
            else:
                dpa=inv.product.estimations_dps.currentYear().estimation
                tpc=inv.product.estimations_dps.currentYear().percentage()
                divestimado=inv.dividend_bruto_estimado().local()
            row=[]
            row.append(inv.name)
            row.append(inv.account.eb.name)
            row.append(inv.product.result.basic.last.quote)
            row.append(dpa)
            row.append(inv.shares())
            row.append(divestimado)
            row.append(tpc)
            rows.append(row)
               
            #Colorea si está desactualizado
            if inv.product.estimations_dps.dias_sin_actualizar()>self.spin.value():
                self.tblInvestments.item(i, 3).setIcon(QIcon(":/xulpymoney/alarm_clock.png"))
        self.tblInvestments.fillFromListOfRows(rows,  decimals=[0, 0, 6, 6, 6, 2, 2])
        self.lblTotal.setText(self.tr("If I keep this investment during a year, I'll get {0}").format( self.sum_of_estimated_dividends()))
        
    ## Reused in AssestsReport
    def sum_of_estimated_dividends(self):
        sumdiv=Money(self.mem, 0, self.mem.localcurrency)
        for i, inv in enumerate(self.investmentes.arr):
            if inv.product.estimations_dps.find(date.today().year)!=None:
                sumdiv=sumdiv+inv.dividend_bruto_estimado().local()
        return sumdiv
        
            
        
    @pyqtSlot() 
    def on_actionInvestmentReport_triggered(self):
        w=frmInvestmentReport(self.mem, self.selInvestment, self)
        w.exec_()
        self.on_chkInactivas_stateChanged(self.chkInactivas.checkState())

            
    @pyqtSlot() 
    def on_actionProductReport_triggered(self):
        w=frmProductReport(self.mem, self.selInvestment.product, self.selInvestment, self)
        w.exec_()
        self.on_chkInactivas_stateChanged(self.chkInactivas.checkState())

                    
    def on_cmd_pressed(self):
        self.on_chkInactivas_stateChanged(self.chkInactivas.checkState())

    def on_tblInvestments_customContextMenuRequested(self,  pos):        
        menu=QMenu()
        menu.addAction(self.actionEstimationDPSEdit)
        menu.addSeparator()
        menu.addAction(self.actionInvestmentReport) 
        menu.addAction(self.actionProductReport)    
        menu.exec_(self.tblInvestments.mapToGlobal(pos))

    def on_tblInvestments_itemSelectionChanged(self):
        self.selInvestment=None
        for i in self.tblInvestments.selectedItems():#itera por cada item no row.
            self.selInvestment=self.investmentes.arr[i.row()]
        print ("Seleccionado: " +  str(self.selInvestment))

