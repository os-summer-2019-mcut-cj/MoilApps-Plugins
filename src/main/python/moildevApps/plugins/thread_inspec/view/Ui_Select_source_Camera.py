# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI/openCam.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(QtWidgets.QWidget):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 120)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_35 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_35.setObjectName("horizontalLayout_35")
        self.label_45 = QtWidgets.QLabel(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_45.sizePolicy().hasHeightForWidth())
        self.label_45.setSizePolicy(sizePolicy)
        self.label_45.setMinimumSize(QtCore.QSize(120, 30))
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setPointSize(12)
        self.label_45.setFont(font)
        self.label_45.setObjectName("label_45")
        self.horizontalLayout_35.addWidget(self.label_45)
        self.comboBox = QtWidgets.QComboBox(Dialog)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.horizontalLayout_35.addWidget(self.comboBox)
        self.verticalLayout.addLayout(self.horizontalLayout_35)


        self.framePortUsb = QtWidgets.QFrame(Dialog)
        self.framePortUsb.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.framePortUsb.setFrameShadow(QtWidgets.QFrame.Plain)
        self.framePortUsb.setObjectName("framePortUsb")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.framePortUsb)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.labelPort = QtWidgets.QLabel(self.framePortUsb)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelPort.sizePolicy().hasHeightForWidth())
        self.labelPort.setSizePolicy(sizePolicy)
        self.labelPort.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setPointSize(12)
        self.labelPort.setFont(font)
        self.labelPort.setObjectName("labelPort")
        self.horizontalLayout_3.addWidget(self.labelPort)
        self.portCamera = QtWidgets.QComboBox(self.framePortUsb)
        self.portCamera.setMinimumSize(QtCore.QSize(80, 0))
        self.portCamera.setObjectName("portCamera")
        self.portCamera.addItem("")
        self.portCamera.addItem("")
        self.portCamera.addItem("")
        self.portCamera.addItem("")
        self.portCamera.addItem("")
        self.portCamera.addItem("")
        self.horizontalLayout_3.addWidget(self.portCamera)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.detectPort = QtWidgets.QPushButton(self.framePortUsb)
        self.detectPort.setMinimumSize(QtCore.QSize(0, 30))
        self.detectPort.setObjectName("detectPort")
        self.horizontalLayout_3.addWidget(self.detectPort)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.verticalLayout.addWidget(self.framePortUsb)

        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_59 = QtWidgets.QLabel(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_59.sizePolicy().hasHeightForWidth())
        self.label_59.setSizePolicy(sizePolicy)
        self.label_59.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setPointSize(12)
        self.label_59.setFont(font)
        self.label_59.setObjectName("label_59")
        self.horizontalLayout.addWidget(self.label_59)
        self.camera_stream_link = QtWidgets.QLineEdit(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.camera_stream_link.sizePolicy().hasHeightForWidth())
        self.camera_stream_link.setSizePolicy(sizePolicy)
        self.camera_stream_link.setMinimumSize(QtCore.QSize(250, 0))
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setPointSize(12)
        self.camera_stream_link.setFont(font)
        self.camera_stream_link.setObjectName("camera_stream_link")
        self.horizontalLayout.addWidget(self.camera_stream_link)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonBox.sizePolicy().hasHeightForWidth())
        self.buttonBox.setSizePolicy(sizePolicy)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_45.setText(_translate("Dialog", "Select Source cam:"))
        self.comboBox.setItemText(0, _translate("Dialog", "USB Camera"))
        self.comboBox.setItemText(1, _translate("Dialog", "Stream Camera"))
        self.labelPort.setText(_translate("Dialog", "Port :"))
        self.portCamera.setItemText(0, _translate("Dialog", "0"))
        self.portCamera.setItemText(1, _translate("Dialog", "1"))
        self.portCamera.setItemText(2, _translate("Dialog", "2"))
        self.portCamera.setItemText(3, _translate("Dialog", "3"))
        self.portCamera.setItemText(4, _translate("Dialog", "4"))
        self.portCamera.setItemText(5, _translate("Dialog", "5"))
        self.detectPort.setText(_translate("Dialog", "Detect Port"))
        self.label_59.setText(_translate("Dialog", "Camera Link:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())