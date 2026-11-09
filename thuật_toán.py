# Form implementation generated from reading ui file 'giaodien_cf.ui'

from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)

        # Cấu hình Background cho giao diện từ file background_cf.jpg
        MainWindow.setStyleSheet("""
            QMainWindow {
                background-image: url('background_cf.jpg');
                background-position: center;
                background-repeat: no-repeat;
            }
            QLabel {
                color: #2B1810;
                font-weight: bold;
            }
            QPushButton {
                background-color: #FFF8DC;
                border: 2px solid #8B4513;
                border-radius: 8px;
                font-weight: bold;
                font-size: 11pt;
            }
            QPushButton:hover {
                background-color: #FFE4C4;
            }
            QListWidget, QLineEdit {
                background-color: rgba(255, 255, 255, 0.9);
                border-radius: 5px;
            }
        """)

        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.thoi_gian = QtWidgets.QLabel(parent=self.centralwidget)
        self.thoi_gian.setGeometry(QtCore.QRect(540, 50, 180, 31))
        self.thoi_gian.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";")
        self.thoi_gian.setObjectName("thoi_gian")

        self.quan_ca_phe = QtWidgets.QLabel(parent=self.centralwidget)
        self.quan_ca_phe.setGeometry(QtCore.QRect(20, 100, 421, 61))
        self.quan_ca_phe.setStyleSheet("font: 75 22pt \"MS Shell Dlg 2\";")
        self.quan_ca_phe.setObjectName("quan_ca_phe")

        # Icon con mèo ban đầu trên giao diện chính
        self.con_meo = QtWidgets.QLabel(parent=self.centralwidget)
        self.con_meo.setGeometry(QtCore.QRect(190, 170, 111, 81))
        self.con_meo.setStyleSheet("font: 75 36pt \"MS Shell Dlg 2\";")
        self.con_meo.setObjectName("con_meo")

        self.menu = QtWidgets.QLabel(parent=self.centralwidget)
        self.menu.setGeometry(QtCore.QRect(570, 140, 100, 30))
        self.menu.setStyleSheet("font: 75 16pt \"MS Shell Dlg 2\";")
        self.menu.setObjectName("menu")

        self.khach = QtWidgets.QLabel(parent=self.centralwidget)
        self.khach.setGeometry(QtCore.QRect(30, 40, 350, 31))
        self.khach.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";")
        self.khach.setObjectName("khach")

        # Khởi tạo các nút chọn nguyên liệu bổ sung Icon
        self.ca_phe = QtWidgets.QPushButton(parent=self.centralwidget)
        self.ca_phe.setGeometry(QtCore.QRect(30, 300, 120, 35))
        self.ca_phe.setObjectName("ca_phe")

        self.sua = QtWidgets.QPushButton(parent=self.centralwidget)
        self.sua.setGeometry(QtCore.QRect(160, 300, 120, 35))
        self.sua.setObjectName("sua")

        self.da = QtWidgets.QPushButton(parent=self.centralwidget)
        self.da.setGeometry(QtCore.QRect(290, 300, 120, 35))
        self.da.setObjectName("da")

        self.matcha = QtWidgets.QPushButton(parent=self.centralwidget)
        self.matcha.setGeometry(QtCore.QRect(30, 350, 120, 35))
        self.matcha.setObjectName("matcha")

        self.dao = QtWidgets.QPushButton(parent=self.centralwidget)
        self.dao.setGeometry(QtCore.QRect(160, 350, 120, 35))
        self.dao.setObjectName("dao")

        self.tra = QtWidgets.QPushButton(parent=self.centralwidget)
        self.tra.setGeometry(QtCore.QRect(290, 350, 120, 35))
        self.tra.setObjectName("tra")

        self.listWidget = QtWidgets.QListWidget(parent=self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(440, 180, 340, 340))
        self.listWidget.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";")
        self.listWidget.setObjectName("listWidget")

        items = [
            "Cà phê đen = cà phê + đá",
            "",
            "Cà phê sữa = cà phê + sữa + đá",
            "",
            "Trà đào = trà + đào + đá",
            "",
            "Matcha = matcha + sữa + đá",
            "",
            "Trà đá = trà + đá"
        ]
        for text in items:
            item = QtWidgets.QListWidgetItem(text)
            self.listWidget.addItem(item)

        self.thanh_phan = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.thanh_phan.setGeometry(QtCore.QRect(30, 410, 380, 30))
        self.thanh_phan.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";")
        self.thanh_phan.setObjectName("thanh_phan")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Quán Cà Phê Nhóm 7"))
        self.thoi_gian.setText(_translate("MainWindow", "Thời gian: 60s"))
        self.quan_ca_phe.setText(_translate("MainWindow", "QUÁN CÀ PHÊ NHÓM 7"))
        self.con_meo.setText(_translate("MainWindow", "😺"))
        self.menu.setText(_translate("MainWindow", "MENU"))
        self.khach.setText(_translate("MainWindow", "KHÁCH GỌI :"))

        # Bổ sung icon minh họa cho các nút bấm nguyên liệu
        self.ca_phe.setText(_translate("MainWindow", "☕ CÀ PHÊ"))
        self.sua.setText(_translate("MainWindow", "🥛 SỮA"))
        self.da.setText(_translate("MainWindow", "🧊 ĐÁ"))
        self.matcha.setText(_translate("MainWindow", "🍵 MATCHA"))
        self.dao.setText(_translate("MainWindow", "🍑 ĐÀO"))
        self.tra.setText(_translate("MainWindow", "🍃 TRÀ"))
