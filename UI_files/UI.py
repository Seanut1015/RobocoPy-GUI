# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt6 UI code generator 6.9.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(321, 436)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QtCore.QSize(321, 436))
        Form.setMaximumSize(QtCore.QSize(321, 436))
        Form.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.tabWidget = QtWidgets.QTabWidget(parent=Form)
        self.tabWidget.setEnabled(True)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 321, 436))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setMinimumSize(QtCore.QSize(321, 436))
        self.tabWidget.setMaximumSize(QtCore.QSize(321, 436))
        font = QtGui.QFont()
        font.setFamily("Cascadia Mono Light")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.tabWidget.setFont(font)
        self.tabWidget.setContextMenuPolicy(
            QtCore.Qt.ContextMenuPolicy.DefaultContextMenu)
        self.tabWidget.setLayoutDirection(
            QtCore.Qt.LayoutDirection.LeftToRight)
        self.tabWidget.setIconSize(QtCore.QSize(16, 16))
        self.tabWidget.setElideMode(QtCore.Qt.TextElideMode.ElideNone)
        self.tabWidget.setDocumentMode(True)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.groupBox = QtWidgets.QGroupBox(parent=self.tab)
        self.groupBox.setGeometry(QtCore.QRect(11, 10, 299, 51))
        self.groupBox.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.groupBox.setAutoFillBackground(False)
        self.groupBox.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading |
                                   QtCore.Qt.AlignmentFlag.AlignLeft | QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.groupBox.setObjectName("groupBox")
        self.source_btn = QtWidgets.QPushButton(parent=self.groupBox)
        self.source_btn.setGeometry(QtCore.QRect(210, 20, 75, 23))
        self.source_btn.setAutoDefault(False)
        self.source_btn.setDefault(False)
        self.source_btn.setFlat(False)
        self.source_btn.setObjectName("source_btn")
        self.source_path = QtWidgets.QLineEdit(parent=self.groupBox)
        self.source_path.setGeometry(QtCore.QRect(20, 20, 181, 20))
        self.source_path.setReadOnly(False)
        self.source_path.setObjectName("source_path")
        self.groupBox_2 = QtWidgets.QGroupBox(parent=self.tab)
        self.groupBox_2.setGeometry(QtCore.QRect(11, 70, 299, 51))
        self.groupBox_2.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.groupBox_2.setObjectName("groupBox_2")
        self.det_btn = QtWidgets.QPushButton(parent=self.groupBox_2)
        self.det_btn.setGeometry(QtCore.QRect(210, 20, 75, 23))
        self.det_btn.setObjectName("det_btn")
        self.det_path = QtWidgets.QLineEdit(parent=self.groupBox_2)
        self.det_path.setGeometry(QtCore.QRect(20, 20, 181, 20))
        self.det_path.setReadOnly(False)
        self.det_path.setObjectName("det_path")
        self.groupBox_3 = QtWidgets.QGroupBox(parent=self.tab)
        self.groupBox_3.setGeometry(QtCore.QRect(11, 130, 299, 51))
        self.groupBox_3.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.groupBox_3.setObjectName("groupBox_3")
        self.radioButton = QtWidgets.QRadioButton(parent=self.groupBox_3)
        self.radioButton.setGeometry(QtCore.QRect(20, 25, 49, 16))
        self.radioButton.setChecked(True)
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(parent=self.groupBox_3)
        self.radioButton_2.setGeometry(QtCore.QRect(120, 25, 50, 16))
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_3 = QtWidgets.QRadioButton(parent=self.groupBox_3)
        self.radioButton_3.setGeometry(QtCore.QRect(220, 25, 54, 16))
        self.radioButton_3.setObjectName("radioButton_3")
        self.groupBox_4 = QtWidgets.QGroupBox(parent=self.tab)
        self.groupBox_4.setGeometry(QtCore.QRect(11, 190, 299, 101))
        self.groupBox_4.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.groupBox_4.setObjectName("groupBox_4")
        self.mt_cb = QtWidgets.QCheckBox(parent=self.groupBox_4)
        self.mt_cb.setGeometry(QtCore.QRect(20, 25, 81, 16))
        self.mt_cb.setTabletTracking(False)
        self.mt_cb.setChecked(True)
        self.mt_cb.setTristate(False)
        self.mt_cb.setObjectName("mt_cb")
        self.j_cb = QtWidgets.QCheckBox(parent=self.groupBox_4)
        self.j_cb.setGeometry(QtCore.QRect(20, 50, 81, 16))
        self.j_cb.setChecked(False)
        self.j_cb.setObjectName("j_cb")
        self.z_cb = QtWidgets.QCheckBox(parent=self.groupBox_4)
        self.z_cb.setGeometry(QtCore.QRect(20, 75, 81, 16))
        self.z_cb.setChecked(False)
        self.z_cb.setObjectName("z_cb")
        self.mt_sb = QtWidgets.QSpinBox(parent=self.groupBox_4)
        self.mt_sb.setGeometry(QtCore.QRect(100, 25, 43, 20))
        self.mt_sb.setMinimum(1)
        self.mt_sb.setMaximum(128)
        self.mt_sb.setProperty("value", 8)
        self.mt_sb.setObjectName("mt_sb")
        self.xn_cb = QtWidgets.QCheckBox(parent=self.groupBox_4)
        self.xn_cb.setGeometry(QtCore.QRect(170, 50, 111, 16))
        self.xn_cb.setObjectName("xn_cb")
        self.xo_cb = QtWidgets.QCheckBox(parent=self.groupBox_4)
        self.xo_cb.setGeometry(QtCore.QRect(170, 75, 111, 16))
        self.xo_cb.setObjectName("xo_cb")
        self.is_cb = QtWidgets.QCheckBox(parent=self.groupBox_4)
        self.is_cb.setGeometry(QtCore.QRect(170, 25, 111, 16))
        self.is_cb.setObjectName("is_cb")
        self.cancel_btn = QtWidgets.QPushButton(parent=self.tab)
        self.cancel_btn.setGeometry(QtCore.QRect(20, 375, 75, 23))
        self.cancel_btn.setObjectName("cancel_btn")
        self.start_btn = QtWidgets.QPushButton(parent=self.tab)
        self.start_btn.setGeometry(QtCore.QRect(226, 375, 75, 23))
        self.start_btn.setObjectName("start_btn")
        self.groupBox_5 = QtWidgets.QGroupBox(parent=self.tab)
        self.groupBox_5.setGeometry(QtCore.QRect(11, 300, 299, 61))
        self.groupBox_5.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.groupBox_5.setObjectName("groupBox_5")
        self.progressBar = QtWidgets.QProgressBar(parent=self.groupBox_5)
        self.progressBar.setGeometry(QtCore.QRect(100, 25, 191, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.label = QtWidgets.QLabel(parent=self.groupBox_5)
        self.label.setGeometry(QtCore.QRect(20, 20, 81, 31))
        self.label.setObjectName("label")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.groupBox_6 = QtWidgets.QGroupBox(parent=self.tab_2)
        self.groupBox_6.setGeometry(QtCore.QRect(11, 10, 299, 86))
        self.groupBox_6.setObjectName("groupBox_6")
        self.label_2 = QtWidgets.QLabel(parent=self.groupBox_6)
        self.label_2.setGeometry(QtCore.QRect(20, 25, 61, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=self.groupBox_6)
        self.label_3.setGeometry(QtCore.QRect(20, 55, 61, 16))
        self.label_3.setObjectName("label_3")
        self.rt_time = QtWidgets.QSpinBox(parent=self.groupBox_6)
        self.rt_time.setGeometry(QtCore.QRect(80, 20, 41, 22))
        self.rt_time.setMinimum(1)
        self.rt_time.setMaximum(9)
        self.rt_time.setObjectName("rt_time")
        self.wait_time = QtWidgets.QSpinBox(parent=self.groupBox_6)
        self.wait_time.setGeometry(QtCore.QRect(80, 50, 41, 22))
        self.wait_time.setMinimum(1)
        self.wait_time.setMaximum(59)
        self.wait_time.setObjectName("wait_time")
        self.comboBox = QtWidgets.QComboBox(parent=self.groupBox_6)
        self.comboBox.setGeometry(QtCore.QRect(200, 20, 61, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox_2 = QtWidgets.QComboBox(parent=self.groupBox_6)
        self.comboBox_2.setGeometry(QtCore.QRect(200, 50, 61, 22))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.label_6 = QtWidgets.QLabel(parent=self.groupBox_6)
        self.label_6.setGeometry(QtCore.QRect(170, 25, 51, 16))
        self.label_6.setToolTip("")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(parent=self.groupBox_6)
        self.label_7.setGeometry(QtCore.QRect(170, 55, 51, 16))
        self.label_7.setToolTip("")
        self.label_7.setObjectName("label_7")
        self.groupBox_7 = QtWidgets.QGroupBox(parent=self.tab_2)
        self.groupBox_7.setGeometry(QtCore.QRect(11, 105, 299, 111))
        self.groupBox_7.setObjectName("groupBox_7")
        self.i_s_cb = QtWidgets.QCheckBox(parent=self.groupBox_7)
        self.i_s_cb.setGeometry(QtCore.QRect(20, 25, 121, 16))
        self.i_s_cb.setToolTip("")
        self.i_s_cb.setChecked(True)
        self.i_s_cb.setObjectName("i_s_cb")
        self.e_cb = QtWidgets.QCheckBox(parent=self.groupBox_7)
        self.e_cb.setGeometry(QtCore.QRect(170, 25, 101, 16))
        self.e_cb.setChecked(True)
        self.e_cb.setObjectName("e_cb")
        self.xd_xf_cb = QtWidgets.QCheckBox(parent=self.groupBox_7)
        self.xd_xf_cb.setGeometry(QtCore.QRect(20, 55, 121, 16))
        self.xd_xf_cb.setChecked(True)
        self.xd_xf_cb.setObjectName("xd_xf_cb")
        self.not_e_s_cb = QtWidgets.QCheckBox(parent=self.groupBox_7)
        self.not_e_s_cb.setEnabled(False)
        self.not_e_s_cb.setGeometry(QtCore.QRect(170, 55, 101, 16))
        self.not_e_s_cb.setCheckable(True)
        self.not_e_s_cb.setChecked(False)
        self.not_e_s_cb.setObjectName("not_e_s_cb")
        self.mir_w_cb = QtWidgets.QCheckBox(parent=self.groupBox_7)
        self.mir_w_cb.setGeometry(QtCore.QRect(20, 85, 121, 16))
        self.mir_w_cb.setChecked(False)
        self.mir_w_cb.setObjectName("mir_w_cb")
        self.preview_cb = QtWidgets.QCheckBox(parent=self.groupBox_7)
        self.preview_cb.setEnabled(True)
        self.preview_cb.setGeometry(QtCore.QRect(170, 85, 101, 16))
        self.preview_cb.setCheckable(True)
        self.preview_cb.setChecked(False)
        self.preview_cb.setObjectName("preview_cb")
        self.groupBox_8 = QtWidgets.QGroupBox(parent=self.tab_2)
        self.groupBox_8.setGeometry(QtCore.QRect(11, 225, 299, 111))
        self.groupBox_8.setCheckable(False)
        self.groupBox_8.setObjectName("groupBox_8")
        self.log_cb = QtWidgets.QCheckBox(parent=self.groupBox_8)
        self.log_cb.setGeometry(QtCore.QRect(20, 20, 73, 16))
        self.log_cb.setChecked(True)
        self.log_cb.setObjectName("log_cb")
        self.log_btn = QtWidgets.QPushButton(parent=self.groupBox_8)
        self.log_btn.setGeometry(QtCore.QRect(210, 80, 75, 23))
        self.log_btn.setObjectName("log_btn")
        self.log_path = QtWidgets.QLineEdit(parent=self.groupBox_8)
        self.log_path.setGeometry(QtCore.QRect(20, 80, 181, 20))
        self.log_path.setReadOnly(True)
        self.log_path.setObjectName("log_path")
        self.logp_cb = QtWidgets.QCheckBox(parent=self.groupBox_8)
        self.logp_cb.setGeometry(QtCore.QRect(170, 20, 91, 16))
        self.logp_cb.setChecked(True)
        self.logp_cb.setObjectName("logp_cb")
        self.nfl_cb = QtWidgets.QCheckBox(parent=self.groupBox_8)
        self.nfl_cb.setGeometry(QtCore.QRect(20, 50, 73, 16))
        self.nfl_cb.setObjectName("nfl_cb")
        self.ndl_cb = QtWidgets.QCheckBox(parent=self.groupBox_8)
        self.ndl_cb.setGeometry(QtCore.QRect(170, 50, 91, 16))
        self.ndl_cb.setObjectName("ndl_cb")
        self.label_4 = QtWidgets.QLabel(parent=self.tab_2)
        self.label_4.setGeometry(QtCore.QRect(20, 370, 221, 21))
        font = QtGui.QFont()
        font.setFamily("Cascadia Mono SemiLight")
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.tabWidget.addTab(self.tab_2, "")

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(0)
        self.source_btn.clicked.connect(Form.source_folder)  # type: ignore
        self.det_btn.clicked.connect(Form.det_folder)  # type: ignore
        self.start_btn.clicked.connect(Form.start)  # type: ignore
        self.cancel_btn.clicked.connect(Form.cancel)  # type: ignore
        self.log_btn.clicked.connect(Form.log_folder)  # type: ignore
        self.radioButton_3.clicked.connect(Form.mir_warning)  # type: ignore
        self.preview_cb.clicked.connect(Form.preview_cmd)  # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.groupBox.setTitle(_translate("Form", "來源位置"))
        self.source_btn.setText(_translate("Form", "劉覽"))
        self.groupBox_2.setTitle(_translate("Form", "目標位置"))
        self.det_btn.setText(_translate("Form", "瀏覽"))
        self.groupBox_3.setTitle(_translate("Form", "選擇動作"))
        self.radioButton.setToolTip(_translate("Form", "複製檔案"))
        self.radioButton.setText(_translate("Form", "複製"))
        self.radioButton_2.setToolTip(_translate("Form", "移動檔案"))
        self.radioButton_2.setText(_translate("Form", "移動"))
        self.radioButton_3.setToolTip(_translate(
            "Form", "鏡像複製(使目標資料夾與來源資料夾完全相同，不推薦使用)"))
        self.radioButton_3.setText(_translate("Form", "鏡像"))
        self.groupBox_4.setTitle(_translate("Form", "傳輸功能"))
        self.mt_cb.setToolTip(_translate("Form", "針對大量檔案使用多執行續加速傳輸(範圍為1~128)"))
        self.mt_cb.setText(_translate("Form", "多執行續"))
        self.j_cb.setToolTip(_translate("Form", "啟用非緩衝 I/O，建議單個檔案超過100MB時使用"))
        self.j_cb.setText(_translate("Form", "大型檔案"))
        self.z_cb.setToolTip(_translate("Form", "如果中斷傳輸，下次可從中斷處繼續(略微降低性能)"))
        self.z_cb.setText(_translate("Form", "中斷恢復"))
        self.xn_cb.setToolTip(_translate("Form", "有相同檔案時，在目標位置保留較舊的檔案"))
        self.xn_cb.setText(_translate("Form", "保留較舊檔案"))
        self.xo_cb.setToolTip(_translate("Form", "有相同檔案時，在目標位置保留較新的檔案"))
        self.xo_cb.setText(_translate("Form", "保留較新檔案"))
        self.is_cb.setToolTip(_translate("Form", "強制取代所有檔案(預設為略過)"))
        self.is_cb.setText(_translate("Form", "強制全部取代"))
        self.cancel_btn.setText(_translate("Form", "取消"))
        self.start_btn.setText(_translate("Form", "開始傳輸"))
        self.groupBox_5.setTitle(_translate("Form", "狀態"))
        self.label.setText(_translate("Form", "準備中..."))
        self.tabWidget.setTabText(self.tabWidget.indexOf(
            self.tab), _translate("Form", "常用"))
        self.groupBox_6.setTitle(_translate("Form", "失敗重試"))
        self.label_2.setToolTip(_translate("Form", "重試次數(建議:3次)"))
        self.label_2.setText(_translate("Form", "重試次數"))
        self.label_3.setToolTip(_translate("Form", "重試等待時間(建議:5秒)"))
        self.label_3.setText(_translate("Form", "等待時間"))
        self.comboBox.setCurrentText(_translate("Form", "次"))
        self.comboBox.setItemText(0, _translate("Form", "次"))
        self.comboBox.setItemText(1, _translate("Form", "十"))
        self.comboBox.setItemText(2, _translate("Form", "百"))
        self.comboBox.setItemText(3, _translate("Form", "千"))
        self.comboBox.setItemText(4, _translate("Form", "萬"))
        self.comboBox.setItemText(5, _translate("Form", "十萬"))
        self.comboBox_2.setCurrentText(_translate("Form", "秒"))
        self.comboBox_2.setItemText(0, _translate("Form", "秒"))
        self.comboBox_2.setItemText(1, _translate("Form", "分"))
        self.comboBox_2.setItemText(2, _translate("Form", "時"))
        self.label_6.setText(_translate("Form", "單位"))
        self.label_7.setText(_translate("Form", "單位"))
        self.groupBox_7.setTitle(_translate("Form", "進階功能"))
        self.i_s_cb.setText(_translate("Form", "包含來源資料夾"))
        self.e_cb.setText(_translate("Form", "包含空資料夾"))
        self.xd_xf_cb.setToolTip(_translate(
            "Form", "在來源資料夾中加入exclude.txt，即可排除內部寫到的檔案"))
        self.xd_xf_cb.setText(_translate("Form", "排除exclude.txt"))
        self.not_e_s_cb.setText(_translate("Form", "不包含資料夾"))
        self.mir_w_cb.setToolTip(_translate(
            "Form", "在來源資料夾中加入exclude.txt，即可排除內部寫到的檔案"))
        self.mir_w_cb.setText(_translate("Form", "關閉鏡像警告"))
        self.preview_cb.setText(_translate("Form", "開啟預覽"))
        self.groupBox_8.setTitle(_translate("Form", "記錄檔"))
        self.log_cb.setText(_translate("Form", "啟用log"))
        self.log_btn.setText(_translate("Form", "瀏覽"))
        self.logp_cb.setText(_translate("Form", "僅保留單次"))
        self.nfl_cb.setText(_translate("Form", "顯示檔案"))
        self.ndl_cb.setText(_translate("Form", "顯示清單"))
        self.label_4.setText(_translate(
            "Form", "© 2025 Seanut‧GPLv3 License  "))
        self.tabWidget.setTabText(self.tabWidget.indexOf(
            self.tab_2), _translate("Form", "進階"))
