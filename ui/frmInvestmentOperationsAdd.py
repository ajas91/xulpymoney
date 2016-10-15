from PyQt5.QtCore import *
from PyQt5.QtGui import *
from libxulpymoney import *
from frmProductReport import *
from Ui_frmInvestmentOperationsAdd import *

class frmInvestmentOperationsAdd(QDialog, Ui_frmInvestmentOperationsAdd):
    def __init__(self, mem, inversion, operinversion,   parent=None):
        QWidget.__init__(self, parent)
        self.setupUi(self)
        self.mem=mem
        self.inversion=inversion
        self.operinversion=operinversion
  
        self.wdgDT.show_microseconds(False)
        self.lblValorAccion.setText(self.tr("Price in {}".format(self.inversion.product.currency.symbol)))
        self.lblConversion.setText(self.tr("Price converted to {}".format(self.inversion.account.currency.symbol)))
        if self.inversion.product.currency==self.inversion.account.currency:
            self.lblConversion.hide()
            self.wdgCurrencyConversion.hide()
        
        if self.operinversion==None:#nuevo movimiento
            self.type=1
            self.operinversion=InvestmentOperation(self.mem)
            self.operinversion.inversion=self.inversion
            self.lblTitulo.setText(self.tr("New operation of {}").format(self.inversion.name))
            self.mem.tiposoperaciones.qcombobox_investments_operations(self.cmbTiposOperaciones)
            self.wdgDT.set(self.mem)
            self.wdgCurrencyConversion.setConversion(Money(self.mem, self.txtValorAccion.decimal(), self.inversion.product.currency), self.inversion.account.currency, self.wdgDT.datetime(), None)
        else:#editar movimiento
            self.type=2
            self.lblTitulo.setText(self.tr("{} operation edition").format(self.inversion.name))
            self.mem.tiposoperaciones.qcombobox_investments_operations(self.cmbTiposOperaciones, self.operinversion.tipooperacion)
            self.wdgDT.set(self.mem, self.operinversion.datetime, self.mem.localzone)
            self.wdgCurrencyConversion.setConversion(Money(self.mem, self.txtValorAccion.decimal(), self.inversion.product.currency), self.inversion.account.currency, self.wdgDT.datetime(), self.operinversion.currency_conversion)
            self.txtImporte.setText(self.operinversion.importe)
            self.txtImpuestos.setText(self.operinversion.impuestos)
            self.txtComision.setText(self.operinversion.comision)
            self.txtValorAccion.setText(self.operinversion.valor_accion)
            self.txtAcciones.setText(self.operinversion.acciones)
    def on_cmd_released(self):        
        id_tiposoperaciones=int(self.cmbTiposOperaciones.itemData(self.cmbTiposOperaciones.currentIndex()))
        self.operinversion.tipooperacion=self.mem.tiposoperaciones.find_by_id(id_tiposoperaciones)
        self.operinversion.impuestos=self.txtImpuestos.decimal()
        self.operinversion.comision=self.txtComision.decimal()
        self.operinversion.valor_accion=self.txtValorAccion.decimal()
        self.operinversion.currency_conversion=self.wdgCurrencyConversion.factor
        self.operinversion.acciones=self.txtAcciones.decimal()
        if id_tiposoperaciones==5: #Venta
            self.operinversion.importe=self.txtImporteBruto.decimal()
            self.operinversion.show_in_ranges=False
            if self.operinversion.acciones>Decimal('0'):
                m=QMessageBox()
                m.setWindowIcon(QIcon(":/xulpymoney/coins.png"))
                m.setIcon(QMessageBox.Information)
                m.setText(self.tr("Sale Shares number must be negative"))
                m.exec_()    
                return        
        elif id_tiposoperaciones==4: #Compra
            self.operinversion.importe=self.txtImporte.decimal()
            if self.operinversion.acciones<0: 
                m=QMessageBox()
                m.setWindowIcon(QIcon(":/xulpymoney/coins.png"))
                m.setIcon(QMessageBox.Information)
                m.setText(self.tr("Purchase shares number must be positive"))
                m.exec_()    
                return
        elif id_tiposoperaciones==6: #Añadido    
            self.operinversion.importe=self.txtImporte.decimal()
            if self.operinversion.acciones<0: 
                m=QMessageBox()
                m.setWindowIcon(QIcon(":/xulpymoney/coins.png"))
                m.setIcon(QMessageBox.Information)
                m.setText(self.tr("Added shares number must be positive"))
                m.exec_()    
                return            
        elif id_tiposoperaciones==8: #Traspaso fondos
            self.operinversion.importe=self.txtImporte.decimal()
        
        if self.operinversion.impuestos<Decimal('0') or  self.operinversion.comision<Decimal('0') or self.operinversion.valor_accion<Decimal('0'):            
            m=QMessageBox()
            m.setWindowIcon(QIcon(":/xulpymoney/coins.png"))
            m.setIcon(QMessageBox.Information)
            m.setText(self.tr("Share price, taxes and comission must be positive amounts"))
            m.exec_()    
            return
            
        self.operinversion.datetime=self.wdgDT.datetime()
        self.operinversion.save()    
        self.mem.con.commit()#Guarda todos los cambios en bd.
        
        ##Mete indice referencia.
        if self.type==1  and id_tiposoperaciones==4:#Añadir y compra
            w=frmQuotesIBM(self.mem, self.mem.data.benchmark, None, self)
            #Quita un minuto para que enganche con operación
            w.wdgDT.set(self.mem, self.wdgDT.datetime()-datetime.timedelta(seconds=1), self.mem.localzone)
            w.chkCanBePurged.setCheckState(Qt.Unchecked)
            w.txtQuote.setFocus()
            w.exec_() 
            self.mem.data.benchmark.result.basic.load_from_db()                
        self.done(0)

    def on_cmbTiposOperaciones_currentIndexChanged(self, index):
        id_tiposoperaciones=int(self.cmbTiposOperaciones.itemData(self.cmbTiposOperaciones.currentIndex()))
        if id_tiposoperaciones==6:#Añadido acciones
            self.txtValorAccion.setText(0)
            self.txtValorAccion.setEnabled(False)
        else:
            self.txtValorAccion.setEnabled(True)
        self.on_txtAcciones_textChanged()
            
    def on_txtAcciones_textChanged(self):
        """El importe a grabar en BD cuando es una compra es el importe neto, cuando es una venta es el importe bruto"""
        id_tiposoperaciones=int(self.cmbTiposOperaciones.itemData(self.cmbTiposOperaciones.currentIndex()))
        try:
            if id_tiposoperaciones==4:#Compra
                importe=abs(round(self.txtAcciones.decimal()*self.txtValorAccion.decimal(), 2))
                self.txtImporte.setText(importe)
                self.txtImporteBruto.setText(importe+self.txtComision.decimal()+self.txtImpuestos.decimal())
            if id_tiposoperaciones==5:#Venta
                importe=abs(round(self.txtAcciones.decimal()*self.txtValorAccion.decimal(), 2))
                self.txtImporte.setText(importe-self.txtComision.decimal()-self.txtImpuestos.decimal())
                self.txtImporteBruto.setText(importe)
            if id_tiposoperaciones==8:#Traspaso
                importe=abs(round(self.txtAcciones.decimal()*self.txtValorAccion.decimal(), 2))
                self.txtImporte.setText(importe)
                self.txtImporteBruto.setText(importe+self.txtComision.decimal()+self.txtImpuestos.decimal())
        except:
            pass
        
        
    def on_txtValorAccion_textChanged(self):
        self.wdgCurrencyConversion.setConversion(Money(self.mem, self.txtValorAccion.decimal(), self.inversion.product.currency), self.inversion.account.currency, self.wdgDT.datetime(), self.wdgCurrencyConversion.factor)
        self.on_txtAcciones_textChanged()
        
    def on_txtComision_textChanged(self):
        self.on_txtAcciones_textChanged()
        
    def on_txtImpuestos_textChanged(self):
        self.on_txtAcciones_textChanged()
