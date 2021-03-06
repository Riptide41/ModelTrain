# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TrainSettingUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(541, 290)
        self.layoutWidget = QtWidgets.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(32, 22, 478, 266))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.layoutWidget.setFont(font)
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.checkBox_rect = QtWidgets.QCheckBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.checkBox_rect.setFont(font)
        self.checkBox_rect.setObjectName("checkBox_rect")
        self.gridLayout.addWidget(self.checkBox_rect, 5, 0, 1, 1)
        self.lineEdit_batch_size = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lineEdit_batch_size.setFont(font)
        self.lineEdit_batch_size.setObjectName("lineEdit_batch_size")
        self.gridLayout.addWidget(self.lineEdit_batch_size, 1, 3, 1, 1)
        self.checkBox_linearlr = QtWidgets.QCheckBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.checkBox_linearlr.setFont(font)
        self.checkBox_linearlr.setObjectName("checkBox_linearlr")
        self.gridLayout.addWidget(self.checkBox_linearlr, 7, 0, 1, 1)
        self.lineEdit_img_size = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lineEdit_img_size.setFont(font)
        self.lineEdit_img_size.setObjectName("lineEdit_img_size")
        self.gridLayout.addWidget(self.lineEdit_img_size, 2, 3, 1, 1)
        self.btn_select_weight = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.btn_select_weight.setFont(font)
        self.btn_select_weight.setObjectName("btn_select_weight")
        self.gridLayout.addWidget(self.btn_select_weight, 0, 3, 1, 1)
        self.btn_ok = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.btn_ok.setFont(font)
        self.btn_ok.setObjectName("btn_ok")
        self.gridLayout.addWidget(self.btn_ok, 8, 3, 1, 1)
        self.checkBox_resume = QtWidgets.QCheckBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.checkBox_resume.setFont(font)
        self.checkBox_resume.setObjectName("checkBox_resume")
        self.gridLayout.addWidget(self.checkBox_resume, 7, 2, 1, 1)
        self.checkBox_evolve = QtWidgets.QCheckBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.checkBox_evolve.setFont(font)
        self.checkBox_evolve.setObjectName("checkBox_evolve")
        self.gridLayout.addWidget(self.checkBox_evolve, 6, 2, 1, 1)
        self.checkBox_notest = QtWidgets.QCheckBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.checkBox_notest.setFont(font)
        self.checkBox_notest.setObjectName("checkBox_notest")
        self.gridLayout.addWidget(self.checkBox_notest, 4, 2, 1, 1)
        self.label = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.lineEdit_name = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lineEdit_name.setFont(font)
        self.lineEdit_name.setObjectName("lineEdit_name")
        self.gridLayout.addWidget(self.lineEdit_name, 1, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 2, 2, 1, 1)
        self.checkBox_nosave = QtWidgets.QCheckBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.checkBox_nosave.setFont(font)
        self.checkBox_nosave.setObjectName("checkBox_nosave")
        self.gridLayout.addWidget(self.checkBox_nosave, 4, 0, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 1, 0, 1, 1)
        self.checkBox_adam = QtWidgets.QCheckBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.checkBox_adam.setFont(font)
        self.checkBox_adam.setObjectName("checkBox_adam")
        self.gridLayout.addWidget(self.checkBox_adam, 6, 0, 1, 1)
        self.checkBox_noautoanchor = QtWidgets.QCheckBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.checkBox_noautoanchor.setFont(font)
        self.checkBox_noautoanchor.setObjectName("checkBox_noautoanchor")
        self.gridLayout.addWidget(self.checkBox_noautoanchor, 5, 2, 1, 1)
        self.lineEdit_device = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lineEdit_device.setFont(font)
        self.lineEdit_device.setObjectName("lineEdit_device")
        self.gridLayout.addWidget(self.lineEdit_device, 2, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1)
        self.lineEdit_epoch = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lineEdit_epoch.setFont(font)
        self.lineEdit_epoch.setObjectName("lineEdit_epoch")
        self.gridLayout.addWidget(self.lineEdit_epoch, 3, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 1, 2, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 2, 0, 1, 1)
        self.lineEdit_weight = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lineEdit_weight.setFont(font)
        self.lineEdit_weight.setObjectName("lineEdit_weight")
        self.gridLayout.addWidget(self.lineEdit_weight, 0, 1, 1, 2)
        self.btn_set_hyperparameters = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.btn_set_hyperparameters.setFont(font)
        self.btn_set_hyperparameters.setObjectName("btn_set_hyperparameters")
        self.gridLayout.addWidget(self.btn_set_hyperparameters, 3, 2, 1, 2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Train parameter"))
        self.checkBox_rect.setToolTip(_translate("Form", "<html><head/><body><p>rectangular training</p></body></html>"))
        self.checkBox_rect.setText(_translate("Form", "Rect"))
        self.lineEdit_batch_size.setText(_translate("Form", "4"))
        self.checkBox_linearlr.setToolTip(_translate("Form", "<html><head/><body><p>linear LR</p></body></html>"))
        self.checkBox_linearlr.setText(_translate("Form", "Linear-lr"))
        self.lineEdit_img_size.setText(_translate("Form", "640"))
        self.btn_select_weight.setText(_translate("Form", "Select"))
        self.btn_ok.setText(_translate("Form", "OK"))
        self.checkBox_resume.setToolTip(_translate("Form", "<html><head/><body><p>resume most recent training</p></body></html>"))
        self.checkBox_resume.setText(_translate("Form", "Resume"))
        self.checkBox_evolve.setToolTip(_translate("Form", "<html><head/><body><p>evolve hyperparameters</p></body></html>"))
        self.checkBox_evolve.setText(_translate("Form", "Evolve"))
        self.checkBox_notest.setToolTip(_translate("Form", "<html><head/><body><p>only test final epoch</p></body></html>"))
        self.checkBox_notest.setText(_translate("Form", "Notest"))
        self.label.setToolTip(_translate("Form", "<html><head/><body><p>initial weights path</p></body></html>"))
        self.label.setWhatsThis(_translate("Form", "<html><head/><body><p>initial weights path</p></body></html>"))
        self.label.setText(_translate("Form", "Weight:"))
        self.lineEdit_name.setText(_translate("Form", "exp"))
        self.label_5.setToolTip(_translate("Form", "<html><head/><body><p>[train, test] image sizes</p></body></html>"))
        self.label_5.setWhatsThis(_translate("Form", "<html><head/><body><pre style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#2b2b2b;\"><span style=\" font-family:\'JetBrains Mono\',\'monospace\'; font-size:11.3pt; color:#6a8759;\">[train, test] image sizes</span></pre></body></html>"))
        self.label_5.setText(_translate("Form", "Img size:"))
        self.checkBox_nosave.setToolTip(_translate("Form", "<html><head/><body><p>only save final checkpoint</p></body></html>"))
        self.checkBox_nosave.setText(_translate("Form", "Nosave"))
        self.label_8.setToolTip(_translate("Form", "<html><head/><body><p>save to project/name</p></body></html>"))
        self.label_8.setText(_translate("Form", "Name:"))
        self.checkBox_adam.setToolTip(_translate("Form", "<html><head/><body><p>use torch.optim.Adam() optimizer</p></body></html>"))
        self.checkBox_adam.setText(_translate("Form", "Adam"))
        self.checkBox_noautoanchor.setToolTip(_translate("Form", "<html><head/><body><p>disable autoanchor check</p></body></html>"))
        self.checkBox_noautoanchor.setText(_translate("Form", "Noautoanchor"))
        self.label_3.setText(_translate("Form", "Epochs:  "))
        self.lineEdit_epoch.setText(_translate("Form", "300"))
        self.label_4.setToolTip(_translate("Form", "<html><head/><body><p>total batch size for all GPUs</p></body></html>"))
        self.label_4.setWhatsThis(_translate("Form", "<html><head/><body><pre style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#2b2b2b;\"><span style=\" font-family:\'JetBrains Mono\',\'monospace\'; font-size:11.3pt; color:#6a8759;\">total batch size for all GPUs</span></pre></body></html>"))
        self.label_4.setText(_translate("Form", "Batch size:"))
        self.label_7.setToolTip(_translate("Form", "<html><head/><body><p>cuda device, i.e. 0 or 0,1,2,3 or cpu</p></body></html>"))
        self.label_7.setText(_translate("Form", "Device:"))
        self.lineEdit_weight.setText(_translate("Form", "yolov5s.pt"))
        self.btn_set_hyperparameters.setText(_translate("Form", "Change Hyperparameters"))
