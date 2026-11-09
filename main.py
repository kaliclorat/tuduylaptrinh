import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QDialog, QVBoxLayout, QLabel, QPushButton
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import QTimer, Qt
from giaodien_cf import Ui_MainWindow
from thuat_toan import CafeLogic


class ResultDialog(QDialog):
    """Cửa sổ hiển thị hình ảnh thông báo kết quả (Mèo Like / Mèo Khóc)"""

    def __init__(self, image_path, message, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Kết quả")
        self.setFixedSize(320, 360)

        layout = QVBoxLayout()

        # Hiển thị hình ảnh
        self.image_label = QLabel(self)
        pixmap = QPixmap(image_path)
        if not pixmap.isNull():
            self.image_label.setPixmap(
                pixmap.scaled(250, 250, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation))
        else:
            self.image_label.setText("[ Không tìm thấy ảnh ]")
        self.image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.image_label)

        # Hiển thị thông báo
        self.msg_label = QLabel(message, self)
        self.msg_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.msg_label.setStyleSheet("font-size: 12pt; font-weight: bold; color: #333;")
        layout.addWidget(self.msg_label)

        # Nút xác nhận
        btn_ok = QPushButton("Đóng", self)
        btn_ok.setStyleSheet(
            "padding: 6px; font-size: 10pt; background-color: #4CAF50; color: white; border-radius: 4px;")
        btn_ok.clicked.connect(self.accept)
        layout.addWidget(btn_ok)

        self.setLayout(layout)


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.logic = CafeLogic()

        # Kết nối các nút bấm nguyên liệu
        self.ca_phe.clicked.connect(lambda: self.on_ingredient_clicked("CÀ PHÊ"))
        self.sua.clicked.connect(lambda: self.on_ingredient_clicked("SỮA"))
        self.da.clicked.connect(lambda: self.on_ingredient_clicked("ĐÁ"))
        self.matcha.clicked.connect(lambda: self.on_ingredient_clicked("MATCHA"))
        self.dao.clicked.connect(lambda: self.on_ingredient_clicked("ĐÀO"))
        self.tra.clicked.connect(lambda: self.on_ingredient_clicked("TRÀ"))

        # Cấu hình Timer đếm ngược (1000 ms = 1s)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_timer)

        # Bắt đầu trò chơi
        self.new_customer_order()

    def new_customer_order(self):
        dish_name = self.logic.generate_random_order()
        self.khach.setText(f"KHÁCH GỌI : {dish_name}")
        self.thanh_phan.clear()
        self.thoi_gian.setText(f"Thời gian: {self.logic.time_left}s")
        self.timer.start(1000)

    def update_timer(self):
        if self.logic.time_left > 0:
            self.logic.time_left -= 1
            self.thoi_gian.setText(f"Thời gian: {self.logic.time_left}s")
        else:
            self.timer.stop()
            # Hiện cửa sổ Mèo Khóc khi hết thời gian
            dialog = ResultDialog("cat_cry.jpg", "Ôi không! Khách đã bỏ đi vì đợi quá lâu! 😿", self)
            dialog.exec()
            self.new_customer_order()

    def on_ingredient_clicked(self, ingredient_name):
        display_text = self.logic.add_ingredient(ingredient_name)
        self.thanh_phan.setText(display_text)

        required_count = len(self.logic.menu_recipes[self.logic.current_order])
        if len(self.logic.selected_ingredients) == required_count:
            self.timer.stop()

            is_correct, message = self.logic.check_recipe()
            if is_correct:
                # Hiện cửa sổ Mèo Like khi làm đúng món
                dialog = ResultDialog("cat_like.jpg", message, self)
                dialog.exec()
                self.new_customer_order()
            else:
                # Hiện cửa sổ Mèo Khóc khi pha sai món
                dialog = ResultDialog("cat_cry.jpg", message, self)
                dialog.exec()
                self.logic.selected_ingredients.clear()
                self.thanh_phan.clear()
                self.timer.start(1000)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
