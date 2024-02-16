import time


class Restaurant:

  def __init__(self):
    self.menu = {}
    self.table_reservation = {}
    self.orders = []
#-----------------------menu part
#ADDING A NEW DISH TO THE MENU

  def add_dish(self):
    added_dish = input("Enter a dish you want to add to the menu: ")
    added_dish_price = float(input(f"Enter the price of {added_dish}: "))
    self.menu.update({added_dish: added_dish_price})

  #CHANGING THE PRICE OF DISH BASED ON ITS NAME IN MENU
  def change_price(self):
    print("----CHANGE THE PRICE----")
    self.show_menu()
    dish = input("Enter dish you want to change the price of: ")
    if dish in self.menu.keys():
      new_price = float(input(f"A new price of {dish}: "))
      self.menu[dish] = new_price
    else:
      print("This dish is not on the menu.")

  # DELETING DISH FROM THE MENU BASED ON ITS NAME IN MENU
  def delete_dish(self):
    delete_dish = input("What dish do you want to delete: ")
    if delete_dish in self.menu.keys():
      self.menu.pop(delete_dish)
    else:
      print("This dish is not on the menu.")

  # SHOWING THE MENU
  def show_menu(self):
    print("----MENU----")
    menu_list = list(self.menu.items())
    for dish, price in menu_list:
      print(f"{dish}: {price}")

#-----------------------bookings part
# ADDING A NEW RESERVATION: NAME AND NUMBER OF TABLE - IF TABLE IS ALREADY BOOKED -

  def add_reservation(self):
    while True:
      name = input("Enter the name of the person who reserved the table: ")
      table_number = input(f"Enter the number of the table for {name}: ")

      if table_number in self.table_reservation.values():
        print("Table is already booked.")
        retry = input(
          "Do you want to try adding reservation again? (yes/no): ")

        if retry.lower(
        ) == 'yes':  # .lower() makes user's input all to lowercase
          continue
        else:
          print("Reservation canceled.")
          break
      else:
        self.table_reservation[name] = table_number
        print(f"Reservation for {name} at table {table_number} added.")
        break
        self.table_reservation.update({name: table_number})

  # SHOWING ALL THE BOOKINGS: NAME AND TABLE NUMBER
  def show_reservations(self):
    print("----RESERVATIONS LIST----")
    reservations_list = list(self.table_reservation.items())
    for name, table_number in reservations_list:
      print(f"{name}: {table_number}")

  # DELETING THE RESERVATIONS
  def delete_reservation(self):
    delete_reservation = input("Whose booking do you want to delete: ")
    self.table_reservation.pop(delete_reservation)

#-----------------------orders part

# GETTING ORDER ITEMS WITH QUANTITY - GETS CALLED BY THE take_order FUNCTION BELOW

  def get_order_items(self):
    items = []
    print("---You are adding dishes to the new order---")
    while True:
      product_name = input("Enter product name (or 'done' to finish): ")
      if product_name.lower() == 'done':
        break

      # Check if the product name is in the menu
      if product_name in self.menu:
        quantity = int(input("Enter quantity: "))
        items.append((product_name, quantity))
      else:
        print(
          f"Error: {product_name} not found in the menu. Please enter a valid dish."
        )
    return items

#TAKING ORDERS FROM THE CUSTOMER

  def take_order(self):
    order_number = None

    for num in range(1, 21):  #20 max orders
      if num not in (order.get("order_number") for order in self.orders):
        order_number = num
        break

    if order_number is not None:
      items = self.get_order_items()
      new_order = {"order_number": order_number, "items": items}
      self.orders.append(new_order)
      print(f"Order {order_number} placed successfully.")
    else:
      print("No available order numbers. We are full of orders.")

# SHOWING ALL THE CURRENT ORDERS

  def show_orders(self):
    if not self.orders:
      print("Orders list is empty.")
    else:
      print("----ORDERS----")
      for order in self.orders:
        print(f"Order {order['order_number']}: {order['items']}")

# DELETING COMPLETED ORDER

  def delete_order(self):
    order_to_delete = int(input("Enter the order's number to delete: "))
    for order in self.orders:
      if order["order_number"] == order_to_delete:
        self.orders.remove(order)
        print(f"Order {order_to_delete} marked as completed.")
        break
      else:
        print(f"Order {order_to_delete} not found.")


# CALCULATING THE BILL - BASED ON THE ORDER DISHES, THEIR QUANTITY AND PRICES FROM MENU

  def calculate_bill(self):
    order_number_to_calculate = int(
      input("Enter the order's number to calculate and print the bill: "))
    order = next(
      (o
       for o in self.orders if o["order_number"] == order_number_to_calculate),
      None)

    if order:
      total_price = sum(
        int(self.menu[item[0]]) * item[1] for item in order["items"])

      def printing_countdown(seconds):
        for i in range(seconds, 0, -1):
          print("Bill will be printed in ", i, "...")
          time.sleep(1)  # Pause for 1 second

      duration = 5
      printing_countdown(duration)
      print(
        f"Total bill for Order {order_number_to_calculate}: ${total_price}")
      self.orders.remove(
        order)  # Mark the order as completed - gets removed from orders list
      return total_price
    else:
      print(f"Order {order_number_to_calculate} not found.")
      return None

  #---------calling the class' functions
rest = Restaurant()

# rest.add_dish()
# rest.add_dish()
# rest.add_dish()
# rest.show_menu()
# rest.take_order()
# rest.take_order()
# rest.take_order()
# rest.show_orders()
# rest.delete_order()
# rest.show_orders()
# rest.take_order()
# rest.show_orders()
# rest.calculate_bill()
# rest.show_orders()