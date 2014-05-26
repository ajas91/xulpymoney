
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from Ui_frmAccountOperationsAdd import *
from libxulpymoney import *

class frmAccountOperationsAdd(QDialog, Ui_frmAccountOperationsAdd):
    def __init__(self, mem, cuentas, cuenta, opercuenta=None, tarjeta=None ,  opertarjeta=None ,  parent=None):
        """TIPOS DE ENTRADAS:        
         1   selAccount=x: Inserción de Opercuentas y edición de cuentas
         2   selAccount=x, selMovimiento=x Modificación de opercuentas
         3   selAccount=x, selMovimiento=x , tarjeta=x, Inserción de opertarjetas
         4   selAccount=x, selMovimiento=x , tarjeta=x, opertarjeta Modificación de opertarjetas"""
        QWidget.__init__(self, parent)
        self.setupUi(self)
        self.mem=mem
        
        self.cuenta=cuenta
        self.opercuenta=opercuenta
        self.tarjeta=tarjeta
        self.opertarjeta=opertarjeta
        self.mem.data.cuentas_active=cuentas

        self.mem.conceptos.load_opercuentas_qcombobox(self.cmbConcepts)
        self.mem.data.cuentas_active.qcombobox(self.cmbAccounts)

        if opertarjeta!=None:
            self.setWindowTitle(self.trUtf8("Modificación de una operación de tarjeta"))
            self.lblTitulo.setText(self.trUtf8("Modificación de un operación de tarjeta"))
            self.cmbAccounts.hide()
            self.tipo=4            
            self.calendar.setSelectedDate(self.opertarjeta.fecha)
            self.cmbConcepts.setCurrentIndex(self.cmbConcepts.findData(self.opertarjeta.concepto.id))
            self.cmbAccounts.setCurrentIndex(self.cmbAccounts.findData(self.opertarjeta.tarjeta.cuenta.id))
            self.txtImporte.setText(str(self.opertarjeta.importe))
            self.txtComentario.setText(self.opertarjeta.comentario)
        elif tarjeta!=None:
            self.setWindowTitle(self.trUtf8("Nueva operación de tarjeta"))
            self.lblTitulo.setText(self.trUtf8("Nueva operación de tarjeta"))
            self.cmbAccounts.hide()
            self.tipo=3
        elif self.opercuenta!=None:
            self.tipo=2
            self.setWindowTitle(self.trUtf8("Modificación de un movimiento de cuenta"))
            self.lblTitulo.setText(self.trUtf8("Modificación de un movimiento de cuenta"))
            self.calendar.setSelectedDate(self.opercuenta.fecha)
            self.cmbConcepts.setCurrentIndex(self.cmbConcepts.findData(self.opercuenta.concepto.id))
            self.cmbAccounts.setCurrentIndex(self.cmbAccounts.findData(self.opercuenta.cuenta.id))
            self.txtImporte.setText(str(self.opercuenta.importe))
            self.txtComentario.setText((self.opercuenta.comentario))    
        else:
            self.tipo=1
            self.setWindowTitle(self.trUtf8("Nuevo movimiento de cuenta"))
            self.lblTitulo.setText(self.trUtf8("Nuevo movimiento de cuenta"))
            self.cmbAccounts.setCurrentIndex(self.cmbAccounts.findData(self.cuenta.id))

        
    def on_cmd_released(self):
        fecha=self.calendar.selectedDate().toPyDate()
        concepto=self.mem.conceptos.find(self.cmbConcepts.itemData(self.cmbConcepts.currentIndex()))
        importe=self.txtImporte.decimal()
        comentario=self.txtComentario.text()
        id_cuentas=self.cmbAccounts.itemData(self.cmbAccounts.currentIndex()) #Sólo se usará en 1 y 2.
        
        if concepto.tipooperacion.id==1 and importe>0:
            m=QMessageBox()
            m.setIcon(QMessageBox.Information)
            m.setText(self.trUtf8("Un gasto no puede tener un importe positivo"))
            m.exec_()    
            return
            
        if concepto.tipooperacion.id==2 and importe<0:
            m=QMessageBox()
            m.setIcon(QMessageBox.Information)
            m.setText(self.trUtf8("Un ingreso no puede tener un importe negativo"))
            m.exec_()
            return
                    
        if self.tipo==1:
            self.opercuenta=AccountOperation(self.mem)
            self.opercuenta.cuenta=self.cuenta
            self.opercuenta.fecha=fecha
            self.opercuenta.concepto=concepto
            self.opercuenta.tipooperacion=concepto.tipooperacion
            self.opercuenta.importe=importe
            self.opercuenta.comentario=comentario
            self.opercuenta.cuenta=self.mem.data.cuentas_active.find(id_cuentas)#Se puede cambiar
            self.opercuenta.save()
            self.mem.con.commit()        #Se debe hacer el commit antes para que al actualizar con el signal salga todos los datos
            self.emit(SIGNAL("OperAccountIBMed"), ())
        elif self.tipo==2:            
            self.opercuenta.fecha=fecha
            self.opercuenta.concepto=concepto
            self.opercuenta.tipooperacion=concepto.tipooperacion
            self.opercuenta.importe=importe
            self.opercuenta.comentario=comentario
            self.opercuenta.cuenta=self.mem.data.cuentas_active.find(id_cuentas)#Se puede cambiar
            self.opercuenta.save()
            self.mem.con.commit()        #Se debe hacer el commit antes para que al actualizar con el signal salga todos los datos
            self.emit(SIGNAL("OperAccountIBMed"), ())
            self.done(0)
        elif self.tipo==3:
            self.opertarjeta=CreditCardOperation(self.mem).init__create(fecha, concepto, concepto.tipooperacion, importe, comentario, self.tarjeta, False, None, None )
            self.opertarjeta.save()
            self.mem.con.commit()        
            self.tarjeta.op_diferido.append(self.opertarjeta)
            self.emit(SIGNAL("OperCreditCardIBMed"), (True))
        elif self.tipo==4:            
            self.opertarjeta.fecha=fecha
            self.opertarjeta.concepto=concepto
            self.opertarjeta.tipooperacion=concepto.tipooperacion
            self.opertarjeta.importe=importe
            self.opertarjeta.comentario=comentario
            self.opertarjeta.save()
            self.mem.con.commit()        #Se debe hacer el commit antes para que al actualizar con el signal salga todos los datos
            self.emit(SIGNAL("OperCreditCardIBMed"), ())
            self.done(0)            
        self.cuenta.saldo_from_db()
    