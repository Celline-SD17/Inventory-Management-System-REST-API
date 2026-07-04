import requests
BASE_URL= "http://127.0.0.1:5000"

def menu():
    while True:
        print("\nInventory Management System")
        print("1. View Inventory")
        print("2. View Item by id")
        print("3. Add Item")
        print("4. Update Item")
        print("5. Delete Item")
        print("6. Search Product by Barcode")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ")

        if choice == "1":
            response = requests.get(f"{BASE_URL}/inventory")
            print(response.json())
        elif choice == "2":
            id = input("Enter the item id: ")
            response = requests.get(f"{BASE_URL}/inventory/{id}")
            print(response.json())
        elif choice == "3":
            barcode = input("Enter the item barcode: ")
            price = float(input("Enter the item price: "))
            stock = int(input("Enter the item stock: "))
            data = {"barcode": barcode, "price": price, "stock": stock}
            response = requests.post(f"{BASE_URL}/inventory", json=data)
            print(response.json())
        elif choice == "4":
            id = input("Enter the item id: ")
            price = float(input("Enter the new price: "))
            stock = int(input("Enter the new stock: "))
            data = {}
            if price:
                data["price"] = float(price)
            if stock:
                data["stock"] = int(stock)
            response = requests.patch(f"{BASE_URL}/inventory/{id}", json=data)
            print(response.json())
        elif choice == "5":
            id = input("Enter the item id:")
            response = requests.delete(f"{BASE_URL}/inventory/{id}")
            print(response.json())
        elif choice == "6":
            barcode = input("Enter the item's barcode: ")
            response = requests.get(f"{BASE_URL}/product/{barcode}")
            print(response.json())
        elif choice == "7":
            print("Exiting the program...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    menu()