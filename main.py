import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt6 import uic
from PyQt6.QtCore import QTimer  # 1. Thêm QTimer ở đây
from thuật_toán import CafeLogic


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # Nạp giao diện đúng tên file .ui của bé
        uic.loadUi("giaodien_cf.ui", self)

        self.logic = CafeLogic()

        # Kết nối các nút bấm nguyên liệu
        self.ca_phe.clicked.connect(lambda: self.on_ingredient_clicked("CÀ PHÊ"))
        self.sua.clicked.connect(lambda: self.on_ingredient_clicked("SỮA"))
        self.da.clicked.connect(lambda: self.on_ingredient_clicked("ĐÁ"))
        self.matcha.clicked.connect(lambda: self.on_ingredient_clicked("MATCHA"))
        self.dao.clicked.connect(lambda: self.on_ingredient_clicked("ĐÀO"))
        self.tra.clicked.connect(lambda: self.on_ingredient_clicked("TRÀ"))

        # 2. Cấu hình QTimer đếm ngược mỗi 1 giây (1000 ms)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_timer)

        # Bắt đầu game lượt đầu tiên
        self.new_customer_order()

    def new_customer_order(self):
        dish_name = self.logic.generate_random_order()
        self.khach.setText(f"KHÁCH GỌI : {dish_name}")
        self.thanh_phan.clear()

        # Reset và khởi động lại đồng hồ đếm ngược
        self.timer.start(1000)

    def update_timer(self):
        """Hàm này tự động chạy mỗi giây để giảm thời gian"""
        if self.logic.time_left > 0:
            self.logic.time_left -= 1
            self.thoi_gian.setText(f"Thời gian: {self.logic.time_left}s")
        else:
            # Hết giờ
            self.timer.stop()
            QMessageBox.warning(self, "Hết giờ!", "Ôi không, khách đã bỏ đi vì đợi quá lâu rồi! 😿")
            self.new_customer_order()  # Sang khách mới

    def on_ingredient_clicked(self, ingredient_name):
        display_text = self.logic.add_ingredient(ingredient_name)
        self.thanh_phan.setText(display_text)

        required_count = len(self.logic.menu_recipes[self.logic.current_order])
        if len(self.logic.selected_ingredients) == required_count:
            # Dừng đồng hồ khi bé đã chọn xong nguyên liệu
            self.timer.stop()

            is_correct, message = self.logic.check_recipe()
            if is_correct:
                self.new_customer_order()
            else:
                QMessageBox.warning(self, "Thất bại", message)
                self.logic.selected_ingredients.clear()
                self.thanh_phan.clear()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())