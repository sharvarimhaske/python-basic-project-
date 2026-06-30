import json
import os

FILE_NAME = "inventory.json"

# Load data
def load_data():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []

# Save data
def save_data(data):
    with open(FILE_NAME, "w") as file:
        json.dump(data, file, indent=4)

# Add product
def add_product():
    data = load_data()

    product_id = input("Enter Product ID: ")
    name = input("Enter Product Name: ")
    price = float(input("Enter Product Price: "))
    quantity = int(input("Enter Quantity: "))

    data.append({
        "id": product_id,
        "name": name,
        "price": price,
        "quantity": quantity
    })

    save_data(data)
    print(" Product Added Successfully!")

# View products
def view_products():
    data = load_data()

    if not data:
        print("No products found.")
        return

    print("\n===== INVENTORY LIST =====")
    for p in data:
        print("-" * 30)
        print("ID      :", p["id"])
        print("Name    :", p["name"])
        print("Price   :", p["price"])
        print("Quantity:", p["quantity"])

# Search product
def search_product():
    pid = input("Enter Product ID: ")
    data = load_data()

    for p in data:
        if p["id"] == pid:
            print("\nProduct Found:")
            print(p)
            return

    print(" Product not found")

# Update product
def update_product():
    pid = input("Enter Product ID to Update: ")
    data = load_data()

    for p in data:
        if p["id"] == pid:
            p["name"] = input("Enter New Name: ")
            p["price"] = float(input("Enter New Price: "))
            p["quantity"] = int(input("Enter New Quantity: "))

            save_data(data)
            print("Product Updated Successfully!")
            return

    print(" Product not found")

# Delete product
def delete_product():
    pid = input("Enter Product ID to Delete: ")
    data = load_data()

    new_data = [p for p in data if p["id"] != pid]

    save_data(new_data)
    print(" Product Deleted Successfully!")

# Total inventory value
def total_value():
    data = load_data()

    total = sum(p["price"] * p["quantity"] for p in data)

    print("\n===== TOTAL INVENTORY VALUE =====")
    print("Total Value:", total)

# Menu
while True:
    print("\n===== INVENTORY MANAGEMENT SYSTEM =====")
    print("1. Add Product")
    print("2. View Products")
    print("3. Search Product")
    print("4. Update Product")
    print("5. Delete Product")
    print("6. Total Inventory Value")
    print("7. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        add_product()
    elif choice == "2":
        view_products()
    elif choice == "3":
        search_product()
    elif choice == "4":
        update_product()
    elif choice == "5":
        delete_product()
    elif choice == "6":
        total_value()
    elif choice == "7":
        print("Thank you!")
        break
    else:
        print("Invalid choice!")
