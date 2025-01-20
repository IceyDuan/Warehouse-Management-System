class Product:
    def __init__(self, Name, ID, Amount, Time):
        self.Name = Name
        self.ID = ID
        self.Amount = Amount
        self.Time = Time

class ProductManageSystem:
    def __init__(self):
        self.product_list = []

    def add_product(self, Name, ID, Amount, Time):
        if Name == '' or ID == '' or Amount == '' or Time == '':
            return "Please enter complete information"
        else:
            product = Product(Name, ID, Amount, Time)
            self.product_list.append(product)
            return "Add successfully"

    def judge(self, ID):
        for i, product in enumerate(self.product_list):
            if product.ID == ID:
                return i, "The ID exists!"
        return -1, "The ID doesn't exist!"

    def modify_product(self, index1, Name, ID, Amount, Time):
        if index1 != -1:
            self.product_list[index1].Name = Name
            self.product_list[index1].ID = ID
            self.product_list[index1].Amount = Amount
            self.product_list[index1].Time = Time
            return "Modified successfully!"
        else:
            return "The ID does not exist or please search first!"

    def delete_product(self, index1):
        if index1 != -1:
            del self.product_list[index1]
            return "Deleted successfully!"
        else:
            return "The ID does not exist or please search first!"

    def search_product(self, ID):
        for product in self.product_list:
            if product.ID == ID:
                return f"Name：{product.Name} ID：{product.ID} Amount：{product.Amount} Entry time：{product.Time}"
        return "No result"

    def merge_sort(self, product_list, descending=False):
        """基于日期的归并排序算法，按年月日排序"""
        if len(product_list) <= 1:
            return product_list

        mid = len(product_list) // 2
        left_half = self.merge_sort(product_list[:mid], descending)
        right_half = self.merge_sort(product_list[mid:], descending)

        return self.merge(left_half, right_half, descending)

    def merge(self, left, right, descending):
        """合并两个有序列表，增加 descending 参数用于控制排序方向"""
        result = []
        i = j = 0

        # 手动解析日期的函数，只处理 YYYY-MM-DD 部分
        def parse_date(date_str):
            # 提取并解析日期部分 YYYY-MM-DD
            year, month, day = map(int, date_str.split('-'))
            return year, month, day

        while i < len(left) and j < len(right):
            left_date = parse_date(left[i].Time)
            right_date = parse_date(right[j].Time)

            # 如果 descending=True，进行降序排序，否则升序排序
            if descending:
                if left_date >= right_date:
                    result.append(left[i])
                    i += 1
                else:
                    result.append(right[j])
                    j += 1
            else:
                if left_date <= right_date:
                    result.append(left[i])
                    i += 1
                else:
                    result.append(right[j])
                    j += 1

        result.extend(left[i:])
        result.extend(right[j:])
        return result

    def display_products(self, sort_by_score=False, descending=False):
        """显示产品信息并根据需要进行排序，descending 控制升序或降序"""
        if len(self.product_list) == 0:
            return "No result"
        else:
            if sort_by_score:
                sorted_products = self.merge_sort(self.product_list, descending)
            else:
                sorted_products = self.product_list

            str1 = ''
            for product in sorted_products:
                str1 += f"Name：{product.Name} ID：{product.ID} Amount：{product.Amount} Entry time：{product.Time}\n"
            return str1
