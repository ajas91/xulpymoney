#!/usr/bin/python3
import sys,  os
import platform

if platform.system()=="Windows":
    sys.path.append("ui/")
    sys.path.append("images/")
else:
    sys.path.append("/usr/lib/xulpymoney")

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from frmInit import *

try:
    os.makedirs( os.environ['HOME']+"/.xulpymoney/")
except:
    pass

app = QApplication(sys.argv)
app.setOrganizationName("Mariano Muñoz ©")
app.setOrganizationDomain("turulomio.users.sourceforge.net")
app.setApplicationName("Xulpymoney")

translator = QTranslator(app)
locale=QLocale()
a=locale.system().name()
if len(a)!=2:
    a=a[:-len(a)+2]
s= QApplication.translate("Core",  "Local language detected:{0}").format(a)
print (s)
if platform.system()=="Windows":
    translator.load("i18n/xulpymoney_{0}.qm".format(a))
else:
    translator.load("/usr/lib/xulpymoney/xulpymoney_{0}.qm".format(a))
app.installTranslator(translator)

frm = frmInit() 
frm.show()

sys.exit(app.exec_())
