# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'xulpymoney/ui/wdgQuotesSaveResult.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_wdgQuotesSaveResult(object):
    def setupUi(self, wdgQuotesSaveResult):
        wdgQuotesSaveResult.setObjectName("wdgQuotesSaveResult")
        wdgQuotesSaveResult.resize(751, 585)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(wdgQuotesSaveResult)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.lbl = QtWidgets.QLabel(wdgQuotesSaveResult)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lbl.setFont(font)
        self.lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl.setObjectName("lbl")
        self.verticalLayout.addWidget(self.lbl)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.label = QtWidgets.QLabel(wdgQuotesSaveResult)
        self.label.setMaximumSize(QtCore.QSize(64, 64))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/xulpymoney/save.png"))
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.tab = QtWidgets.QTabWidget(wdgQuotesSaveResult)
        self.tab.setObjectName("tab")
        self.tabAdded = QtWidgets.QWidget()
        self.tabAdded.setObjectName("tabAdded")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.tabAdded)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.mqtwAdded = mqtwObjects(self.tabAdded)
        self.mqtwAdded.setObjectName("mqtwAdded")
        self.horizontalLayout_3.addWidget(self.mqtwAdded)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/xulpymoney/save.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tab.addTab(self.tabAdded, icon, "")
        self.tabUpdated = QtWidgets.QWidget()
        self.tabUpdated.setObjectName("tabUpdated")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.tabUpdated)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.mqtwUpdated = mqtwObjects(self.tabUpdated)
        self.mqtwUpdated.setObjectName("mqtwUpdated")
        self.horizontalLayout_4.addWidget(self.mqtwUpdated)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/xulpymoney/editar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tab.addTab(self.tabUpdated, icon1, "")
        self.tabIgnored = QtWidgets.QWidget()
        self.tabIgnored.setObjectName("tabIgnored")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.tabIgnored)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.mqtwIgnored = mqtwObjects(self.tabIgnored)
        self.mqtwIgnored.setObjectName("mqtwIgnored")
        self.horizontalLayout_5.addWidget(self.mqtwIgnored)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/xulpymoney/study.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tab.addTab(self.tabIgnored, icon2, "")
        self.tabErrors = QtWidgets.QWidget()
        self.tabErrors.setObjectName("tabErrors")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.tabErrors)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.mqtwErrors = mqtwObjects(self.tabErrors)
        self.mqtwErrors.setObjectName("mqtwErrors")
        self.horizontalLayout_6.addWidget(self.mqtwErrors)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/xulpymoney/button_cancel.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tab.addTab(self.tabErrors, icon3, "")
        self.verticalLayout.addWidget(self.tab)
        self.horizontalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(wdgQuotesSaveResult)
        self.tab.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(wdgQuotesSaveResult)

    def retranslateUi(self, wdgQuotesSaveResult):
        _translate = QtCore.QCoreApplication.translate
        wdgQuotesSaveResult.setWindowTitle(_translate("wdgQuotesSaveResult", "Form"))
        self.lbl.setText(_translate("wdgQuotesSaveResult", "Report of saved quotes"))
        self.tab.setTabText(self.tab.indexOf(self.tabAdded), _translate("wdgQuotesSaveResult", "Added"))
        self.tab.setTabText(self.tab.indexOf(self.tabUpdated), _translate("wdgQuotesSaveResult", "Updated"))
        self.tab.setTabText(self.tab.indexOf(self.tabIgnored), _translate("wdgQuotesSaveResult", "Ignored"))
        self.tab.setTabText(self.tab.indexOf(self.tabErrors), _translate("wdgQuotesSaveResult", "Errors"))
from xulpymoney.ui.myqtablewidget import mqtwObjects
import xulpymoney.images.xulpymoney_rc
