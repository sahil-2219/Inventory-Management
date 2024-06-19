# order_processing.py

from collections import deque

class OrderProcessingSystem:
    def __init__(self):
        self.order_queue = deque()  # Queue to store orders in processing order

    def add_order_to_queue(self, order_id):
        self.order_queue.append(order_id)

    def process_next_order(self):
        if self.order_queue:
            return self.order_queue.popleft()
        return None  # Queue is empty

# Example usage
if __name__ == "__main__":
    ops = OrderProcessingSystem()
    ops.add_order_to_queue('O001')
    ops.add_order_to_queue('O002')
    print(ops.process_next_order())
    print(ops.process_next_order())
