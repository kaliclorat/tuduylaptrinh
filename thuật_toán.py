import random

class CafeLogic :
    def __init__(self):
        # Danh sách menu đồ uống và công thức nguyên liệu tương ứng (tập hợp các nguyên liệu)
        self.menu_recipes = {
            "Cà phê đen": {"CÀ PHÊ", "ĐÁ"},
            "Cà phê sữa": {"CÀ PHÊ", "SỮA", "ĐÁ"},
            "Trà đào": {"TRÀ", "ĐÀO", "ĐÁ"},
            "Matcha": {"MATCHA", "SỮA", "ĐÁ"},
            "Trà đá": {"TRÀ", "ĐÁ"}
        }
        self.current_order = ""
        self.selected_ingredients = set()
        self.time_left =60

    def generate_random_order(self):
        """Random 1 món ăn/nước uống từ menu cho khách"""
        self.current_order = random.choice(list(self.menu_recipes.keys()))
        self.selected_ingredients.clear()
        self.time_left = self.time_left - 1
        return self.current_order

    def add_ingredient(self, ingredient_name):
        """Thêm nguyên liệu vào danh sách chọn và trả về chuỗi hiển thị trên line_edit"""
        self.selected_ingredients.add(ingredient_name)
        return " + ".join(sorted(self.selected_ingredients))

    def check_recipe(self):
        """Kiểm tra xem các nguyên liệu đã chọn có đúng với món khách gọi hay không"""
        if not self.current_order:
            return False

        required_ingredients = self.menu_recipes.get(self.current_order, set())

        if self.selected_ingredients == required_ingredients:
            return True, f"Chính xác!  {self.current_order} 😺"
        else:
            return False, "Chưa đúng công thức rồi, thử lại xem!"