from inventory_management import InventoryManagementSystem
from order_mangement import OrderManagementSystem
from order_processing import OrderProcessingSystem
from sorting_algo import bubble_sort

# Main function to run the entire project
def main():
    # Example: Calling functions or methods from each script
    inventory_system = InventoryManagementSystem()
    inventory_system.run()

    order_system = OrderManagementSystem()
    order_system.run()

    order_processor = OrderProcessingSystem()
    order_processor.process_orders()

    # Example of using bubble_sort function from sorting_algo module
    my_list = [64, 34, 25, 12, 22, 11, 90]
    sorted_list = bubble_sort(my_list)
    print("Sorted list:", sorted_list)

# Entry point
if __name__ == "__main__":
    main()
