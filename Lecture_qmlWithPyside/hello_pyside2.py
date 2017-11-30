#-'''- coding: utf-8 -'''-

import sys
from PySide2 import QtCore, QtGui, QtQuick

app = QtGui.QGuiApplication(sys.argv)
view = QtQuick.QQuickView()
url = QtCore.QUrl('qml/helloworld.qml')
view.setSource(url)
view.show()
sys.exit(app.exec_())
