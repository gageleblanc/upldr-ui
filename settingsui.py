# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\settings.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_UpldrSettings(object):
    def setupUi(self, UpldrSettings):
        UpldrSettings.setObjectName("UpldrSettings")
        UpldrSettings.resize(800, 600)
        UpldrSettings.setMinimumSize(QtCore.QSize(800, 600))
        UpldrSettings.setBaseSize(QtCore.QSize(800, 600))
        self.gridLayout_4 = QtWidgets.QGridLayout(UpldrSettings)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.defaultRemoteBox = QtWidgets.QGroupBox(UpldrSettings)
        self.defaultRemoteBox.setObjectName("defaultRemoteBox")
        self.gridLayout = QtWidgets.QGridLayout(self.defaultRemoteBox)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.defaultRemoteBox)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.defaultRemoteNameEdit = QtWidgets.QLineEdit(self.defaultRemoteBox)
        self.defaultRemoteNameEdit.setEnabled(False)
        self.defaultRemoteNameEdit.setObjectName("defaultRemoteNameEdit")
        self.gridLayout.addWidget(self.defaultRemoteNameEdit, 0, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.defaultRemoteBox)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 2, 1, 1)
        self.defaultRemotePortEdit = QtWidgets.QLineEdit(self.defaultRemoteBox)
        self.defaultRemotePortEdit.setEnabled(False)
        self.defaultRemotePortEdit.setObjectName("defaultRemotePortEdit")
        self.gridLayout.addWidget(self.defaultRemotePortEdit, 0, 3, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.defaultRemoteBox)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.defaultRemoteSchemeEdit = QtWidgets.QLineEdit(self.defaultRemoteBox)
        self.defaultRemoteSchemeEdit.setEnabled(False)
        self.defaultRemoteSchemeEdit.setObjectName("defaultRemoteSchemeEdit")
        self.gridLayout.addWidget(self.defaultRemoteSchemeEdit, 1, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.defaultRemoteBox)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 1, 2, 1, 1)
        self.defaultRemoteTimeoutEdit = QtWidgets.QLineEdit(self.defaultRemoteBox)
        self.defaultRemoteTimeoutEdit.setEnabled(False)
        self.defaultRemoteTimeoutEdit.setObjectName("defaultRemoteTimeoutEdit")
        self.gridLayout.addWidget(self.defaultRemoteTimeoutEdit, 1, 3, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.defaultRemoteBox)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.defaultRemoteHostEdit = QtWidgets.QLineEdit(self.defaultRemoteBox)
        self.defaultRemoteHostEdit.setEnabled(False)
        self.defaultRemoteHostEdit.setObjectName("defaultRemoteHostEdit")
        self.gridLayout.addWidget(self.defaultRemoteHostEdit, 2, 1, 1, 1)
        self.gridLayout_4.addWidget(self.defaultRemoteBox, 0, 0, 1, 1)
        self.defaultRemoteBox_2 = QtWidgets.QGroupBox(UpldrSettings)
        self.defaultRemoteBox_2.setObjectName("defaultRemoteBox_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.defaultRemoteBox_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_6 = QtWidgets.QLabel(self.defaultRemoteBox_2)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 0, 0, 1, 1)
        self.newRemoteNameEdit = QtWidgets.QLineEdit(self.defaultRemoteBox_2)
        self.newRemoteNameEdit.setEnabled(True)
        self.newRemoteNameEdit.setObjectName("newRemoteNameEdit")
        self.gridLayout_2.addWidget(self.newRemoteNameEdit, 0, 1, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.defaultRemoteBox_2)
        self.label_9.setObjectName("label_9")
        self.gridLayout_2.addWidget(self.label_9, 0, 2, 1, 1)
        self.newRemotePortEdit = QtWidgets.QLineEdit(self.defaultRemoteBox_2)
        self.newRemotePortEdit.setEnabled(True)
        self.newRemotePortEdit.setObjectName("newRemotePortEdit")
        self.gridLayout_2.addWidget(self.newRemotePortEdit, 0, 3, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.defaultRemoteBox_2)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 1, 0, 1, 1)
        self.newRemoteSchemeEdit = QtWidgets.QLineEdit(self.defaultRemoteBox_2)
        self.newRemoteSchemeEdit.setEnabled(True)
        self.newRemoteSchemeEdit.setObjectName("newRemoteSchemeEdit")
        self.gridLayout_2.addWidget(self.newRemoteSchemeEdit, 1, 1, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.defaultRemoteBox_2)
        self.label_10.setObjectName("label_10")
        self.gridLayout_2.addWidget(self.label_10, 1, 2, 1, 1)
        self.newRemoteTimeoutEdit = QtWidgets.QLineEdit(self.defaultRemoteBox_2)
        self.newRemoteTimeoutEdit.setEnabled(True)
        self.newRemoteTimeoutEdit.setObjectName("newRemoteTimeoutEdit")
        self.gridLayout_2.addWidget(self.newRemoteTimeoutEdit, 1, 3, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.defaultRemoteBox_2)
        self.label_8.setObjectName("label_8")
        self.gridLayout_2.addWidget(self.label_8, 2, 0, 1, 1)
        self.newRemoteHostEdit = QtWidgets.QLineEdit(self.defaultRemoteBox_2)
        self.newRemoteHostEdit.setEnabled(True)
        self.newRemoteHostEdit.setObjectName("newRemoteHostEdit")
        self.gridLayout_2.addWidget(self.newRemoteHostEdit, 2, 1, 1, 1)
        self.submitNewButton = QtWidgets.QPushButton(self.defaultRemoteBox_2)
        self.submitNewButton.setObjectName("submitNewButton")
        self.gridLayout_2.addWidget(self.submitNewButton, 2, 3, 1, 1)
        self.gridLayout_4.addWidget(self.defaultRemoteBox_2, 1, 0, 1, 1)
        self.frame = QtWidgets.QFrame(UpldrSettings)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.remotesComboBox = QtWidgets.QComboBox(self.frame)
        self.remotesComboBox.setObjectName("remotesComboBox")
        self.gridLayout_3.addWidget(self.remotesComboBox, 0, 0, 1, 2)
        self.setDefaultButton = QtWidgets.QPushButton(self.frame)
        self.setDefaultButton.setObjectName("setDefaultButton")
        self.gridLayout_3.addWidget(self.setDefaultButton, 0, 3, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.frame)
        self.label_11.setObjectName("label_11")
        self.gridLayout_3.addWidget(self.label_11, 1, 0, 1, 1)
        self.listRemoteNameEdit = QtWidgets.QLineEdit(self.frame)
        self.listRemoteNameEdit.setEnabled(True)
        self.listRemoteNameEdit.setObjectName("listRemoteNameEdit")
        self.gridLayout_3.addWidget(self.listRemoteNameEdit, 1, 1, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.frame)
        self.label_15.setObjectName("label_15")
        self.gridLayout_3.addWidget(self.label_15, 1, 2, 1, 1)
        self.listRemotePortEdit = QtWidgets.QLineEdit(self.frame)
        self.listRemotePortEdit.setEnabled(True)
        self.listRemotePortEdit.setObjectName("listRemotePortEdit")
        self.gridLayout_3.addWidget(self.listRemotePortEdit, 1, 3, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.frame)
        self.label_13.setObjectName("label_13")
        self.gridLayout_3.addWidget(self.label_13, 2, 0, 1, 1)
        self.listRemoteSchemeEdit = QtWidgets.QLineEdit(self.frame)
        self.listRemoteSchemeEdit.setEnabled(True)
        self.listRemoteSchemeEdit.setObjectName("listRemoteSchemeEdit")
        self.gridLayout_3.addWidget(self.listRemoteSchemeEdit, 2, 1, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.frame)
        self.label_12.setObjectName("label_12")
        self.gridLayout_3.addWidget(self.label_12, 2, 2, 1, 1)
        self.listRemoteTimeoutEdit = QtWidgets.QLineEdit(self.frame)
        self.listRemoteTimeoutEdit.setEnabled(True)
        self.listRemoteTimeoutEdit.setObjectName("listRemoteTimeoutEdit")
        self.gridLayout_3.addWidget(self.listRemoteTimeoutEdit, 2, 3, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.frame)
        self.label_14.setObjectName("label_14")
        self.gridLayout_3.addWidget(self.label_14, 3, 0, 1, 1)
        self.listRemoteHostEdit = QtWidgets.QLineEdit(self.frame)
        self.listRemoteHostEdit.setEnabled(True)
        self.listRemoteHostEdit.setObjectName("listRemoteHostEdit")
        self.gridLayout_3.addWidget(self.listRemoteHostEdit, 3, 1, 1, 1)
        self.saveButton = QtWidgets.QPushButton(self.frame)
        self.saveButton.setObjectName("saveButton")
        self.gridLayout_3.addWidget(self.saveButton, 3, 3, 1, 1)
        self.deleteRemoteButton = QtWidgets.QPushButton(self.frame)
        self.deleteRemoteButton.setObjectName("deleteRemoteButton")
        self.gridLayout_3.addWidget(self.deleteRemoteButton, 0, 2, 1, 1)
        self.gridLayout_4.addWidget(self.frame, 2, 0, 1, 1)

        self.retranslateUi(UpldrSettings)
        self.submitNewButton.clicked.connect(UpldrSettings.submitRemoteSlot)
        self.setDefaultButton.clicked.connect(UpldrSettings.setDefaultSlot)
        self.saveButton.clicked.connect(UpldrSettings.saveRemoteSlot)
        self.remotesComboBox.currentIndexChanged['int'].connect(UpldrSettings.refreshAll)
        self.deleteRemoteButton.clicked.connect(UpldrSettings.deleteRemoteSlot)
        QtCore.QMetaObject.connectSlotsByName(UpldrSettings)

    def retranslateUi(self, UpldrSettings):
        _translate = QtCore.QCoreApplication.translate
        UpldrSettings.setWindowTitle(_translate("UpldrSettings", "Upldr Settings"))
        self.defaultRemoteBox.setTitle(_translate("UpldrSettings", "Default Remote"))
        self.label.setText(_translate("UpldrSettings", "Remote Name:"))
        self.label_4.setText(_translate("UpldrSettings", "Remote Port:"))
        self.label_2.setText(_translate("UpldrSettings", "Remote Scheme:"))
        self.label_5.setText(_translate("UpldrSettings", "Remote Timeout:"))
        self.label_3.setText(_translate("UpldrSettings", "Remote Host:"))
        self.defaultRemoteBox_2.setTitle(_translate("UpldrSettings", "New Remote"))
        self.label_6.setText(_translate("UpldrSettings", "Remote Name:"))
        self.label_9.setText(_translate("UpldrSettings", "Remote Port:"))
        self.label_7.setText(_translate("UpldrSettings", "Remote Scheme:"))
        self.label_10.setText(_translate("UpldrSettings", "Remote Timeout:"))
        self.label_8.setText(_translate("UpldrSettings", "Remote Host:"))
        self.submitNewButton.setText(_translate("UpldrSettings", "Submit"))
        self.setDefaultButton.setText(_translate("UpldrSettings", "Set Default"))
        self.label_11.setText(_translate("UpldrSettings", "Remote Name:"))
        self.label_15.setText(_translate("UpldrSettings", "Remote Port:"))
        self.label_13.setText(_translate("UpldrSettings", "Remote Scheme:"))
        self.label_12.setText(_translate("UpldrSettings", "Remote Timeout:"))
        self.label_14.setText(_translate("UpldrSettings", "Remote Host:"))
        self.saveButton.setText(_translate("UpldrSettings", "Save"))
        self.deleteRemoteButton.setText(_translate("UpldrSettings", "Delete Remote"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    UpldrSettings = QtWidgets.QWidget()
    ui = Ui_UpldrSettings()
    ui.setupUi(UpldrSettings)
    UpldrSettings.show()
    sys.exit(app.exec_())
