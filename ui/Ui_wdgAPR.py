# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/wdgAPR.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_wdgAPR(object):
    def setupUi(self, wdgAPR):
        wdgAPR.setObjectName("wdgAPR")
        wdgAPR.resize(1199, 447)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(wdgAPR.sizePolicy().hasHeightForWidth())
        wdgAPR.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/xulpymoney/history.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        wdgAPR.setWindowIcon(icon)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(wdgAPR)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.lbl = QtWidgets.QLabel(wdgAPR)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lbl.setFont(font)
        self.lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl.setObjectName("lbl")
        self.verticalLayout.addWidget(self.lbl)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.wdgYear = wdgYear(wdgAPR)
        self.wdgYear.setObjectName("wdgYear")
        self.horizontalLayout_4.addWidget(self.wdgYear)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.tab = QtWidgets.QTabWidget(wdgAPR)
        self.tab.setObjectName("tab")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.tab_5)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.table = myQTableWidget(self.tab_5)
        self.table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.table.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.table.setObjectName("table")
        self.table.setColumnCount(10)
        self.table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(9, item)
        self.table.verticalHeader().setVisible(False)
        self.horizontalLayout.addWidget(self.table)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/xulpymoney/document-edit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tab.addTab(self.tab_5, icon1, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.tab_2)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tblReport = myQTableWidget(self.tab_2)
        self.tblReport.setObjectName("tblReport")
        self.tblReport.setColumnCount(10)
        self.tblReport.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tblReport.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblReport.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblReport.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblReport.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblReport.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblReport.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblReport.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblReport.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblReport.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblReport.setHorizontalHeaderItem(9, item)
        self.tblReport.verticalHeader().setVisible(False)
        self.verticalLayout_2.addWidget(self.tblReport)
        self.lblReport = QtWidgets.QLabel(self.tab_2)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lblReport.setFont(font)
        self.lblReport.setText("")
        self.lblReport.setAlignment(QtCore.Qt.AlignCenter)
        self.lblReport.setObjectName("lblReport")
        self.verticalLayout_2.addWidget(self.lblReport)
        self.horizontalLayout_5.addLayout(self.verticalLayout_2)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/xulpymoney/coins.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tab.addTab(self.tab_2, icon2, "")
        self.verticalLayout.addWidget(self.tab)
        self.horizontalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(wdgAPR)
        self.tab.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(wdgAPR)

    def retranslateUi(self, wdgAPR):
        _translate = QtCore.QCoreApplication.translate
        self.lbl.setText(_translate("wdgAPR", "Assets report"))
        item = self.table.horizontalHeaderItem(0)
        item.setText(_translate("wdgAPR", "Year"))
        item = self.table.horizontalHeaderItem(1)
        item.setText(_translate("wdgAPR", "Initial balance"))
        item = self.table.horizontalHeaderItem(2)
        item.setText(_translate("wdgAPR", "Final balance"))
        item = self.table.horizontalHeaderItem(3)
        item.setText(_translate("wdgAPR", "Difference"))
        item = self.table.horizontalHeaderItem(4)
        item.setText(_translate("wdgAPR", "Incomes"))
        item = self.table.horizontalHeaderItem(5)
        item.setText(_translate("wdgAPR", "Net gains"))
        item = self.table.horizontalHeaderItem(6)
        item.setText(_translate("wdgAPR", "Net dividends"))
        item = self.table.horizontalHeaderItem(7)
        item.setText(_translate("wdgAPR", "Expenses"))
        item = self.table.horizontalHeaderItem(8)
        item.setText(_translate("wdgAPR", "I+G+D-E"))
        item = self.table.horizontalHeaderItem(9)
        item.setText(_translate("wdgAPR", "% APR"))
        self.tab.setTabText(self.tab.indexOf(self.tab_5), _translate("wdgAPR", "Assets report"))
        item = self.tblReport.horizontalHeaderItem(0)
        item.setText(_translate("wdgAPR", "Year"))
        item = self.tblReport.horizontalHeaderItem(1)
        item.setText(_translate("wdgAPR", "Invested balance"))
        item = self.tblReport.horizontalHeaderItem(2)
        item.setText(_translate("wdgAPR", "Investment valoration"))
        item = self.tblReport.horizontalHeaderItem(3)
        item.setText(_translate("wdgAPR", "Diff"))
        item = self.tblReport.horizontalHeaderItem(4)
        item.setText(_translate("wdgAPR", "%"))
        item = self.tblReport.horizontalHeaderItem(6)
        item.setText(_translate("wdgAPR", "Net Gains + Dividends"))
        item = self.tblReport.horizontalHeaderItem(8)
        item.setText(_translate("wdgAPR", "Taxes"))
        item = self.tblReport.horizontalHeaderItem(9)
        item.setText(_translate("wdgAPR", "Comissions"))
        self.tab.setTabText(self.tab.indexOf(self.tab_2), _translate("wdgAPR", "Invested report"))

from myqtablewidget import myQTableWidget
from wdgYear import wdgYear
import xulpymoney_rc
