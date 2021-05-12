# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QObject, pyqtSlot
import os


class Ui_Upldr(QObject):
    def setupUi(self, Upldr):
        Upldr.setObjectName("Upldr")
        Upldr.resize(896, 588)
        self.centralwidget = QtWidgets.QWidget(Upldr)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.uploadFrame = QtWidgets.QFrame(self.centralwidget)
        self.uploadFrame.setEnabled(True)
        self.uploadFrame.setMinimumSize(QtCore.QSize(100, 25))
        self.uploadFrame.setBaseSize(QtCore.QSize(250, 30))
        self.uploadFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.uploadFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.uploadFrame.setObjectName("uploadFrame")
        self.gridLayout = QtWidgets.QGridLayout(self.uploadFrame)
        self.gridLayout.setObjectName("gridLayout")
        self.fileNameLabel = QtWidgets.QLabel(self.uploadFrame)
        self.fileNameLabel.setObjectName("fileNameLabel")
        self.gridLayout.addWidget(self.fileNameLabel, 0, 0, 1, 1)
        self.fileNameEdit = QtWidgets.QLineEdit(self.uploadFrame)
        self.fileNameEdit.setObjectName("fileNameEdit")
        self.gridLayout.addWidget(self.fileNameEdit, 0, 1, 1, 1)
        self.browseButton = QtWidgets.QPushButton(self.uploadFrame)
        self.browseButton.setObjectName("browseButton")
        self.gridLayout.addWidget(self.browseButton, 0, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.uploadFrame)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.categoryLine = QtWidgets.QLineEdit(self.uploadFrame)
        self.categoryLine.setObjectName("categoryLine")
        self.gridLayout.addWidget(self.categoryLine, 1, 1, 1, 2)
        self.label_3 = QtWidgets.QLabel(self.uploadFrame)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.tagLine = QtWidgets.QLineEdit(self.uploadFrame)
        self.tagLine.setObjectName("tagLine")
        self.gridLayout.addWidget(self.tagLine, 2, 1, 1, 2)
        self.uploadButton = QtWidgets.QPushButton(self.uploadFrame)
        self.uploadButton.setObjectName("uploadButton")
        self.gridLayout.addWidget(self.uploadButton, 3, 2, 1, 1)
        self.gridLayout_2.addWidget(self.uploadFrame, 0, 0, 1, 1)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.outputTextBrowser = QtWidgets.QTextBrowser(self.frame)
        self.outputTextBrowser.setObjectName("outputTextBrowser")
        self.gridLayout_3.addWidget(self.outputTextBrowser, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.frame, 1, 0, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_2, 0, 0, 1, 1)
        Upldr.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Upldr)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 896, 21))
        self.menubar.setObjectName("menubar")
        self.menuUpldr = QtWidgets.QMenu(self.menubar)
        self.menuUpldr.setObjectName("menuUpldr")
        Upldr.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Upldr)
        self.statusbar.setObjectName("statusbar")
        Upldr.setStatusBar(self.statusbar)
        self.actionSettings = QtWidgets.QAction(Upldr)
        self.actionSettings.setObjectName("actionSettings")
        self.menuUpldr.addAction(self.actionSettings)
        self.menubar.addAction(self.menuUpldr.menuAction())

        self.retranslateUi(Upldr)
        self.browseButton.clicked.connect(self.browseSlot)
        self.uploadButton.clicked.connect(self.uploadSlot)
        self.fileNameEdit.returnPressed.connect(self.returnPressedSlot)
        self.actionSettings.triggered.connect(self.openSettingsSlot)
        QtCore.QMetaObject.connectSlotsByName(Upldr)

    def retranslateUi(self, Upldr):
        _translate = QtCore.QCoreApplication.translate
        Upldr.setWindowTitle(_translate("Upldr", "Upldr"))
        self.fileNameLabel.setText(_translate("Upldr", "File Name"))
        self.browseButton.setText(_translate("Upldr", "Browse"))
        self.label_2.setText(_translate("Upldr", "Category"))
        self.label_3.setText(_translate("Upldr", "Tag"))
        self.uploadButton.setText(_translate("Upldr", "Upload"))
        self.menuUpldr.setTitle(_translate("Upldr", "Upldr"))
        self.actionSettings.setText(_translate("Upldr", "Settings"))

    @pyqtSlot()
    def returnPressedSlot(self):
        pass

    @pyqtSlot()
    def uploadSlot(self):
        pass

    @pyqtSlot()
    def browseSlot(self):
        pass

    @pyqtSlot()
    def openSettingsSlot(self):
        pass


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Upldr = QtWidgets.QMainWindow()
    ui = Ui_Upldr()
    ui.setupUi(Upldr)
    Upldr.show()
    sys.exit(app.exec_())
