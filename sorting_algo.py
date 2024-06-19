# sorting_algorithms.py

def bubble_sort(products):
    n = len(products)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if products[j][1]['price'] > products[j+1][1]['price']:
                products[j], products[j+1] = products[j+1], products[j]
    return products

# Example usage
if __name__ == "__main__":
    products = [('P001', {'name': 'Smartphone', 'price': 9000}), ('P002', {'name': 'Laptop', 'price': 1000})]
    sorted_products = bubble_sort(products)
    print(sorted_products)
