import random

class CafeLogic:
    def __init__(self):
        # Danh sách menu đồ uống và công thức nguyên liệu tương ứng
        self.menu_recipes = {
            "Cà phê đen": {"CÀ PHÊ", "ĐÁ"},
            "Cà phê sữa": {"CÀ PHÊ", "SỮA", "ĐÁ"},
            "Trà đào": {"TRÀ", "ĐÀO", "ĐÁ"},
            "Matcha": {"MATCHA", "SỮA", "ĐÁ"},
            "Trà đá": {"TRÀ", "ĐÁ"}
        }
        self.current_order = ""
        self.selected_ingredients = set()
        self.time_left = 60

    def generate_random_order(self):
        """Tạo ngẫu nhiên 1 món đồ uống từ menu"""
        self.current_order = random.choice(list(self.menu_recipes.keys()))
        self.selected_ingredients.clear()
        self.time_left = 60
        return self.current_order

    def add_ingredient(self, ingredient_name):
        """Thêm nguyên liệu vào danh sách chọn và trả về chuỗi hiển thị"""
        self.selected_ingredients.add(ingredient_name)
        return " + ".join(sorted(self.selected_ingredients))

    def check_recipe(self):
        """Kiểm tra xem nguyên liệu đã chọn có khớp với món khách gọi không"""
        if not self.current_order:
            return False, "Chưa có món ăn được chọn!"

        required_ingredients = self.menu_recipes.get(self.current_order, set())

        if self.selected_ingredients == required_ingredients:
            return True, f"Chính xác! Đã làm xong {self.current_order}!"
        else:
            return False, "Chưa đúng công thức rồi, thử lại xem!"