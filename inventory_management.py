# inventory_management.py

class InventoryManagementSystem:
    def __init__(self):
        self.product_catalog = {}  # Hash map to store product catalog: {product_id: {'name': name, 'price': price, 'stock': stock}}

    def add_product(self, product_id, name, price, stock):
        if product_id in self.product_catalog:
            return False  # Product with this ID already exists
        self.product_catalog[product_id] = {'name': name, 'price': price, 'stock': stock}
        return True

    def update_stock(self, product_id, quantity):
        if product_id in self.product_catalog:
            self.product_catalog[product_id]['stock'] += quantity
            return True
        return False  # Product not found

    def search_product(self, product_id):
        if product_id in self.product_catalog:
            return self.product_catalog[product_id]
        return None

    def list_products_by_price(self):
        sorted_products = sorted(self.product_catalog.items(), key=lambda x: x[1]['price'])
        return sorted_products

# Example usage
if __name__ == "__main__":
    ims = InventoryManagementSystem()
    ims.add_product('P001', 'Smartphone', 500, 100)
    ims.add_product('P002', 'Laptop', 1000, 50)
    ims.update_stock('P001', 10)
    print(ims.search_product('P001'))
    print(ims.list_products_by_price())
