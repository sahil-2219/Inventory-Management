# order_management.py

class OrderManagementSystem:
    def __init__(self):
        self.orders = []  # Array to store orders: [{'order_id': id, 'product_id': product_id, 'quantity': quantity, 'status': status}]

    def place_order(self, order_id, product_id, quantity):
        self.orders.append({'order_id': order_id, 'product_id': product_id, 'quantity': quantity, 'status': 'Placed'})

    def track_order(self, order_id):
        for order in self.orders:
            if order['order_id'] == order_id:
                return order
        return None  # Order not found

    def list_orders_by_status(self, status):
        filtered_orders = [order for order in self.orders if order['status'] == status]
        return filtered_orders

# Example usage
if __name__ == "__main__":
    oms = OrderManagementSystem()
    oms.place_order('O001', 'P001', 5)
    oms.place_order('O002', 'P002', 2)
    print(oms.track_order('O001'))
    print(oms.list_orders_by_status('Placed'))
